'''
Created on Mar 12, 2018

@author: lenovo
'''

def isPalindrome(n):
    s = str(n)
    reverseString = ""
    
    for i in range (len(s) - 1, -1, -1):
        reverseString += s[i]

    return reverseString == s


def findLargestPalindrome():
    palindrome = -1
    
    for i in range (999, 99, -1):
        for j in range (i, 99, -1):
            
            # if product is palindrome and is greater than last recorded palindrome
            if isPalindrome(i * j) and i * j > palindrome:
                palindrome = i * j
    return palindrome;

print (findLargestPalindrome())

