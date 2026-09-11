class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zerocount = 0
        for num in nums:
            if num != 0:
                product = product * num
            else:
                zerocount += 1
            if zerocount > 1:
                return [0] * len(nums)

        if zerocount == 1:
            solution = [0] * len(nums)
            for i in range(len(nums)):
                if nums[i] == 0:
                    solution[i] = product
                    return solution
        
        solution = []
        for num in nums:
            solution.append(product//num)
        return solution    
        
        