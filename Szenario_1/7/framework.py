#!/usr/bin/env python
import argparse
import logging
import socket
import sys
import threading
import time
import signal
from util.workermanager import WorkerManager

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger

import util.utils
from util.nodemanager import NodeManager


logger = logging.getLogger(__name__)
f_socket: socket.socket
scheduler: BackgroundScheduler


def init_argparse() -> argparse.ArgumentParser:

    parser = argparse.ArgumentParser(
        usage="%(prog)s config",
        description="Mitigates Flooding-DDoS-Attacks on DTN-nodes.",
    )

    parser.add_argument("config", help="Path to a configuration file")

    return parser


def interval_reset(nm: NodeManager) -> None:
    """Instructs NodeManager to reset the counts of the Bundles which were received in the last
    interval.

    Args:
        nm (NodeManager): Management utility of the node for which the counts should be reset.
    """
    # print("RESET")
    nm.reset_flag = True
    nm.reset_time_reached()


def listen(nm: NodeManager, wm: WorkerManager) -> None:
    print("Listening for incoming bundles on node " + nm.get_node_number() + ":")

    # Create a socket for incoming traffic
    global f_socket
    f_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    f_socket.bind(("", 4555))

    while True:
        message, addr = f_socket.recvfrom(196)
        threading.Thread(target=wm.add_bundle, args=[message]).start()

        # sender = util.utils.get_bundle_source(message)
        # print("Received Bundle from node " + sender)
        # logger.info("Captured bundle coming from node " + sender)

        # Forward bundle to the port ION uses
        # -> TODO: Trust check to see if it should be
        # discarded instead
        # if nm.is_neighbour(sender):
        # if nm.can_accept_bundle(sender):
        #    print(nm.count_recvd_bundle(sender))
        #    f_socket.sendto(message, ("127.0.0.1", 4556))
        #    nm.count_recvd_bundle(sender)
        #    f_socket.sendto(message, ("127.0.0.1", 4556))
        # else:
        #    f_socket.sendto(message, ("127.0.0.1", 4556))


def main(nm: NodeManager, wm: WorkerManager) -> None:
    """Main event loop.

    Args:
        nm (NodeManager): [description]
    """
    wm.start_workers()
    # Create a thread for listening to incoming messages
    logger.info("Starting thread listening for incoming messages")
    l = threading.Thread(target=listen, args=[nm, wm])
    l.daemon = True
    l.start()

    # Schedule resetting the count of the received bundles
    # every X seconds
    global scheduler
    scheduler = BackgroundScheduler()
    scheduler.add_job(
        interval_reset, IntervalTrigger(seconds=nm.get_reset_time()), args=([nm])
    )
    scheduler.start()
    logging.getLogger("apscheduler").setLevel(logging.WARNING)
    time.sleep(1000)


def cleanup() -> None:
    """Closes the socket and shuts down
    the scheduler on SIGINT.
    """
    global f_socket
    global scheduler

    logger.info("---------Shutting down----------")
    f_socket.close()
    logger.info("Closed socket")
    scheduler.shutdown()
    logger.info("Shut down scheduler")
    nm.shutdown()
    logger.info("Shut down node manager")


def signal_handler(signum, frame) -> None:
    logger.info("Received SIGINT")
    cleanup()
    sys.exit(0)


if __name__ == "__main__":

    # Handling SIGINT
    signal.signal(signal.SIGINT, signal_handler)

    # Initializing logger
    logging.basicConfig(
        filename="framework.log",
        level=logging.INFO,
        format="%(asctime)s %(name)s:%(levelname)s: %(message)s",
        datefmt="[%Y-%m-%d %H:%M:%S]",
    )

    # Parsing command line arguments
    parser = init_argparse()
    args = parser.parse_args()

    if not args.config:
        print("Please provide a configuration file!")
        exit(1)
    else:
        try:
            # Quick test to see if file exists
            f = open(args.config, "r")
            f.close()

            # Initialize NodeManager with config file
            logger.info("Starting NodeManager")
            nm = NodeManager(args.config)

        except (FileNotFoundError, IsADirectoryError) as err:
            logger.error(f"{sys.argv[0]}: {args.config}: {err.strerror}")
            print(f"{sys.argv[0]}: {args.config}: {err.strerror}", file=sys.stderr)
            exit(1)

    logger.info("Entering main event loop.")
    wm = WorkerManager(nm, 25)
    main(nm, wm)
