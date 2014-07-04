#!/usr/bin/env python3.4
# -*- coding: utf-8 -*-

"""Simple random number generator
prints a number between 00 and 100 every 5 seconds
2014 by Antiadriano"""



from random import randint
from time import sleep

if __name__ == "__main__":
    while True:
        print("Number: " + "%02d" % (randint(0, 100)))
        sleep(5)
