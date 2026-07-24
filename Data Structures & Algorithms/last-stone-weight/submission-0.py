class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap=[]
        for num in stones:
            heapq.heappush(heap,-num)
        k=len(stones)
        while heap:
            num2=heapq.heappop(heap)
            if heap:
                num1=heapq.heappop(heap)
                if num1!=num2:
                    new_n=num2-num1
                    heapq.heappush(heap,new_n)
            else:
                return -num2
        
        if heap:
            return -heap[0]
        return 0


        