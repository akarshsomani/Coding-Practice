# https://leetcode.com/problems/move-zeroes/
# complexity n

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        l = len(nums)
        
        non_zero = 0
        for i in range(l):
            if nums[i] != 0:
                
                nums[non_zero] = nums[i]
                non_zero += 1
            # print(nums)
                
        for i in range( non_zero,l):
            nums[i] = 0
