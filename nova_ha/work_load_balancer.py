# -*- coding: utf-8 -*-
import time
from novaclient.v2.servers import Server
Server.hostname = (lambda self: getattr(self,'OS-EXT-SRV-ATTR:host'))

from auth import get_nova_client


def main():
    runner = WorkLoadBalancer()
    while True:
        time.sleep(5.0)
        runner.run()

class WorkLoadBalancer:
    def __init__(self):
        self.client = get_nova_client()

    def run(self):
        pass

