import os
import time
import pyion
import threading


def listen(eid_listen: str, proxy) -> None:
    """Listens on the endpoint specified in the config."""
    count_spam = 0
    count_ham = 0
    with proxy.bp_open(eid_listen) as eid:
        while eid.is_open:
            rcvd = eid.bp_receive()
            if rcvd == b"HAM":
                count_ham += 1
                f = open("hamcount.txt", "w")
                f.write(str(count_ham))
                f.close()


if __name__ == "__main__":

    pyion.ION_NODE_LIST_DIR = os.path.abspath(os.path.join(".", os.pardir))
    proxy = pyion.get_bp_proxy("9")
    proxy.bp_attach()

    l = threading.Thread(target=listen, args=["ipn:9.2", proxy])
    l.daemon = True
    l.start()
    l.join()
