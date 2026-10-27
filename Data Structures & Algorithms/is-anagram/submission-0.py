class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        counter1 = Counter(s)
        counter2 = Counter(t)
        for e in counter1:
            if counter2[e]!=counter1[e]:
                return False
        return True
