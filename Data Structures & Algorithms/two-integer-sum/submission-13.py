class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsDict = dict()
        for i, num in enumerate(nums):
            if num in numsDict:
                numsDict[num].append(i)
            else:
                numsDict[num] = list()
                numsDict[num].append(i)
        print(numsDict)
        nums.sort()
        idx1 = 0
        idx2 = 1
        while idx1 < len(nums)-1:
            while idx2 < len(nums):
                if nums[idx1] + nums[idx2] == target:
                    if nums[idx1] != nums[idx2]:
                        return sorted([numsDict[nums[idx1]][0], numsDict[nums[idx2]][0]])
                    else:
                        return sorted([numsDict[nums[idx1]][0], numsDict[nums[idx2]][1]])
                elif nums[idx1] + nums[idx2] < target:
                    idx2 += 1
                else:
                    break
            idx1 += 1
            idx2 = idx1 + 1

        