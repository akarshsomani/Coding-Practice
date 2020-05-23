# https://www.interviewbit.com/problems/rain-water-trapped/

# complexity of this problem is O(n)

# The logic behind the question is the highest in left and right of the current block which we store in arrays to save the complexity to got to n*2

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def trap(self, A):
        l= len(A)
        
        left = [0]*l
        left[0] = A[0]
        
        # highest building to the left
        for i in range(1, l):
            left[i] = max(left[i-1],A[i])
        
        right = [0]*l
        right[l-1] = A[l-1]
        
        # hightest building to the right
        for i in range(l-2, -1, -1): 
            right[i] = max(right[i + 1], A[i]);
         
        # Min the left and right building minus it's height as the block cannot replace with water
        water = 0   
        for i in range(0, l): 
            water += min(left[i], right[i]) - A[i] 
        
        # print(A)
        # print(left)
        # print(right)
        
        return water
