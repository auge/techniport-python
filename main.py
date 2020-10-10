#!/usr/bin/env python3
import argparse
import json


class TechniPort:
    def __init__(self, host: str, port: int):
        #self._s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #self._s.connect((host, port))
        pass

    def _expect(self, data: bytes):
        r = self._s.recv(len(data))
        if r != data:
            raise Exception('Failed to read expected data.')

    def disconnect(self):
        self._s.send(b'\xff')
        self._s.close()

    def read_device_description(self):
        pass

    def list_dir(self, dir: str):
        if dir is None:
            dir = '/usb1/recordings'

        n_elems = len(path_elements)
        print(path_elements)
        print(n_elems)
        if n_elems > 255:
            raise Exception('Too many path elements.')
        data = b'\x03\x00' + bytes([n_elems])
        print(data)
        self._s.send(data)

    def _change_dir(self, path_elements: [str]):
        pass

    def download_file(self, number: int):
        pass


parser = argparse.ArgumentParser(description='List and download recordings from TechniSat PVR recorders.')
parser.add_argument('-l', '--list', help='List directory', action='store_true')
parser.add_argument('-c', '--change_dir', type=str, metavar='dir', help='Change directory')
parser.add_argument('-d', '--download', type=int, metavar='N', help='Download recording number N')
args = parser.parse_args()
print(args)

with open('config.json', 'r') as fp:
    config = json.load(fp)

t = TechniPort(config['host'], config['port'])

try:
    if args.list:
        t.list_dir(args.change_dir)
    if args.download:
        t.download_file(args.download)
except Exception as e:
    print(e)
finally:
    t.disconnect()
