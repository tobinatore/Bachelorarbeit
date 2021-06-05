import threading
import time

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger

from management.nodemanager import NodeManager


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
    pass


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
    time.sleep(10)


if __name__ == "__main__":
    nm = NodeManager()
    main(nm)
