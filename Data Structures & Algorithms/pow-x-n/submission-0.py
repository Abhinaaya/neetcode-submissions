class Solution:
    def myPow(self, x: float, n: int) -> float:
        ans=1
        if n<0:
            n=-n
            x=1/x
        while n:
            if n%2!=0:
                ans*=x
            x*=x
            n//=2
        
        return ans
        