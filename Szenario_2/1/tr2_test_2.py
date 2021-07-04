import time
import pyion
import threading


def listen(eid_listen: str, proxy) -> None:
    """Listens on the endpoint specified in the args."""
    count_spam = 0
    count_ham = 0
    with proxy.bp_open(eid_listen) as eid:
        while eid.is_open:
            rcvd = eid.bp_receive()


def legit_traffic(eid_send: str, proxy) -> None:
    i = 0
    sleeptime = 1
    with proxy.bp_open(eid_send) as eid:
        while i < 100:
            print("Sending to node 29")
            dest = "29"
            dest_eid = "ipn:" + dest + ".2"
            eid.bp_send(dest_eid, b"HAM", report_eid="ipn:1.2")
            time.sleep(sleeptime)
            i += 1
    print("Done.")


if __name__ == "__main__":

    pyion.ION_NODE_LIST_DIR = "/home/tobias/Desktop/Bachelorarbeit/Szenario_2/"
    proxy = pyion.get_bp_proxy("1")
    proxy.bp_attach()

    l = threading.Thread(target=listen, args=["ipn:1.2", proxy])
    l.daemon = True
    l.start()

    # Simulating normal traffic for non-attackers
    t = threading.Thread(target=legit_traffic, args=["ipn:1.1", proxy]).start()

    l.join()
