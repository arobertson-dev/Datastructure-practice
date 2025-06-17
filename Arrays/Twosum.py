""" 
TWO SUM PROBLEM
LEVEL: EASY

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.

"""


#this import allows for type annotations, like List[int], to indicate a list of integers
from typing import List



#this solution uses a nested loop to check every pair of numbers in the list and see if they add up to the target or not, if they do
#it returns the indices of those two numbers


# O(n^2) time complexity

""" 
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]: 
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

                    
""" 
# O(n) time complexity
 
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexMap = {}
        for i in range(len(nums)):           
            targetIndex = target - nums[i]
            if targetIndex in indexMap:                                              
                return [indexMap[targetIndex], i]
            indexMap[nums[i]] = i
            
            
## if the targetIndex is in the map, return the target and its value, if not add the current value and index to the map

