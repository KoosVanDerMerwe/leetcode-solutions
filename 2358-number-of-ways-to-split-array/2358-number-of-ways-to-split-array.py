class Solution(object):
    def waysToSplitArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = sum(nums)
        left_section = 0
        ans = 0

        for i in range(len(nums)-1):
            left_section += nums[i]
            right_section = total - left_section
            if left_section >= right_section:
                ans += 1
        
        return ans

                 

        
        