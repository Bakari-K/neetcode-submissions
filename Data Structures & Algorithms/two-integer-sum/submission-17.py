class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsDict = dict()
        for i, num in enumerate(nums):
            if num in numsDict:
                numsDict[num].append(i)
            else:
                numsDict[num] = list()
                numsDict[num].append(i)
        for num in numsDict:
            opposite = target - num
            if opposite != num and opposite in numsDict:
                return sorted([numsDict[num][0], numsDict[opposite][0]])
            elif opposite in numsDict and len(numsDict[opposite]) == 2:
                return sorted([numsDict[num][0], numsDict[num][1]])