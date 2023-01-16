#!/bin/bash
# displays all HTTP methods the server will accept
curl -s OPTIONS "$1" | grep "Allow" | cut -d ": " -f2
