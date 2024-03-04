class Solution:
    def isPalindrome(self, x: int) -> bool:
        x=str(x)
        reverse=""
        for i in range(-1,-len(x)-1,-1):
            reverse+=x[i]
        if reverse==x:
            return True
        