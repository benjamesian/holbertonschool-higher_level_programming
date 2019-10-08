#!/usr/bin/python3
""" SIlly Class """


class LockedClass:
    def __setattr__(self, name, value):
        if name != 'first_name':
            cls_name = self.__class__.__name__
            msg = "'{:s}' object has no attribute '{}'".format(cls_name, name)
            raise AttributeError(msg)
        super().__setattr__(name, value)
