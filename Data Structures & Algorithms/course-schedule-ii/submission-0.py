from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj=[[] for _ in range(numCourses)]
        for u,v in prerequisites:
            adj[v].append(u)
        indeg=[0]*(numCourses)
        for u,v in prerequisites:
            indeg[u]+=1
        q=deque()
        for i in range(len(indeg)):
            if indeg[i]==0:
                q.append(i)
        order=[]
        while q:
            node=q.popleft()
            order.append(node)
            for nei in adj[node]:
                indeg[nei]-=1
                if indeg[nei]==0:
                    q.append(nei)
        if len(order)!=numCourses:
            return []
        return order
