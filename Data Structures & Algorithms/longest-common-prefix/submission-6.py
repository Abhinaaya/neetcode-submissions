class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix=strs[0]
        n=len(strs)
        for i in range  (1,n):
            j=0
            while j<len(prefix) and j<len(strs[i]) and prefix[j]==strs[i][j]:
                j+=1

            prefix=prefix[:j]
            if len(prefix)==0:
                return ""

        return prefix
        