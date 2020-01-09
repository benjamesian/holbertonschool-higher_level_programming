#!/bin/bash
# send a GET request with a header variable
curl -sLX GET $1 -H "X-HolbertonSchool-User-Id: 98"
