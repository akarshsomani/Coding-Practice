# https://leetcode.com/problems/group-anagrams/

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        l = len(strs)
        
        d = {}
        
        for i in range(l):
            s = ''.join(sorted(strs[i]))
            # print(s)
            if s in d.keys():
                d[s].append(strs[i])
            else:
                d[s] = [strs[i]]
        # print(d.values())
        return d.values()
        
