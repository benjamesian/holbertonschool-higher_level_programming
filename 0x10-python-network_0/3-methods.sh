#!/bin/bash
# check http methods a server will accept
curl -siIX OPTIONS $1|awk '/Allow:/{for (i=2;i<NF;i++) printf $i " "; print $NF}'
