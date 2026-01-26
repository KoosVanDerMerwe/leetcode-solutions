class Solution(object):
    def minStartValue(self, nums):
        current_sum = 0
        min_sum = 0
        
        for num in nums:
                current_sum += num

                if current_sum < min_sum:
                        min_sum = current_sum
                
        return 1 - min_sum
        
            
            
        