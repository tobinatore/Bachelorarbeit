import time
import pyion
import threading

from pyion.constants import BpAckReqEnum, BpCustodyEnum, BpPriorityEnum, BpReportsEnum


def listen(eid_listen: str, proxy) -> None:
    """Listens on the specified endpoint"""
    with proxy.bp_open(eid_listen) as eid:
        while eid.is_open:
            print(eid.bp_receive())


def sim_traffic(eid_send: str, proxy) -> None:
    i = 0
    time.sleep(1)
    sleeptime = 1.5
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
            print("sending to " + dest)
            eid.bp_send(dest_eid, b"HAM", report_eid="ipn:2.2")
            time.sleep(sleeptime)


if __name__ == "__main__":

    pyion.ION_NODE_LIST_DIR = "/home/tobias/Desktop/Bachelorarbeit/Szenario_1/"
    proxy = pyion.get_bp_proxy("2")
    proxy.bp_attach()

    l = threading.Thread(target=listen, args=["2.2", proxy])
    l.daemon = True
    l.start()

    t = threading.Thread(target=sim_traffic, args=["2.1", proxy])
    t.daemon = True
    t.start()

    while True:
        time.sleep(10)
