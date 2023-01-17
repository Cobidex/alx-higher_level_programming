#!/bin/bash
# makes a request to 0.0.0.0:5000/catch_me that causes the server to respond
curl -sLX PUT -H "Origin: HolbertonSchool" -d "user_id=98" "http://0.0.0.0:5000/catch_me"
