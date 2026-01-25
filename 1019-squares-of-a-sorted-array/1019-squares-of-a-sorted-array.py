class Solution(object):
    def sortedSquares(self, nums):
        n = len(nums)
        # 1. Create a result list of the same size, filled with zeros
        result = [0] * n
        
        # 2. Place pointers at both ends
        left = 0
        right = n - 1
        
        # 3. Fill the result list starting from the back (largest squares first)
        for i in range(n - 1, -1, -1):
            left_square = nums[left] ** 2
            right_square = nums[right] ** 2
            
            if left_square > right_square:
                result[i] = left_square
                left += 1
            else:
                result[i] = right_square
                right -= 1
                
        return result