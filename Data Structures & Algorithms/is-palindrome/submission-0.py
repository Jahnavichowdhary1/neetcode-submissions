class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = ""
        for char in s:
            if char.isalnum():
                result += char.lower()
        first = 0
        last = len(result)-1
        while first<last: 
            if result[first] != result[last]:
                return False
            first += 1
            last -= 1


        return True