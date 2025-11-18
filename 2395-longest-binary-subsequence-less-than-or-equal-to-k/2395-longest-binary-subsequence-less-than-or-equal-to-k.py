class Solution:
    def longestSubsequence(self, s, k):
        zeros = s.count('0')
        val = 0
        power = 1
        ones_used = 0
        
        for i in range(len(s) - 1, -1, -1):
            if s[i] == '1':
                if val + power <= k:
                    val += power
                    ones_used += 1
            if power > k:
                break
            power <<= 1
        
        return zeros + ones_used
