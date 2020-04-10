#!/bin/bash
# cURL - displays the size
curl -sD - "$1" | grep Content-Length | cut -d " " -f 2
