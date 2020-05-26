# https://leetcode.com/problems/kth-largest-element-in-an-array/

# complexity nlog(n)

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        nums.sort(reverse = True)
        return(nums[k-1])
        
