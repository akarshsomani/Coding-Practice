# https://leetcode.com/problems/move-zeroes/

# Complexity n**2
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        l = len(nums)
        for i in range(l):
            j = i
            if(nums[i] != 0):
                while(j>0):
                    if(nums[j-1] == 0):
                        nums[j], nums[j-1] = nums[j-1], nums[j]
                        j -= 1
                    else:
                        break
                #print(nums)
