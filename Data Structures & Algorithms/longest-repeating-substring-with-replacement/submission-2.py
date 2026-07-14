class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=0
        mp={}
        max_length=0
        max_freq=0
        for r in range(len(s)):
            mp[s[r]]=mp.get(s[r],0)+1
            le=r-l+1
            max_freq=max(max_freq,mp[s[r]])
            if (le-max_freq>k):
                left_char=s[l]
                mp[left_char]-=1
                l+=1
            max_length=max(max_length,r-l+1)
        return max_length
        



        