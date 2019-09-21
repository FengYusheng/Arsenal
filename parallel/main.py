# -*- coding: utf-8 -*-
import time
import multiprocessing
import sys
import signal
import os

from common.parallel import *


def target_func_(q):
    q.put(os.getpid())
    time.sleep(1)


if __name__ == '__main__':
    # queue = multiprocessing.Queue(15)
    # https://my.oschina.net/yangyanxing/blog/296052
    # https://stackoverflow.com/questions/43155553/python-3-5-multiprocessing-pool-and-queue-dont-work

    # manager = multiprocessing.Manager()
    # queue = manager.Queue()

    # NOTE: https://stackoverflow.com/questions/26578799/send-sigint-to-python-subprocess-using-os-kill-as-if-pressing-ctrlc
    # We can't send signal on Windows like Unix.

    signal.signal(signal.SIGTERM, signal.SIG_IGN)
    signal.signal(signal.SIGINT, signal.SIG_IGN)

    print("Main process ", os.getpid(), " starts!")
    worker1 = Workers(name="Worker1")
    worker2 = Workers(name="Worker2")

    worker1.start()
    worker2.start()

    # Child received signal, then main received it.
    worker1.join()
    worker2.join()
    print(worker1.exitcode == signal.SIGINT)
    print('Main finished.')
