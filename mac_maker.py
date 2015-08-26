#!/usr/bin/env python
# Written for Python 3
# Raphael Enochian, Aug 2015
from random import SystemRandom
r = SystemRandom()


def get_vendor():
    vendors = {
        'motorola': '1430C6',  # Motorola moto g
        'blackberry': 'A4E4B8',
        'samsung': 'F025B7',    # Galaxy S6
        'apple': 'F0CBA1',  # iPhone
    }
    return r.choice(list(vendors.values()))


def get_device():
    addr = r.randrange(0x999999)
    addr = "{0:0{1}X}".format(addr, 6)
    # ^ https://docs.python.org/3.5/library/string.html#format-string-syntax
    return addr


def formatter(mac):
    raw = [mac[i:i+2] for i in range(0, len(mac), 2)]
    mac = ""
    for i in raw:
        mac += i + ":"
    return mac[:-1]


def main():
    mac = get_vendor() + get_device()
    mac = formatter(mac)
    print(mac)

if __name__ == '__main__':
    main()
