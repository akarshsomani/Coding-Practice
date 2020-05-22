# https://www.interviewbit.com/problems/max-sum-contiguous-subarray/

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxSubArray(self, A):
        l = len(A)
        max_gobal =A[0] 
        max_current = A[0] 
          
        for i in range(1,l): 
            max_current = max(A[i], max_current + A[i]) 
            max_gobal = max(max_gobal,max_current) 
              
        return max_gobal 
            
