#!/usr/bin/env python3
# -*- coding:utf-8-*-
# global variable management module


def init_global_variable():
    """initialize variable"""
    global GLOBALS_DICT
    GLOBALS_DICT = {}


def set_variable(name, value):
    """!
    Set variable

    @param name name: name of the variable
    @param value value: value of the variable

    @return bool: True if the variable is set, False otherwise
    """
    try:
        GLOBALS_DICT[name] = value
        return True
    except KeyError:
        return False


def get_variable(name):
    """!
    A function used to retrieve a variable

    @param name name: name of the variable
    
    @return value: value of the variable
    """
    try:
        return GLOBALS_DICT[name]
    except KeyError:
        return "Not Found"