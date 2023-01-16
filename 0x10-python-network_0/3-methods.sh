#!/bin/bash
# displays all HTTP methods the server will accept
curl -s get "$1" | grep "Allow" | cut -d " " -f2 | sed 's/,/, /g'
