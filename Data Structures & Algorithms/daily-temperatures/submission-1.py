class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]
        ans=[0]*len(temperatures)
        for i in range(len(temperatures)):
            while  stack and  temperatures[i]>temperatures[stack[-1]]:
                idx=stack[-1]
                ans[idx]=i-idx
                stack.pop()
            stack.append(i)
        return ans

        