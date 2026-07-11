class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.merge_sort(nums,0,len(nums)-1)
        return nums

    def merge_sort(self,nums,l,r):
        if l>=r:
            return
        mid=(l+r)//2
        self.merge_sort(nums,l,mid)
        self.merge_sort(nums,mid+1,r)
        self.merge(nums,l,mid,r)
    
    def merge(self,nums,l,m,r):
        left=nums[l:m+1]
        right=nums[m+1:r+1]
        i=j=0
        k=l
        while i<len(left) and j<len(right):
            if left[i]<right[j]:
                nums[k]=left[i]
                i+=1
            else:
                nums[k]=right[j]
                j+=1
            k+=1
        
        while i<len(left):
            nums[k]=left[i]
            i+=1
            k+=1
        
        while j<len(right):
            nums[k]=right[j]
            j+=1
            k+=1
            

