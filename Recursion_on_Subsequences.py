
"""
The below code generates all subsequences of the array [3, 1, 2].
The subsequences are printed one by one.
"""
def subsequence(arr, n, i, sq):
    if i >= n:
        print(sq)
        return 
    # include the current element
    sq.append(arr[i])
    subsequence(arr, n, i + 1, sq)
    # exclude the current element
    sq.pop()
    subsequence(arr, n, i + 1, sq)

arr = [3,1,2]
n = 3
sq = []
subsequence(arr, n, 0, sq)


