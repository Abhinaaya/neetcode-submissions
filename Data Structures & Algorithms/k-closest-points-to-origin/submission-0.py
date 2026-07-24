class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap=[]
        ans=[]
        for pair in points:
            x=pair[0]
            y=pair[1]
            dist=x*x+y*y
            heapq.heappush(heap,(-dist,[x,y]))
            if k<len(heap):
                heapq.heappop(heap)
        while heap:
            dist,coord = heapq.heappop(heap)
            ans.append(coord)
        return ans

        
        