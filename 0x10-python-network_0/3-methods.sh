#!/bin/bash
# displays all HTTP methods the server will accept
curl -s GET "$1" | grep "Allow" | cut -d " " -f2 | sed 's/,/, /g'
