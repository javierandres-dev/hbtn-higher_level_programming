#!/usr/bin/python3
def from_json_string(my_str):
    """
        function that returns an object (Python data structure)
        represented by a JSON string
    """
    import json
    return json.loads(my_str)
