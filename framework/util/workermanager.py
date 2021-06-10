import queue
import socket
import threading
import time
from typing import List

from . import utils
from .nodemanager import NodeManager


class WorkerManager:
    __workers: List[threading.Thread]
    __worker_pool: int
    bundle_queue: queue.Queue
    __socket_queue: queue.Queue
    __node_manager: NodeManager

    def __init__(self, nm: NodeManager, worker_pool: int = 10) -> None:
        """Initializes a new WorkerManager-Object with a set amount of
        worker threads.

        Args:
            nm: NodeManager of the node the framework runs on.
            worker_pool (int, optional): The number of threads this object can spawn. Defaults to 10.
        """
        self.bundle_queue = queue.Queue()
        self.__socket_queue = queue.Queue()
        self.__workers = []
        self.__worker_pool = worker_pool
        self.__node_manager = nm

        for i in range(worker_pool):
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.bind(("", 4554 - i))
            self.__socket_queue.put(sock)

    def start_workers(self) -> None:
        for i in range(self.__worker_pool):
            thread = threading.Thread(target=self.__work)
            thread.daemon = True
            thread.start()
            self.__workers.append(thread)

    def __work(self) -> None:
        """Takes bundles from the bundle queue,
        parses the source and checks whether the
        bundle shoudl be accepted.
        """
        while True:
            if not self.bundle_queue.empty():
                bundle = self.bundle_queue.get()
                sender = utils.get_bundle_source(bundle)
                # print(sender)
                if self.__node_manager.is_neighbour(sender):
                    self.__node_manager.count_recvd_bundle(sender)
                    # if self.__node_manager.can_accept_bundle(sender):
                    sock = self.__socket_queue.get()
                    sock.sendto(bundle, ("127.0.0.1", 4556))
                    self.__socket_queue.put(sock)
                else:
                    sock = self.__socket_queue.get()
                    sock.sendto(bundle, ("127.0.0.1", 4556))
                    self.__socket_queue.put(sock)
            else:
                time.sleep(1)

    def add_bundle(self, bundle: bytes) -> None:
        self.bundle_queue.put(bundle)
