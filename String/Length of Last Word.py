"""
Given a string s consisting of some words separated by some number of spaces, return the length of
the last word in the string.

A word is a maximal substring consisting of non-space characters only.
"""


def lengthOfLastWord(s):
    return len(s.split()[-1])


s = "Hello World"

print(lengthOfLastWord(s))
