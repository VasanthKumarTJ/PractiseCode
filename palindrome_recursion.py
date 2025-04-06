def palindrome(n):
    if n <=1:
        return n
    return palindrome(n-1)+ palindrome(n-2)

res = palindrome(4)
print(res)