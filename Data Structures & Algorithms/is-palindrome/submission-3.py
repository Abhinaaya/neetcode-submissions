class Solution:
    def isPalindrome(self, s: str) -> bool:
        ch="".join(i for i in s.lower() if i.isalnum())
        l=0
        r=len(ch)-1
        while l<r:
            if ch[l]!=ch[r]:
                return False
            l+=1
            r-=1
        return True
        