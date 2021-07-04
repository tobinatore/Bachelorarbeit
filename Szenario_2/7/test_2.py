import os
import time
import pyion
import threading


def listen(eid_listen: str, proxy) -> None:
    """Listens on the specified endpoint"""
    with proxy.bp_open(eid_listen) as eid:
        while eid.is_open:
            print(eid.bp_receive())


def sim_traffic(eid_send: str, proxy) -> None:
    i = 0
    sleeptime = 3.3
    with proxy.bp_open(eid_send) as eid:
        while True:

            # First 10 destinations:
            # 11,3,18,24,18,11,24,3,18,24,11
            if i % 5 == 0:
                dest = "11"
            elif i % 3 == 0:
                dest = "24"
            elif i % 2 == 0:
                dest = "18"
            else:
                dest = "3"

            i += 1
            print("sending to "+dest)
            dest_eid = "ipn:" + dest + ".2"
            eid.bp_send(dest_eid, b"HAM", report_eid="ipn:7.2")
            time.sleep(sleeptime)


if __name__ == "__main__":

    pyion.ION_NODE_LIST_DIR = os.path.abspath(os.path.join(".", os.pardir))
    proxy = pyion.get_bp_proxy("7")
    proxy.bp_attach()

    l = threading.Thread(target=listen, args=["ipn:7.2", proxy])
    l.daemon = True
    l.start()

    t = threading.Thread(target=sim_traffic, args=["ipn:7.1", proxy])
    t.daemon = True
    t.start()
        
    while True:
      time.sleep(10)
