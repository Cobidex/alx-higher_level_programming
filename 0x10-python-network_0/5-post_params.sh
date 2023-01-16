#!/bin/bash
# displays the body of the response
curl -sX POST "$1" -H "email:test@gmail.com" "subject:I will always be here for PLD"
