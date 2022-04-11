"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all
non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters
include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.



Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
"""


# def isPalindrome(s: str) -> bool:
#     """
#     My bad solution
#     """
#     l = []
#
#     for i in s:
#         if not i.isalnum():
#             continue
#         l.append(i)
#
#     n_s = ''.join(l).lower()
#     aa = n_s[::-1]
#
#     if aa == n_s:
#         return True
#     return False

def isPalindrome(s):
    s = ''.join(e for e in s if e.isalnum()).lower()
    return s == s[::-1]


s = "A man, a plan, a canal: Panama"

print(isPalindrome(s))
