#!/bin/bash
# sends a POST request to the passed URL
curl -sL -d "email=test@gmail.com&subject=I will always be here for PLD" -X POST "$1"
