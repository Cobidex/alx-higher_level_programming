#!/bin/bash
# send JSON POST request, displays body of response.
curl -sX POST -H "Content-Type: application/json" -d @"$2" "$1"
