#!/usr/bin/python3
"""
module that creates an Object from a “JSON file”:
"""
import json


def load_from_json_file(filename):
    """
    function that creates an Object from a “JSON file”

    Args:
        filename: file name

    """

    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)
    
