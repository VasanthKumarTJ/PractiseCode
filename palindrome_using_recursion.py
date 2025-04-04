def palindrome(lst, i):
    if(i>=len(lst)//2):
        return True
    if (lst[i] != lst[len(lst) - i - 1]):
        return False
    return  palindrome(lst, i + 1)


lst = "madeam"
res = palindrome(lst, 0)
print(res)