# https://leetcode.com/problems/valid-anagram/

# each loop will run only 26 times

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        d1 = {}
        d2 = {}
        for i in range(ord('a'), ord('a')+26):
            d1[chr(i)] = 0
        for i in range(ord('a'), ord('a')+26):
            d2[chr(i)] = 0
        
        for each in s:
            d1[each] += 1
        for each in t:
            d2[each] += 1
            
        for i in range(ord('a'), ord('a')+26):
            if d1[chr(i)] != d2[chr(i)]:
                return False
        
        return True
            
