class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        chars = []
        for char in s:
            if char.isalnum():
                chars.append(char)
        left = 0
        right = len(chars) - 1
        while right > left:
            if chars[left] != chars[right]:
                return False
            left += 1
            right -= 1
        return True
        