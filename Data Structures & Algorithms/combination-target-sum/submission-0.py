class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        pair=[]
        ans=[]
        def dfs(index,total):
            if total==target:
                ans.append(pair[:])
                return
            if total>target:
                return
            if len(nums)==index:
                return 
            pair.append(nums[index])
            dfs(index,total+nums[index])
            pair.pop()
            dfs(index+1,total)
        dfs(0,0)
        return ans
            

        