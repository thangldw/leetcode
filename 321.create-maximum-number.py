#
# @lc app=leetcode id=321 lang=python3
#
# [321] Create Maximum Number
#

# @lc code=start
class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        def prep(nums, k):
            drop = len(nums) - k
            out = []
            for num in nums:
                while drop and out and out[-1] < num:
                    out.pop()
                    drop -= 1
                out.append(num)
            return out[:k]

        def merge(a, b):
            return [max(a, b).pop(0) for _ in a+b]

        return max(merge(prep(nums1, i), prep(nums2, k-i))
                for i in range(k+1)
                if i <= len(nums1) and k-i <= len(nums2))
        
# @lc code=end

