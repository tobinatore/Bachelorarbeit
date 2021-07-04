import configparser
import logging
import math
import os
import subprocess
import time
from typing import Dict, List, Set
import threading

import pyion
import util.utils


class NodeManager:
    """
    Class containing information about a node.
    """

    # ------------------------
    # |    INTERNAL VARS     |
    # ------------------------
    __logger: logging.Logger

    # ------------------------
    # |      NODE VARS       |
    # ------------------------
    __node_num: str
    __eid_send: str
    __eid_recv: str
    __is_flooder: bool
    __neighbours: List[str]
    __node_dir: str

    # ------------------------
    # |      TRUST VARS      |
    # ------------------------
    __threshold_flooding: int
    __memory_limits: Dict[float, int]
    __penalty_growth_rate: float
    __trust_recovery_rate: float
    __trust_scores: Dict[str, float]
    __reset_interval: int
    __bundles_last_interval: Dict[str, int]
    reset_flag: bool
    __mem_percentage: float
    __banned_nodes: Set[str]

    # ------------------------
    # |    INITIALIZATION    |
    # ------------------------
    def __init__(self, path: str) -> None:

        # Initialize Logger
        self.__logger = logging.getLogger(__name__)

        config = configparser.ConfigParser()
        config.read(path)

        # Configuring the node
        self.__logger.info("Getting node config")
        self.__node_num = config["NODE_CONFIG"]["node_number"]
        self.__eid_send = config["NODE_CONFIG"]["eid_send"]
        self.__eid_recv = config["NODE_CONFIG"]["eid_receive"]
        self.__is_flooder = config.getboolean("NODE_CONFIG", "is_flooder")
        self.__neighbours = config["NODE_CONFIG"]["neighbours"].split(",")
        self.__node_dir = config["NODE_CONFIG"]["node_dir"]

        # Logging results
        self.__logger.info("Node number: " + str(self.__node_num))
        self.__logger.info("Sending from EID " + self.__eid_send)
        self.__logger.info("Receiving critical info on EID " + self.__eid_recv)
        self.__logger.info(
            "Node is flooder: " + ("no" if not self.__is_flooder else "yes")
        )
        self.__logger.info("Neighbours: " + str(self.__neighbours))
        self.__logger.info("Initialized proxy to ION engine.")

        # Initializing the trust system
        self.__logger.info("Initializing trust system")
        self.__threshold_flooding = int(config["TRUST_CONFIG"]["threshold_flooding"])
        l = [
            word
            for line in config["TRUST_CONFIG"]["memory_limits"].split("|")
            for word in line.split(",")
        ]
        it = iter(l)
        self.__memory_limits = {
            float(score): int(limit) for score, limit in zip(it, it)
        }
        self.__penalty_growth_rate = float(
            config["TRUST_CONFIG"]["punishment_growth_rate"]
        )
        self.__trust_recovery_rate = float(
            config["TRUST_CONFIG"]["trust_recovery_rate"]
        )
        self.__trust_scores = {node: 10.0 for node in self.__neighbours}
        self.__reset_interval = int(config["TRUST_CONFIG"]["reset_interval"])
        self.__bundles_last_interval = {node: 0 for node in self.__neighbours}
        self.reset_flag = False
        self.__mem_percentage = 0.0
        self.__banned_nodes = set()

        # Logging the results
        self.__logger.info(
            "Threshold value for flooding: " + str(self.__threshold_flooding) + " bps"
        )
        self.__logger.info("Bundle acceptance cutoff: " + str(self.__memory_limits))
        self.__logger.info(
            "Growth of penalty function: "
            + (
                "linear"
                if self.__penalty_growth_rate == 1.0
                else "exponential (factor: " + str(self.__penalty_growth_rate) + ")"
            )
        )
        self.__logger.info(
            "Trust recovery rate: "
            + (
                ("disabled")
                if self.__trust_recovery_rate == 0
                else str(self.__trust_recovery_rate)
            )
        )
        self.__logger.info("Initialized trust scores: " + str(self.__trust_scores))
        self.__logger.info(
            "Bundle count reset interval set to: "
            + str(self.__reset_interval)
            + " seconds"
        )
        self.__logger.info(
            "Initialized bundles received in the last "
            + str(self.__reset_interval)
            + " seconds: "
            + str(self.__bundles_last_interval)
        )

    def count_recvd_bundle(self, node_nbr: str, no_bundles: int = 1) -> int:
        """Updates the __bundles_last_interval variable by adding the number of bundles which were newly received.

        Args:
            node_nbr (str): Node number / name of the sender.
            no_bundles (int, optional): Number of bundles node_nbr sent. Defaults to 1.

        Returns:
            int: The number of bundles exceeding __threshold_flooding.
        """
        if self.reset_flag:
            self.__bundles_last_interval[node_nbr] = no_bundles
            self.reset_flag = False
        else:
            self.__bundles_last_interval[node_nbr] += no_bundles
        return (
            0
            if self.__bundles_last_interval[node_nbr] <= self.__threshold_flooding
            else self.__bundles_last_interval[node_nbr] - self.__threshold_flooding
        )

    def reset_rcvd_bundles(self) -> None:
        """Resets the count of bundles received in the last second to 0 for each neighbour."""
        self.__bundles_last_interval = {node: 0 for node in self.__neighbours}

    def get_node_number(self) -> str:
        """Returns own node number

        Returns:
            str: The node number / name of this node
        """
        return self.__node_num

    def get_ion_proxy(self) -> object:
        return self.__ion_proxy

    def get_neighbours(self) -> List[str]:
        """Returns all neighbours of this node.

        Returns:
            List[str]: List of neighbours
        """
        return self.__neighbours

    def is_neighbour(self, node_nbr: str) -> bool:
        """Checks if a given node is a neighbour of this node.

        Args:
            node_nbr (str): Node number / name of the node to check.

        Returns:
            bool: True if the node is a neighbour, False else.
        """

        return node_nbr in self.__neighbours

    def get_trust_scores(self) -> Dict[str, float]:
        """Returns a dict containing the trust scores for all
        neighbouring nodes.

        Returns:
            Dict[str, float]: Dict in the format {node:trust_score,...}
        """
        return self.__trust_scores

    def get_reset_time(self) -> int:
        """Returns the reset interval as specified in the
        configuration file.

        Returns:
            int: The reset interval in seconds
        """
        return self.__reset_interval

    def update_trust_scores(self, new_scores: Dict[str, float]) -> None:
        """Sets the trust scores to the supplied values.

        Args:
            new_scores (Dict[str, float]): A dict containing the new scores.
        """
        self.__trust_scores = new_scores
        self.__logger.info("New Trust Scores:" + str(self.__trust_scores))

    def can_accept_bundle(self, node: str) -> bool:
        """Compares memory usage with the cutoff value
        defined by the senders current trust score and decides
        whether to accept or decline the bundle.

        Args:
            node (str): The node number of the sender

        Returns:
            bool: Decision on whether to accept or decline the bundle.
                    True if bundle gets accepted
                    False else
        """

        current_trust = self.__trust_scores[node]
        self.__logger.info("TRUST FOR NODE " + node + ": " + str(current_trust))
        if current_trust > 0:
            # find cutoff by evaluating all key of the dict
            # and choosing the one closest (but still less than)
            # or equal to current_trust
            # Snippet adapted from https://stackoverflow.com/a/37851350
            cutoff = self.__memory_limits[
                max(
                    key
                    for key in map(int, self.__memory_limits.keys())
                    if key <= current_trust
                )
            ]

            return True if self.__mem_percentage < cutoff else False
        else:
            # the sender has a trust score of 0
            # -> do not accept any of its bundles
            self.__logger.info("NOT ACCEPTING BUNDLE")
            self.__banned_nodes.add(node)
            return False

    def reset_time_reached(self) -> None:
        """The specified time has elapsed, calculates new trust scores."""
        util.utils.calc_penalty(
            self,
            self.__bundles_last_interval,
            self.__trust_scores,
            self.__threshold_flooding,
            self.__penalty_growth_rate,
            self.__trust_recovery_rate,
        )
        self.__mem_percentage = self.calc_memory_percentage()

    def calc_memory_percentage(self) -> float:
        """Calculates the percentage of unavailable memory space.

        Returns:
            float: Percentage of memory used
        """
        nn = self.__node_num

        # change directories to the node's directory
        # so the SDR can be queried
        os.chdir(self.__node_dir)

        # Query ION's SDR memory
        process = subprocess.run(
            ["ip netns exec nns" + nn + " sdrwatch n" + nn],
            capture_output=True,
            shell=True,
        )
        stdout = process.stdout
        stdout = stdout.decode("utf-8").split("\n")
        for string in stdout:
            if "total now in use" in string:
                used = string
            elif "total heap size" in string:
                total = string

        # sdrwatch returns a string in the format "total heap:              40000"
        # -> the number needs to be extracted
        total = [int(n) for n in total.split() if n.isdigit()][0]
        used = [int(n) for n in used.split() if n.isdigit()][0]
        perc = (float(used) / total) * 100
        self.__logger.info("Memory in use:" + str(perc))
        return perc

    def get_banned_nodes(self) -> List[str]:
        return self.__banned_nodes
