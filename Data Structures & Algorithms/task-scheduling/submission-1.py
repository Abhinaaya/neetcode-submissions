class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq={}
        for apl in tasks:
            if apl in freq:
                freq[apl]+=1
            else:
                freq[apl]=1
        max_count=0
        max_freq=0
        for count in freq.values():
            max_freq=max(count,max_freq)
        for count in freq.values():
            if count==max_freq:
                max_count+=1
        return max(len(tasks),(max_freq-1)*(n+1)+max_count)
        