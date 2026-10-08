class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m=len(nums1)
        n=len(nums2)
        if m>n:
            nums1,nums2=nums2,nums1
            m,n=n,m
        
        l=0
        r=m
        while l<=r:
                cut1=(l+r)//2
                cut2=(m+n+1)//2- cut1
                left1=float('-inf') if cut1==0 else nums1[cut1-1]
                right1=float('inf') if cut1==m else nums1[cut1]
                left2=float('-inf') if cut2==0 else nums2[cut2-1]
                right2=float('inf') if cut2==n else nums2[cut2]
                if left1<=right2 and left2<=right1:
                    if (m+n)%2==1:
                        return max(left1,left2)
                    else:
                        return (max(left1,left2)+min(right1,right2))/2
                elif left1>right2:
            # need to move more elements to the left of cut1
                    r=cut1-1
                else:
                    l=cut1+1

        
        
       

        

        