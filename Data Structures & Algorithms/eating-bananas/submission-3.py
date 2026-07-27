class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l=1
        r=max(piles)
        ans=r
        while l<=r:
            mid=(r+l)//2
            hour=0
            for pile in piles:
                hour+=(pile+mid-1)//mid
            if hour<=h:
                ans=mid
                r=mid-1
            elif hour>h:
                l=mid+1
        return ans

        