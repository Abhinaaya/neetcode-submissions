class Solution:
    def isPalindrome(self, s: str) -> bool:
        ch="".join(i for i in s.lower() if i.isalnum())
        rev_ch=ch[::-1]
        return ch==rev_ch
        