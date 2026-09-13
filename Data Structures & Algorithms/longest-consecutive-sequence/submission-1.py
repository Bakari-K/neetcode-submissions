import heapq
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        max = 0
        for num in nums:
            if (num - 1) not in numsSet:
                sequence = 1
                curr = num + 1
                while True:
                    if curr in numsSet:
                        sequence += 1
                    else:
                        break
                    curr += 1
                if sequence > max:
                    max = sequence
        return max


        