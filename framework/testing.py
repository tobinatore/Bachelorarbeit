import time
import pyion
import threading
import random


def listen(eid_listen: str, proxy) -> None:
    """Listens on the endpoint specified in the config."""
    count_spam = 0
    count_ham = 0
    with proxy.bp_open(eid_listen) as eid:
        while eid.is_open():
            rcvd = eid.bp_receive()
            if rcvd == b"SPAM":
                count_spam += 1
                f = open("spamcount.txt", "w")
                f.write(count_spam)
                f.close()
            elif rcvd == b"HAM":
                count_ham += 1
                f = open("hamcount.txt", "w")
                f.write(count_ham)
                f.close()


def attack_node(target: str, eid_send: str, proxy) -> None:
    """Floods the node specified in the config with bundles."""
    time.sleep(5)
    with proxy.bp_open(eid_send) as eid:
        while True:
            eid.bp_send(target, b"SPAM")
            time.sleep(0.01)


def sim_traffic(eid_send: str, proxy) -> None:
    i = 0
    sleeptime = 1
    with proxy.bp_open(eid_send) as eid:
        while True:

            # First 10 destinations:
            # 7,6,3,8,3,7,8,6,3,8,7
            if i % 5 == 0:
                dest = "7"
            elif i % 3 == 0:
                dest = "8"
            elif i % 2 == 0:
                dest = "3"
            else:
                dest = "6"

            i += 1

            dest_eid = "ipn:" + dest + ".2"
            eid.bp_send(dest_eid, b"HAM")
            time.sleep(sleeptime)


if __name__ == "__main__":

    pyion.ION_NODE_LIST_DIR = "/home/tobias/Desktop/Bachelorarbeit/Szenario_1/ion_nodes"
    proxy = pyion.get_bp_proxy("2")
    proxy.bp_attach()

    l = threading.Thread(target=listen, args=["2.2", proxy])
    l.daemon = True
    l.start()

    is_attacker = False
    # Simulating normal traffic for non-attackers
    if is_attacker:
        a = threading.Thread(target=attack_node, args=["ipn:6.2", "8.1", proxy])
    else:
        t = threading.Thread(target=sim_traffic, args=["2.1", proxy])
