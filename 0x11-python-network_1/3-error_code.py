#!/usr/bin/python3
# Task 3. Error code #0
if __name__ == "__main__":
    from sys import argv
    from urllib import request, error
    the_url = argv[1]
    my_request = request.Request(the_url)
    try:
        with request.urlopen(my_request) as response:
            body = response.read().decode("utf-8")
            print("{}".format(body))
    except error.HTTPError as err:
        print("Error code: {}".format(err.code))
