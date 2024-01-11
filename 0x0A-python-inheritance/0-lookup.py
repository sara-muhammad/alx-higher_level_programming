#!/usr/bin/python3
'''This module to define lookup function'''

def lookup(obj):
    ''' return list of all available attributes and methods in object '''
    return (dir(obj))
