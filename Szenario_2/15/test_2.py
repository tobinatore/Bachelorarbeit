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
    sleeptime = 10
    with proxy.bp_open(eid_send) as eid:
        while True:

            # First 10 destinations:
            # 18,25,21,23,21,18,23,25,21,23,18
            if i % 5 == 0:
                dest = "18"
            elif i % 3 == 0:
                dest = "23"
            elif i % 2 == 0:
                dest = "21"
            else:
                dest = "25"

            i += 1
            print("sending to "+dest)
            dest_eid = "ipn:" + dest + ".2"
            eid.bp_send(dest_eid, b"HAM", report_eid="ipn:15.2")
            time.sleep(sleeptime)


if __name__ == "__main__":

    pyion.ION_NODE_LIST_DIR = "/home/tobias/Desktop/Bachelorarbeit/Szenario_2/"
    proxy = pyion.get_bp_proxy("15")
    proxy.bp_attach()

    l = threading.Thread(target=listen, args=["ipn:15.2", proxy])
    l.daemon = True
    l.start()

    t = threading.Thread(target=sim_traffic, args=["ipn:15.1", proxy])
    t.daemon = True
    t.start()
        
    while True:
      time.sleep(10)