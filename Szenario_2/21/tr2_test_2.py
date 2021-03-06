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


def attack(eid_send: str, proxy) -> None:
    i = 0
    sleeptime = 0.01
    with proxy.bp_open(eid_send) as eid:
        while True:
            print("Sending to node 26")
            dest = "26"
            dest_eid = "ipn:" + dest + ".2"
            eid.bp_send(dest_eid, b"SPAM", report_eid="ipn:21.2")
            time.sleep(sleeptime)
            i += 1


if __name__ == "__main__":

    pyion.ION_NODE_LIST_DIR = os.path.abspath(os.path.join(".", os.pardir))
    proxy = pyion.get_bp_proxy("21")
    proxy.bp_attach()

    # Simulating normal traffic for non-attackers
    t = threading.Thread(target=attack, args=["ipn:21.1", proxy]).start()

    t.join()
