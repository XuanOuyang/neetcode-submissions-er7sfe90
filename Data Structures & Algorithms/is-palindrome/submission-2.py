class Solution:
    def isPalindrome(self, s: str) -> bool:
        #remove all but alphabets make lower and into list
        l = s.lower()
        c = "".join(char for char in l if char.isalnum())
        f = list(c)

        l = 0
        r = len(f) - 1
        while l < r:
            if f[l] != f[r]:
                return False
            l += 1
            r -= 1
        return True