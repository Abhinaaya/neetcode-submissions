class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        st=set(nums)
        longest=0
        for x in st:
            if x-1 not in st:
                length=1
                while x+length in st:
                    length+=1
                longest=max(longest,length)
        return longest






        


        