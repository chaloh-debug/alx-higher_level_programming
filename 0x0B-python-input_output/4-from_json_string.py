#!/usr/bin/python3
"""
module to decode a JSON file
"""
import json


def from_json_string(my_str):
    """

    function that returns an object represented by a JSON string:

    Args:
        my_str: JSON file

    """

    return json.loads(my_str)
