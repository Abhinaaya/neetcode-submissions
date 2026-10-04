class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        st=[]
        max_area=0
        for i in range(len(heights)):
            while st and heights[i]<heights[st[-1]]:
                h=heights[st.pop()]
                if st:
                    w=i-st[-1]-1
                else:
                    w=i
                max_area=max(max_area,w*h)
            st.append(i)
        return max_area


        