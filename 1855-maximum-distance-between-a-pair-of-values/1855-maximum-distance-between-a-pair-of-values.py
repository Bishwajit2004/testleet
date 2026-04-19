class Solution:
    def maxDistance(self, nums1, nums2):
        i = 0
        res = 0
        
        for j in range(len(nums2)):
            while i < len(nums1) and nums1[i] > nums2[j]:
                i += 1
            if i == len(nums1):
                break
            res = max(res, j - i)
        
        return res