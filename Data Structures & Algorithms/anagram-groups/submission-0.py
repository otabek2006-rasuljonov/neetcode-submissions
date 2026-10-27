class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        dc = {}
        for i in range(len(strs)):
            key = tuple(sorted(strs[i]))
            if key not in dc:
                dc[key] = []
            dc[key].append(strs[i])  
        for lss in dc.keys():
            ans.append(dc[lss])
        return ans