from management.nodemanager import NodeManager


def bundle_received(nm: NodeManager, nbr: str) -> None:
    """Processes incoming bundles.

    Args:
        nbr (str): Node number / name of the sender.
    """
    if(nm.is_neighbour(nbr)):
        nm.count_rcvd_bundles(nbr)


def listen() -> None:
    pass


if __name__ == "__main__":
    nm = NodeManager()
    # listen()
    while(True):
        print(nm.count_recvd_bundle("2"))
