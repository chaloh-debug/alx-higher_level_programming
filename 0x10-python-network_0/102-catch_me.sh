#!/bin/bash
#specific response from server
curl -sL 0.0.0.0:5000/catch_me -X PUT -H "Origin:You got me!"
