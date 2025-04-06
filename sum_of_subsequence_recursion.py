
"""
The code below generates all subsequences of the array [3, 1, 2] that sum to a target value of 4.
# It uses recursion to explore both including and excluding each element in the array.
"""
def subsequence(arr, i, narr, target_sum, s):
    n = len(arr)
    if i >= n:
        if s == target_sum:
            print(narr)
        return 
    # include the current element
    narr.append(arr[i])
    s += arr[i]
    subsequence(arr, i + 1, narr, target_sum, s)
    # exclude the current element
    s -= arr[i]
    narr.pop()
    subsequence(arr, i + 1, narr, target_sum, s)

arr = [1,2,1]
narr = []
target_sum = 2
subsequence(arr, 0, narr, target_sum, 0)