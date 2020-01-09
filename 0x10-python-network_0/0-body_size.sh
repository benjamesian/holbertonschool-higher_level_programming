#!/bin/bash
# check content length of a response header
curl $1 -sI | awk '/Content-Length:/{print $2}'
