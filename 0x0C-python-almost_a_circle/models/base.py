#!/usr/bin/python3
"This is the based module"

import json
import os
import turtle


class Base:
    "this is the main class"


    __nb_objects = 0

    def __init__(self, id=None):
        """establish the private attributes and id fields
        Args:
            id(int): an integer"""
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id
