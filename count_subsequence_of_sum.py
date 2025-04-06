def subsequence(arr, i, target_sum, s):
    n = len(arr)
    if i >= n:
        if s == target_sum:
            return 1
        return 0
    # include the current element
    s += arr[i]
    l = subsequence(arr, i + 1, target_sum, s)
    # exclude the current element
    s -= arr[i]
    r = subsequence(arr, i + 1, target_sum, s)
    return l + r

arr = [1,2,1]
target_sum = 2
result = subsequence(arr, 0, target_sum, 0)
print(result)