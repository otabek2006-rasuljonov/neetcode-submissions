class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dct = {}
        for s in nums:
            if s in dct:
                dct[s]+=1
            else:
                dct[s]=1
        sdct=dict(sorted(dct.items(), key=lambda item: item[1]))
        return list(sdct)[-k:]
        
            
