class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = set()
        for i in range(len(nums)):
            inset = set()
            for j in range(i+1, len(nums)):
                numsk =  0 - nums[i] - nums[j]
                if numsk in inset:
                    combo = tuple(sorted([nums[i], nums[j], numsk]))
                    output.add(combo)
                inset.add(nums[j])
        output2 = list()
        for combo in output:
            output2.append(list(combo))
        return output2