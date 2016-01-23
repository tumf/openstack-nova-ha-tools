# -*- coding: utf-8 -*-
import os
from novaclient import client

def get_nova_client():
    return client.Client(2,
                         os.environ.get("OS_USERNAME"),
                         os.environ.get("OS_PASSWORD"),
                         os.environ.get("OS_TENANT_NAME"),
                         os.environ.get("OS_AUTH_URL"))
