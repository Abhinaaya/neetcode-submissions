class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        mp1={}
        mp2={}
        if len(s1)>len(s2):
            return False

        k=len(s1)
        for ch in s1:
            mp1[ch]=mp1.get(ch,0)+1
        for i in range(k):
            chh=s2[i]
            mp2[chh]=mp2.get(chh,0)+1
        if mp1==mp2:
            return True
        l=0
        for r in range(k,len(s2)):
            mp2[s2[r]]=mp2.get(s2[r],0)+1
            
            mp2[s2[l]]-=1
            if mp2[s2[l]]==0:
                del mp2[s2[l]]
            l+=1
            if mp1==mp2:
                return True
        return False
        
        
        

