def palindrome(s):
    for letter in s:
        reverse_s= s[::-1]
        if reverse_s=s:
            return True
