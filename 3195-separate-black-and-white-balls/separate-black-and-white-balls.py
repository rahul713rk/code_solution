class Solution:
    def minimumSteps(self, s: str) -> int:
        res = 0
        count = 0

        for i in s:
            if i == '0':
                res += count
            else:
                count += 1
        return res