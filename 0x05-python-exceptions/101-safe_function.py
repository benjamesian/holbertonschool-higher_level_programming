#!/usr/bin/python3

import sys
def safe_function(fct, *args):
    try:
        return fct(*args)
    except Exception as inst:
        sys.stderr.write("Exception: {}\n", inst)
        return None
