#!/usr/bin/python3
# Task 1. Response header value #0
from sys import argv
import urllib.request
with urllib.request.urlopen(argv[1]) as response:
    html = response.info()
    print("{}".format(html.get("X-Request-Id")))
