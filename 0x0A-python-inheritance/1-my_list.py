#!/usr/bin/python3
''' This module define class MyList '''

class MyList(list):
    ''' create sorted list '''
    def __init__(self):
        ''' constructor method '''
        super().__init__()
    
    def print_sorted(self):
        ''' print sorted list '''
        print(sorted(self))
