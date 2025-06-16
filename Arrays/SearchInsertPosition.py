""" 
Search Insert Position
Difficulty: Easy
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4
 

Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums contains distinct values sorted in ascending order.
-104 <= target <= 104

"""
##This solution uses binary search to find the index where the target should be inserted in a sorted array. 
##First, it initializes two pointers, left and right, to the start and end of the array.
##Then, it enters a loop that continues until left is greater than right.
#In each iteration, it calculates the middle index and compares the value at that index with the target.
##If the value is equal to the target, it returns the index.
##If the value is less than the target, it moves the left pointer to mid + 1.
##If the value is greater than the target, it moves the right pointer to mid - 1.
##Finally, if the target is not found, it returns the left pointer, which is the insertion point.
from typing import List
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
               left = 0
               right = len(nums) -1

               while left <= right:
                       mid = (left + right) // 2
                       if nums[mid] == target:
                           return mid
                       elif nums[mid] < target:
                           left = mid + 1
                       else:
                           right = mid - 1
               return left
                    

         

