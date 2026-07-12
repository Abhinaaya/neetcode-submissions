class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        mp={}
        for i in range(len(numbers)):
            need=target-numbers[i]
            if need in mp:
                return [mp[need]+1,i+1]
            mp[numbers[i]]=i

        