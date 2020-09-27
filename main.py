#!/usr/bin/env python3

import argparse
import json
import socket

with open('config.json', 'r') as fp:
    config = json.load(fp)


class TechniPort:
    def __init__(self, host: str, port: int):
        self._s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._s.connect((host, port))

    def read_device_description(self):
        pass

    def list_dir(self):
        pass

    def change_dir(self, path_elements: dict):
        pass

    def download_file(self, number: int):
        pass

t = TechniPort(config['host'], config['port'])

