class Solution(object):
    def sortedSquares(self, nums):
        n = len(nums)
        result = [0] * n
        i = 0
        j = n - 1
        
        for p in range(n - 1, -1, -1):
            if abs(nums[i]) > abs(nums[j]):
                result[p] = nums[i] * nums[i]
                i += 1
            else:
                result[p] = nums[j] * nums[j]
                j -= 1
        return result
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        