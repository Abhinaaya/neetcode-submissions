class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=0
        max_freq=0
        max_len=0
        mp={}
        for r in range(len(s)):
            mp[s[r]]=mp.get(s[r],0)+1
            le=r-l+1
            max_freq=max(max_freq,mp[s[r]])
            if le-max_freq>k:
                left_char=s[l]
                mp[left_char]-=1
                l+=1
            max_len=max(max_len,r-l+1)
        return max_len
