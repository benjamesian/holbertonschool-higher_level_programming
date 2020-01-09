#!/bin/bash
# send a GET request with a header variable
curl -sLX POST $1 -d "email=hr@holbertonschool.com&subject=I will always be here for PLD"
