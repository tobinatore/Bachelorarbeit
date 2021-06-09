from cbor2 import loads


def get_bundle_source(recvd_message: bytes) -> str:
    """Parses the received data and extracts the senders node number.

    Args:
        recvd_message (bytes): Bundle conforming to the Concise Binary Object Representation.

    Returns:
        str: The node number / name of the bundles origin.
    """

    # Decoding the byte-representation and accessing the node number of the sender.
    # see https://datatracker.ietf.org/doc/html/draft-ietf-dtn-bpbis-31#section-4.3.1
    # for the structure of the primary bundle block.
    return str(loads(recvd_message)[0][4][1][0])
