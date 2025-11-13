'''
https://leetcode.com/problems/next-permutation/description/

This is a trick question where we find next lexicographically greater permutation.

We solve it in 3 steps:

1. Move from right to left and find the first decreasing element.

2. If element is found i.e index >=0 , again move from right to left 
   and find the first element greater than found element in step 1. 
   Swap both elements.

3. Reverse all elements to the right of the index in step 1.

Make sure to handle edge cases like when elements are equal in right to decreasing element.
If right elements are equal keep moving left.

We go from right to left till index becomes -1 in step 1
That takes care of i+1 = 0 for full array reversal if no decreasing element is found.
'''

from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        N = len(nums)
        i = N -2
        while i>=0 and nums[i] >= nums[i+1]:
            i -= 1
        
        if i>=0:
            j = N - 1
            while j > i and nums[j] <= nums[i]:
                j -= 1
            
            nums[i], nums[j] = nums[j], nums[i]

        nums[i+1 :] = reversed(nums[i+1 :])
        return nums

if __name__ == "__main__":
    sol = Solution()
    print(sol.nextPermutation([1,2,3]))  # Output: [1,3,2]
    print(sol.nextPermutation([3,2,1]))  # Output: [1,2,3]
    print(sol.nextPermutation([1,1,5]))  # Output: [1,5,1]


