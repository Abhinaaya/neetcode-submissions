class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        k=len(nums)
        ans=nums[0:k+1]+nums[0:k+1]
        return ans
        