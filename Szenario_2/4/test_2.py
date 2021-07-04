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
    sleeptime = 1
    with proxy.bp_open(eid_send) as eid:
        while True:

            # First 10 destinations:
            # 10,2,17,23,17,10,23,2,17,23,10
            if i % 5 == 0:
                dest = "10"
            elif i % 3 == 0:
                dest = "23"
            elif i % 2 == 0:
                dest = "17"
            else:
                dest = "2"

            i += 1
            print("sending to "+dest)
            dest_eid = "ipn:" + dest + ".2"
            eid.bp_send(dest_eid, b"HAM", report_eid="ipn:4.2")
            time.sleep(sleeptime)


if __name__ == "__main__":

    pyion.ION_NODE_LIST_DIR = os.path.abspath(os.path.join(".", os.pardir))
    proxy = pyion.get_bp_proxy("4")
    proxy.bp_attach()

    l = threading.Thread(target=listen, args=["ipn:4.2", proxy])
    l.daemon = True
    l.start()

    t = threading.Thread(target=sim_traffic, args=["ipn:4.1", proxy])
    t.daemon = True
    t.start()
        
    while True:
      time.sleep(10)
