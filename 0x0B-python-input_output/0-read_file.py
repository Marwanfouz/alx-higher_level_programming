#!/usr/bin/python3
"""
    this module contains a function that reads a text file
    (UTF8) and prints it
"""


def read_file(filename=""):
    """Function that reads a text file (UTF8) and prints it to stdout"""
    with open(filename, encoding='utf-8') as f:
        for i in f:
            print(i, end="")
