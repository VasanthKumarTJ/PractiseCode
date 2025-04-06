# print only one sum of subsequence of an array that equals a target sum
def subsequence(arr, i, narr, target_sum, s):
    n = len(arr)
    if i >= n:
        if s == target_sum:
            print(narr)
            return True
        return False
    # include the current element
    narr.append(arr[i])
    s += arr[i]
    if subsequence(arr, i + 1, narr, target_sum, s):
        return True
    # exclude the current element
    s -= arr[i]
    narr.pop()
    if subsequence(arr, i + 1, narr, target_sum, s):
        return True
    return False    

arr = [1,2,1]
narr = []
target_sum = 2
subsequence(arr, 0, narr, target_sum, 0)