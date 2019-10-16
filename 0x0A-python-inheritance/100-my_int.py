#!/usr/bin/python3


class MyInt(int):
    def __eq__(self, value):
        return not super().__eq__(value)

    def __ne__(self, value):
        return super().__eq__(value)
