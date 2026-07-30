class Solution:
    def isHappy(self, n: int) -> bool:
        slow=n
        fast=self.getsq(n)
        while fast!=1 and slow!=fast:
            slow=self.getsq(slow)
            fast=self.getsq(self.getsq(fast))
        return fast==1
    def getsq(self,n):
        total=0
        while n:
            digit=n%10
            n//=10
            total+=digit*digit
        return total


        