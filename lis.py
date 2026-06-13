# longest increasing subsequence
# Given an integer array nums, return the length of the longest strictly increasing subsequence.
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0

        dp = [1] * len(nums)

        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)


if __name__ == "__main__":
    nums = input("Enter the array elements separated by spaces: ").split()
    nums = [int(x) for x in nums if x.strip()]
    solution = Solution()
    print("Length of the longest increasing subsequence:", solution.lengthOfLIS(nums))