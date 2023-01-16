#!/bin/bash
# sends request to URL and displays only the status code response
curl -s -o /dev/null -w "%{http_code}" "$1"
