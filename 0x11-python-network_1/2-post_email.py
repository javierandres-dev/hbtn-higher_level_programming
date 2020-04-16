#!/usr/bin/python3
# Task 2. POST an email #0
if __name__ == "__main__":
    from sys import argv
    import urllib.request
    the_url = argv[1]
    the_email = {"email": argv[2]}
    email = urllib.parse.urlencode(the_email)
    email = email.encode("utf-8")
    my_request = urllib.request.Request(the_url, email)
    with urllib.request.urlopen(my_request) as response:
        body = response.read().decode("utf-8")
        print("{}".format(body))
