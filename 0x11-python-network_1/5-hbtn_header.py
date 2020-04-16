#!/usr/bin/python3
# Task 5. Response header value #1
if __name__ == "__main__":
    import sys
    import requests
    the_url = sys.argv[1]
    my_req = requests.get(the_url)
    print("{}".format(my_req.headers.get("X-Request-Id")))
