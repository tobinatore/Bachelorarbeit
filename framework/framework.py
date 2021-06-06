#!/usr/bin/env python
import argparse
from os import close
import socket
import sys
import threading
import time

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger

import util.utils
from util.nodemanager import NodeManager


def init_argparse() -> argparse.ArgumentParser:

    parser = argparse.ArgumentParser(
        usage="%(prog)s config",
        description="Mitigates Flooding-DDoS-Attacks on DTN-nodes.",
    )

    parser.add_argument("config", help="Path to a configuration file")

    return parser


def bundle_received(nm: NodeManager, nbr: str) -> None:
    """Processes incoming bundles.

    Args:
        nbr (str): Node number / name of the sender.
    """
    if nm.is_neighbour(nbr):
        nm.count_rcvd_bundles(nbr)


def reset_bundle_counts(nm: NodeManager) -> None:
    """Instructs NodeManager to reset the counts of the Bundles which were received in the last
    interval.

    Args:
        nm (NodeManager): Management utility of the node for which the counts should be reset.
    """
    nm.reset_rcvd_bundles()


def listen() -> None:
    print("Listening")
    # Create a socket for incoming traffic
    f_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    f_socket.bind(("", 4555))

    while True:
        message, addr = f_socket.recvfrom(2048)
        util.utils.parse_bundle(message)
        # Forward bundle to the port ION uses
        # -> TODO: Trust check to see if it should be
        # discarded instead
        f_socket.sendto(message, ("127.0.0.1", 4556))


def main(nm: NodeManager) -> None:
    """Main event loop.

    Args:
        nm (NodeManager): [description]
    """

    # Create a thread for listening to incoming messages
    l = threading.Thread(target=listen)
    l.daemon = True
    l.start()

    # Schedule resetting the count of the received bundles
    # every X seconds
    scheduler = BackgroundScheduler()
    scheduler.add_job(
        reset_bundle_counts, IntervalTrigger(seconds=nm.get_reset_time()), args=([nm])
    )
    scheduler.start()
    time.sleep(1000)


if __name__ == "__main__":

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
            nm = NodeManager(args.config)

        except (FileNotFoundError, IsADirectoryError) as err:

            print(f"{sys.argv[0]}: {args.config}: {err.strerror}", file=sys.stderr)
            exit(1)

    # TODO: Graceful shutdown on SIGINT
    main(nm)
