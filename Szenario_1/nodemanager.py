import pyion
import configparser
import logging


class NodeManager:
    """
    Class containing information about a node. 
    """

    # ------------------------
    # |    INTERNAL VARS     |
    # ------------------------
    __logger = None

    # ------------------------
    # |      NODE VARS       |
    # ------------------------
    __node_num = ""
    __eid_send = ""
    __eid_recv = ""
    __is_flooder = None
    __neighbours = []
    __ion_proxy = None

    # ------------------------
    # |      TRUST VARS      |
    # ------------------------
    __threshold_flooding = 0
    __memory_limits = {}
    __penalty_growth_rate = 0
    __trust_recovery_rate = 0
    __trust_scores = {}

    def __init__(self) -> None:
        # Initialize Logger
        logging.basicConfig(
            filename="framework.log",
            level=logging.INFO,
            format="%(asctime)s %(name)s:%(levelname)s: %(message)s",
            datefmt="[%Y-%m-%d %H:%M:%S]",
        )
        self.__logger = logging.getLogger(__name__)

        config = configparser.ConfigParser()
        config.read("config.ini")

        # Configuring the node
        self.__logger.info("Getting node config")
        self.__node_num = config["NODE_CONFIG"]["node_number"]
        self.__eid_send = config["NODE_CONFIG"]["eid_send"]
        self.__eid_recv = config["NODE_CONFIG"]["eid_receive"]
        self.__is_flooder = config.getboolean("NODE_CONFIG", "is_flooder")
        self.__neighbours = config["NODE_CONFIG"]["neighbours"].split(",")
        self.__ion_proxy = pyion.get_bp_proxy(self.__node_num)

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

        self.__threshold_flooding = int(
            config["TRUST_CONFIG"]["threshold_flooding"])
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

        self.__logger.info(
            "Threshold value for flooding: " +
            str(self.__threshold_flooding) + " bps"
        )
        self.__logger.info("Bundle acceptance cutoff: " +
                           str(self.__memory_limits))
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
        self.__logger.info("Initialized trust scores: " +
                           str(self.__trust_scores))
