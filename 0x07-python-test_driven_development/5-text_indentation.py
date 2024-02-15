#!/usr/bin/python3
# Fuad Hassen <fuadhas6634@gmail.com>
# 5-text_indentation.py
"""This module provide a function that indent text. """


def text_indentation(text):
    """This function indent the text.

    Args:
        text (string): the text to be indented

    Raise:
        TypeError if the text is not string
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for i in range(len(text)):
        if text[i] == '.' or text[i] == '?' or text[i] == ':':
            print(text[i], end="")
            print("\n")
        else:
            if text[i] == " ":
                if text[i - 1] == '.' or text[i - 1] == '?':
                    continue
                if text[i - 1] == ':':
                    continue
            print(text[i], end="")
