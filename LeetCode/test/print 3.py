from typing import List
#import typing

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in nums:
            for j in nums:
                if nums.index(i)!=nums.index(j):
                    if i+j == target:
                        return [nums.index(i),nums.index(j)]
                
a = [2,7,11,15]
b = 9
s = Solution()
print('un')
print(s.twoSum(a, b))

a = [3,2,4]
b = 6
print('deux')
print(s.twoSum(a, b))

a = [3,3]
b = 6
print('trois')
print(s.twoSum(a, b))