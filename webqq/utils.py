# -*- coding: utf-8 -*-

import Queue


class Chat(object):
    def __init__(self):
        self.msg_queue = Queue.Queue()

    def get_msg(self):
        new_msg = list()
        if self.msg_queue.qsize() > 0:
            for msg in range(self.msg_queue.qsize()):
                new_msg.append(self.msg_queue.get_nowait())

        return new_msg
