#!/usr/bin/python

import sys
import time

while 1:
    line = sys.stdin.readline()
    if not line: break
    print line, time.ctime()
    print "OK"
    sys.stdout.flush()
