class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l=1
        r=max(piles)
        ans=r
        while l<=r:
            hour=0
            mid=(r+l)//2
            for pile in piles:
                hour+=(pile+mid-1)//mid
            if hour<=h:
                ans=mid
                r=mid-1
            else:
                l=mid+1
        return ans

        