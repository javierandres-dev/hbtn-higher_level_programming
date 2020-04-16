#!/usr/bin/python3
# Task 6. POST an email #1
if __name__ == "__main__":
    import sys
    import requests
    the_url = sys.argv[1]
    the_email = {"email": sys.argv[2]}
    my_req = requests.post(the_url, the_email)
    body = my_req.text
    print("{}".format(body))
