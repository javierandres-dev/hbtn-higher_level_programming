#!/usr/bin/python3
# Task 8. Search API
if __name__ == "__main__":
    import sys
    import requests
    the_url = "https://api.github.com/user"
    my_user = sys.argv[1]
    my_pass = sys.argv[2]
    my_requ = requests.get(the_url, auth=(my_user, my_pass))
    the_resp = my_requ.json()
    print("{}".format(the_resp.get("id")))
