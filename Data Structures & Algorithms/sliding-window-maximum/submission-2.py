class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # result = []

        # for i in range(len(nums) - k + 1):
        #     window = nums[i:i + k]
        #     result.append(max(window))

        # return result
        from collections import deque
        dq = deque()
        result = []

        for right in range(len(nums)):
            # Remove indexes outside the current window
            while dq and dq[0] <= right - k:
                dq.popleft()

            # Remove smaller values from the back
            while dq and nums[dq[-1]] <= nums[right]:
                dq.pop()

            dq.append(right)

            # Record the maximum once the first window is full
            if right >= k - 1:
                result.append(nums[dq[0]])

        return result