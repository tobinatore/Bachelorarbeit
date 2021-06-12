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
    with proxy.bp_open(eid_send) as eid:
        while True:
            dest = str(random.randint(1, 9))
            while dest == "":
                dest = str(random.randint(1, 9))
            dest_eid = "ipn:" + dest + ".2"
            eid.bp_send(dest_eid, b"HAM")
            time.sleep(random.randint(1, 15))


if __name__ == "__main__":

    proxy = pyion.get_bp_proxy("N")
    proxy.bp_attach()

    l = threading.Thread(target=listen, args=["X.2", proxy])
    l.daemon = True
    l.start()

    is_attacker = False
    # Simulating normal traffic for non-attackers
    if is_attacker:
        a = threading.Thread(target=attack_node, args=["ipn:6.2", "8.1", proxy])
    else:
        t = threading.Thread(target=sim_traffic, args=["X.1", proxy])
