#!/bin/bash
# 8. cURL a JSON file
curl -s -X POST -H "Content-Type: application/json" -d @"$2" "$1"
