#!/usr/bin/python3

def uppercase(s):
    for i in range(len(s)):
        c = s[i]
        if ord('a') <= ord(c) <= ord('z'):
            c = chr(ord(c) - 32)
        print("{}".format(c), end="")
    print()
