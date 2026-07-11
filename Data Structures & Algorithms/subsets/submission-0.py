class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        def s_s(i,new_arr):
            if i==len(nums):
                
                res.append(new_arr)
                return 
            
            s_s(i+1,new_arr+[nums[i]])
            s_s(i+1,new_arr)

        s_s(0,[])

        return res
        