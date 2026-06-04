class Solution:
    def isPalindrome(self, s: str) -> bool:
        #need all lower case and no symbols and becomes array
        t = s.lower().replace(" ", "")
        u = "".join(f for f in t if f.isalnum())
        v = list(u)
        #now 2 pointer
        left = 0
        right = len(v) - 1

        while left < right:
            if v[left] != v[right]:
                return False
            left += 1
            right -= 1   
        return True
