class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq_map={}
        count=0
        req=None
        
        for num in nums:
            if count==0 :
                req=num
            count+=1 if req==num else -1
        return req
