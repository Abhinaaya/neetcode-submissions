class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n_set=set(nums)
        longest=0
        for num in n_set:
            if num-1 not in n_set:
                length=1
                while num+length in n_set:
                    length+=1
                longest=max(length,longest)
        return longest
            
        