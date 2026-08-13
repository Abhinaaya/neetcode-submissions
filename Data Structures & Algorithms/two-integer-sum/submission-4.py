class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       mp={}
       for i,num in enumerate(nums):
        k=target-num
        if k in mp:
            return [mp[k],i]
        mp[num]=i

        