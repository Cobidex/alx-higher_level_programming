#!/bin/bash
#  sends a request to that URL, and displays the size of the body of the response
curl -sI GET "$1" | grep -i "Content-Length" | cut -d " " -f 2
