class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_multi=[1]*(len(nums))
        for i in range(1,len(nums)):
            prefix_multi[i]*=prefix_multi[i-1]*nums[i-1]
        suffix=1
        for j in range(len(nums)-1,-1,-1):
            prefix_multi[j]*=suffix
            suffix*=nums[j]
        return prefix_multi
        