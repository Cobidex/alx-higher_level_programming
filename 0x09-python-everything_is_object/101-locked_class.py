#!/usr/bin/python3
"""module to create a locked class"""


class LockedClass():
    """a Locked class"""

    def __setattr__(self, name, value):
        """sets attribute if name is as first_name"""

        if name == "first_name":
            self.__dict__[name] = value
        else:
            raise AttributeError("LockedClass has no attribute '" + Name + "'")
