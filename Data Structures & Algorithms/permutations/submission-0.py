class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        perm=[]
        used=[False]*(len(nums))
        def dfs():
            if len(perm)==len(nums):
                ans.append(perm[:])
                return
            for i in range(len(nums)):
                if used[i]:
                    continue
                
                used[i]=True
                perm.append(nums[i])
                dfs()
                perm.pop()
                used[i]=False
                
        dfs()
        return ans