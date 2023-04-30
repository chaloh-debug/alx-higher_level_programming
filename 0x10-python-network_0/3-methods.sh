#!/bin/bash
#display all methods used
curl -sIL -X OPTIONS "$1" | grep -i Allow | cut -d " " -f2-
