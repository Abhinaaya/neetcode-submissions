class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        mp={}
        for ch in s:
            mp[ch]=mp.get(ch,0)+1
        for k in t:
            if k in mp:
                mp[k]-=1
                if mp[k]==0:
                    del mp[k]
        if not mp:
            return True
        return False

        