from util.nodemanager import NodeManager
from cbor2 import loads
from typing import Dict
import logging
import queue
import threading
import time

logger = logging.getLogger(__name__)


def get_bundle_source(recvd_message: bytes) -> str:
    """Parses the received data and extracts the senders node number.

    Args:
        recvd_message (bytes): Bundle conforming to the Concise Binary Object Representation.

    Returns:
        str: The node number / name of the bundles origin.
    """
    sender = None
    # Decoding the byte-representation and accessing the node number of the sender.
    # see https://datatracker.ietf.org/doc/html/draft-ietf-dtn-bpbis-31#section-4.3.1
    # for the structure of the primary bundle block.
    try:
        sender = str(loads(recvd_message)[0][4][1][0])
    except Exception:
        print("Error getting sender")

    # In case there is no sender specified in the bundle,
    # check if there's a report eid
    if sender == None:
        try:
            sender = str(loads(recvd_message)[0][5][1][0])
        except Exception:
            print("Error getting report eid")

    return sender


def calc_penalty(
    nm: NodeManager,
    bundles: Dict[str, int],
    scores: Dict[str, float],
    threshold: int,
    factor: float = 1.5,
    rec_rate: float = 0.1,
) -> None:
    """Calculates the penalty a node gets for sending
    too many bundles in a short timeframe.

    Args:
        nm (NodeManager): Manager of the node for whose neighbours the trust scores are calculated.
        bundles (Dict[str, int]): The amount of bundles received from each neighbour in the last interval.
        scores (Dict[str, float]): The current trust scores for all neighbours.
        threshold (int): The amount of bundles after which sending more bundles is considered flooding.
        factor (float, optional): Exponent of the penalty function. Defaults to 1.5.
        rec_rate (float, optional): The amount of trust a node regenerates if it didn't flood. Defaults to 0.1.
    """
    for node in bundles:
        value = bundles[node]
        logger.info("Bundles from node " + str(node) + ": " + str(value))
        if value > threshold:
            scores[node] = max(
                (scores[node] - (((value - threshold) ** factor) * 0.1)), 0
            )
            logger.info("NEW SCORE NODE " + node + ": " + str(scores[node]))
        elif scores[node] < 10 and scores[node] > 0:
            scores[node] += rec_rate

        if scores[node] > 10:
            scores[node] = 10
    nm.update_trust_scores(scores)
