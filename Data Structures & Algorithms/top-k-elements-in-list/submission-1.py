class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp={}
        ans=[]
        heap=[]
        for ki in range(len(nums)):
            mp[nums[ki]]=mp.get(nums[ki],0)+1
        for i,freq in mp.items():
            heapq.heappush(heap,(-freq,i))
        for _ in range(k):
            freq,i=heapq.heappop(heap)
            ans.append(i)
        return ans



        