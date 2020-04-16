#!/usr/bin/python3
# Task 4. What's my status? #1
if __name__ == "__main__":
    import requests
    my_req = requests.get("https://intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(my_req.text)))
    print("\t- content: {}".format(my_req.text))
