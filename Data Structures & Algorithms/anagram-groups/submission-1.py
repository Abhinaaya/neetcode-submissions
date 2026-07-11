class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        st_map={}
        for s in strs:
           k="".join(sorted(s))
           if k not in st_map:
            st_map[k]=[]
           st_map[k].append(s)
        return list(st_map.values())
        