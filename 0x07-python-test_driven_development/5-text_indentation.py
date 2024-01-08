#!/usr/bin/python3
"""This module define text Indentation function"""

def text_indentation(text):
    """ Print text with two new lines after each '.', '?'and ':'. 
    Args:
        text(string): The text to print.
    Raises:
        TypeError: If text is not a string.

    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    c = 0
    while c < len(text):
        
        print(f"{text[c]}", end= "")

        if text[c] == "\n" or text[c] in ".?:":
            if text[c] in ".?:":
                print("\n")
            c += 1

        c = c + 1
