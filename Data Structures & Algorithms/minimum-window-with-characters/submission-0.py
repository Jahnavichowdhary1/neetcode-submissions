from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(t)> len(s):
            return ""

        need = Counter(t)
        window = {}

        have = 0
        left = 0
        required = len(need)

        res = [-1, -1]
        res_len = float("inf")
        for right , ch in enumerate(s):
            window[ch] = window.get(ch, 0) +1
            
            if ch in need and window[ch] == need[ch]:
                have += 1

            while have == required:
                current_len = right -left +1


                if current_len < res_len:
                    res = [left, right]
                    res_len = current_len

                left_char = s[left]
                window[left_char] -= 1

                if (left_char in need and window[left_char] < need[left_char]):
                    have -= 1

                left += 1

        if res_len == float("inf"):
            return ""

        return s[res[0]:res[1] + 1]

