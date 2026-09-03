class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sdict = dict()
        tdict = dict()
        for char in s:
            if char not in sdict:
                sdict[char] = 1
            else:
                sdict[char] = sdict[char] + 1
        for char in t:
            if char not in tdict:
                tdict[char] = 1
            else:
                tdict[char] = tdict[char] + 1
        if sdict == tdict:
            return True
        return False