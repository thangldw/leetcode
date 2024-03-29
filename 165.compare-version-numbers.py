#
# @lc app=leetcode id=165 lang=python3
#
# [165] Compare Version Numbers
#

# @lc code=start
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        s1 = [int(i) for i in version1.split(".")]
        s2 = [int(i) for i in version2.split(".")]
        
        l1, l2 = len(s1), len(s2)
        if l1 < l2: s1 += [0]*(l2-l1) 
        else: s2 += [0]*(l1 - l2)
            
        return (s1 > s2) - (s1 < s2)
        
# @lc code=end

