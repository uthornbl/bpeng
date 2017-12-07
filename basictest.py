#!/usr/bin/python

import sys
import urllib2

try:
    response = urllib2.urlopen('http://192.168.50.50/', timeout=4)
    html = response.read()
    print("*** Test PASSED ***")
    sys.exit(0)
except Exception as e:
    print("*** Test FAILED ***")
    sys.exit(1)
