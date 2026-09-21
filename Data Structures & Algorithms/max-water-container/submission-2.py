class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area=0
        max_area=0
        l=0
        r=len(heights)-1
        while l<r :
            le=min(heights[l],heights[r])
            br=r-l
            area=le*br
            max_area=max(area,max_area)
            if heights[l]<heights[r]:
                l+=1
            else:
                r-=1
        return max_area

        