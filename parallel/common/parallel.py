# -*- coding: utf-8 -*-
"""
Various methods of multi-process creation.
1. Create multiple processes, Process, Pool
2. Start multiple processes, start(), join().
3. Terminate child processes, terminate().
4. Logging.

Reference:
1. http://www.blog.pythonlibrary.org/2016/08/02/python-201-a-multiprocessing-tutorial/
2. https://thief.one/2016/11/24/Multiprocessing-Pool/
3. Performance test: https://www.ellicium.com/python-multiprocessing-pool-process/
4. https://www.cnblogs.com/gengyi/p/8586357.html
5. 关闭进程 https://www.cnblogs.com/alan-babyblog/p/5351031.html
6. signal: http://brieflyx.me/2015/python-module/python-signal-module/
7. https://stackoverflow.com/questions/1408356/keyboard-interrupts-with-pythons-multiprocessing-pool
"""
import multiprocessing.pool
import multiprocessing
import signal
import time
import sys
import os


def child_signal_handler(num, frame):
    pid = os.getpid()
    print('{0} was killed'.format(pid))
    sys.exit('{0} was killed'.format(pid))



class Workers(multiprocessing.Process):
    def __init__(self, count=None, name='worker'):
        super(Workers, self).__init__()
        self.count_ = multiprocessing.cpu_count() - 1 if not count else count
        self.name_ = name
        self.daemon = True

    def exit_handler(self, num, frame):
        print(self.pid, "was killed.")
        sys.exit("Bye bye {0}".format(self.pid))

    def run(self):
        # The child process can receive the signal, though parent process has received the signal.
        signal.signal(signal.SIGTERM, self.exit_handler)
        signal.signal(signal.SIGINT, self.exit_handler)
        print('{0} starts'.format(self.name))
        print('{0} pid {1}'.format(self.name, self.pid))
        time.sleep(2)
        print('{0} ends'.format(self.name))


__all__ = [
    'Workers',
    'child_signal_handler'
]

