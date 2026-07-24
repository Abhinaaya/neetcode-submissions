class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        pair=[]
        ans=[]
        def dfs(index,total):
            if total==target:
                ans.append(pair[:])
                return
            if total>target:
                return
            if index>len(candidates):
                return
            for i in range(index,len(candidates)):
                if i>index and candidates[i]==candidates[i-1]:
                    continue
                pair.append(candidates[i])
                dfs(i+1,total+candidates[i])
                pair.pop()
                
        dfs(0,0)
        return ans

        