class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        s = {}
        res = []
        for i in nums:
            if i in s:
                s[i] = s[i]+1
            else:
                s[i] = 1

        # for i, count in s.items():
        #     if count >= k:
        #         res.append(i)
        # return res 
        sorted_items = sorted(s.items(), key=lambda x: x[1], reverse=True)
        for i in range(k):
            res.append(sorted_items[i][0])

        return res
        