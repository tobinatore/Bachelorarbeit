import pyion
import configparser
import logging
from typing import Dict, List


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
    __ion_proxy: any

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

    # ------------------------
    # |    INITIALIZATION    |
    # ------------------------
    def __init__(self, path: str) -> None:

        # Initialize Logger
        logging.basicConfig(
            filename="framework.log",
            level=logging.INFO,
            format="%(asctime)s %(name)s:%(levelname)s: %(message)s",
            datefmt="[%Y-%m-%d %H:%M:%S]",
        )
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
        # self.__ion_proxy = pyion.get_bp_proxy(self.__node_num)

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
        self.__trust_scores = {node: 10 for node in self.__neighbours}
        self.__reset_interval = int(config["TRUST_CONFIG"]["reset_interval"])
        self.__bundles_last_interval = {node: 0 for node in self.__neighbours}

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
        return self.__node_num

    def get_proxy(self) -> object:
        return self.__ion_proxy

    def get_neighbours(self) -> List[str]:
        return self.__neighbours

    def is_neighbour(self, node_nbr: str) -> bool:
        """Checks if a given node is a neighbour of this node.

        Args:
            node_nbr (str): Node number / name of the node to check.

        Returns:
            bool: True if th node is a neighbour, false else.
        """

        return node_nbr in self.__neighbours

    def get_trust_scores(self) -> Dict[str, float]:
        return self.__trust_scores

    def get_reset_time(self) -> int:
        return self.__reset_interval

    def update_trust_scores(self, new_scores: Dict[str, float]) -> None:
        self.__trust_scores = new_scores
