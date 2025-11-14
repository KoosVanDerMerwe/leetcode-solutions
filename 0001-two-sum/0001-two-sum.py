class Solution(object):
    def twoSum(self, nums, target):
        seen_number = {}

        for i ,number in enumerate(nums):
            compliment = target - number
            if compliment in seen_number:
                return [seen_number[compliment], i]
            seen_number[number] = i
        