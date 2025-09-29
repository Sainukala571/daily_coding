class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        n=len(nums)
        for majority in set(nums):

            if nums.count(majority)>n//2:

                return majority
