class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj=[[] for _ in range(numCourses)]
        for u,v in prerequisites:
            adj[v].append(u)
        order=[]
        state=[0]*(numCourses)
        def dfs(node):
            if state[node]==1:
                return False
            elif state[node]==2:
                return True
            state[node]=1
            for nei in adj[node]:
                if not dfs(nei):
                    return False
            state[node]=2
            order.append(node)
            return True
        for i in range(numCourses):
            if not dfs(i):
                return []
        order.reverse()
        return order
        
        