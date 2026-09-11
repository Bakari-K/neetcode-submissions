import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = defaultdict(int)
        for num in nums:
            frequencies[num] += 1
        data = [(0, 0)] * k
        for pair in frequencies.items():
            flipped_pair = (pair[1], pair[0])
            heapq.heappush(data, flipped_pair)
            heapq.heappop(data)
        solution = []
        for pair in data:
            solution.append(pair[1])
        return solution

            
        
        