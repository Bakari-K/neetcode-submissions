class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        stringdict = dict()
        for string in strs:
            sortedstring = str(sorted(string))
            if sortedstring not in stringdict:
                stringdict[sortedstring] = []
                stringdict[sortedstring].append(string)
            else:
                stringdict[sortedstring].append(string)
        output = []
        for key in stringdict:
            output.append(stringdict[key])
        return output