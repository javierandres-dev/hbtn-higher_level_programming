#!/usr/bin/python3
# Task 8. Search API
if __name__ == "__main__":
    import sys
    import requests
    the_url = "http://0.0.0.0:5000/search_user"
    if len(sys.argv) > 1:
        the_letter = {"q": sys.argv[1]}
    else:
        the_letter = {'q': ""}
    my_req = requests.post(the_url, the_letter)
    try:
        the_resp = my_req.json()
        if not the_resp:
            print("No result")
        else:
            print("[{}] {}".format(the_resp.get('id'), the_resp.get('name')))
    except:
        print("Not a valid JSON")
