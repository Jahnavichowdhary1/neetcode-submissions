class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = ""

        longest = 0

        for ch in s:
            while ch in res:
                res = res[1:]

            res += ch

            longest = max(longest, len(res))

        return longest