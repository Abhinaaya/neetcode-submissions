class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq_map={}
        
        for i in nums:
            freq_map[i]=freq_map.get(i,0)+1

        for key, value in freq_map.items():
            if value>len(nums)//2:
                return key
        