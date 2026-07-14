class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        mp={}
        n=len(s1)
        for ch in s1:
            mp[ch]=mp.get(ch,0)+1
        for i in range(len(s2)):
            chh=s2[i]
            if chh in mp:
                new_s2=s2[i:i+n]
                if sorted(s1)==sorted(new_s2):
                    return True
        return False


