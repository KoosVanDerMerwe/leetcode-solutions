class Solution(object):
    def romanToInt(self, s):
        values = {
            "I": 1, "V": 5, "X": 10,
            "L": 50, "C": 100, "D": 500, "M": 1000
        }

        total = 0
        i = 0

        while i < len(s):
            current = values[s[i]]

            if i + 1 < len(s):
                next_val = values[s[i + 1]]
                if current < next_val:
                    total += (next_val - current)
                    i += 2
                    continue

            total += current
            i += 1

        return total
