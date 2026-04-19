class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        seen = {}
        left = 0
        ans = 0

        for right in range(len(s)):
            ch = s[right]

            if ch in seen and seen[ch] >= left:
                left = seen[ch] + 1

            seen[ch] = right
            ans = max(ans, right - left + 1)

        return ans
