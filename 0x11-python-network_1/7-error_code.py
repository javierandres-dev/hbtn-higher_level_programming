#!/usr/bin/python3
# Task 7. Error code #1
if __name__ == "__main__":
    import sys
    import requests
    the_url = sys.argv[1]
    my_req = requests.get(the_url)
    the_resp = my_req.status_code
    if the_resp >= 400:
        print("Error code: {}".format(the_resp))
    else:
        print(my_req.text)
