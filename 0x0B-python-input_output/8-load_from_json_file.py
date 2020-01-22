#!/usr/bin/python3
def load_from_json_file(filename):
    """
        function that creates an Object from a “JSON file”
    """
    import json
    with open(filename) as f:
        new_obj = json.load(f)
        return new_obj
