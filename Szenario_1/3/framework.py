#!/usr/bin/env python
import argparse
import logging
import socket
import sys
import threading
import time
import signal
from util.workermanager import WorkerManager
import psutil
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger

import util.utils
from util.nodemanager import NodeManager


logger = logging.getLogger(__name__)
f_socket: socket.socket
scheduler: BackgroundScheduler


def get_ip_addresses(family: socket.AddressFamily):
    """Returns all network interfaces and their assigned IP addresses.

    Args:
        family (socket.AddressFamily): AF_INET for IPv4, AF_INET6 for IPv6 addresses.

    Yields:
        List[Tuple(str,str)]: A list of all interfaces and their assigned IP addresses
    """

    # This snippet was written by StackOverflow user pmav99
    # Link to answer: https://stackoverflow.com/a/43478599
    for interface, snics in psutil.net_if_addrs().items():
        for snic in snics:
            if snic.family == family:
                yield (interface, snic.address)


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
    print("RESET")
    nm.reset_flag = True
    nm.reset_time_reached()


def wait_for_message(sock: socket.socket, wm: WorkerManager):
    while True:
        message, addr = sock.recvfrom(196)
        threading.Thread(target=wm.add_bundle, args=[message]).start()


def listen(nm: NodeManager, wm: WorkerManager) -> None:
    print("Listening for incoming bundles on node " + nm.get_node_number() + ":")

    ip_list = get_ip_addresses(socket.AF_INET)
    global sockets
    sockets = []

    for address in ip_list:
        if not address[0] == "lo":
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.bind((address[1], 4555))
            print("Bound Socket to interface " + address[0] + ", IP: " + address[1])
            threading.Thread(target=wait_for_message, args=[sock, wm]).start()
            sockets.append(sock)


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

    while True:
        time.sleep(100)


def cleanup() -> None:
    """Closes the socket and shuts down
    the scheduler on SIGINT.
    """

    global sockets
    global scheduler

    logger.info("---------Shutting down----------")
    for sock in sockets:
        sock.close()
    logger.info("Closed sockets")
    scheduler.shutdown()
    logger.info("Shut down scheduler")


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
