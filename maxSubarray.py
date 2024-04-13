import math
import os
import random
import re
import sys

#
# Complete the 'maxSubarray' function below.
# https://www.hackerrank.com/challenges/maxsubarray/problem
#  ralizado por Jairo Cogollo
#  mickt681@gmail.com
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def max_subarray(arr:list):
    maxSumSequence = maxSubarraySum = arr[0]
    currentSubsequenceSum = max(arr[0], 0)
    for i in range(1, len(arr)):
        maxSumSequence = max(maxSumSequence + arr[i], maxSumSequence)
        currentSubsequenceSum = max(arr[i], currentSubsequenceSum + arr[i])
        maxSubarraySum = max(maxSubarraySum, currentSubsequenceSum)
    return [maxSubarraySum, maxSumSequence]

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())
    '''enter the value of t  '''

    for t_itr in range(t):
        n = int(input("").strip())
        '''enter the value of n  '''

        arr = list(map(int, input().rstrip().split()))
        '''enter the value of arr'''

        result = max_subarray(arr)
        print(result[0], result[1])

    #     fptr.write(' '.join(map(str, result)))
    #     fptr.write('\n')

    # fptr.close()
