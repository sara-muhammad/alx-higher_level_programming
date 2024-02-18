#!/usr/bin/python3
""" Module contains a function that reads a text file (UTF8) and prints it to stdout"""

def read_file(filename=""):
    """ read file element 
    Args:
        filename: name of the file to be read
    """

    with open(filename,'r', encoding = "utf-8") as myfile:
        line = myfile.readlines()
        for i in line:
            print(i , end="")
