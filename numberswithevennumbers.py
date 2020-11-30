class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        mapping = {}
        mapping[1] = 0
        for i in nums:
            temp = i
            count = 0
            while (temp >= 10):
                temp = temp/10
                count += 1
            
            if (count % 2 != 0):
                mapping[1] += 1
            
        return mapping[1]
