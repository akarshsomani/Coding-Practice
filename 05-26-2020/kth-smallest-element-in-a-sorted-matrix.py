# https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/

# complexity n**2 log(n**2)

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        
        arr = []
        
        for each in matrix:
            arr.extend(each)
            
        arr.sort()
        return(arr[k-1])
