import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = defaultdict(int)
        for num in nums:
            frequencies[num] += 1
        frequencies = sorted(frequencies.items(), key = lambda item: item[1], reverse = True)
        solution = []
        for i in range(k):
            solution.append(frequencies[i][0])
        return solution

            
        
        