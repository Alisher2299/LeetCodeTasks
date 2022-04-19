"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.


Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
"""


def isValid(s: str) -> bool:
    char_dict = {'(': ')', '[': ']', '{': '}'}
    stack = []

    for i in s:
        if i in char_dict:
            stack.append(i)
        elif len(stack) == 0 or char_dict[stack.pop()] != i:
            return False
    return len(stack) == 0


s = '()'
print(isValid(s))
