class Solution:
    def check(self, nums: list[int]) -> bool:
        count=0
        for i in range(len(nums)):
            if nums[i]>nums[(i+1)%len(nums)]:
                count+=1
            return count<=1
nums = list(map(int, input("Enter the list of numbers: ").split()))
solution = Solution()   
print(solution.check(nums))
        
#Given an array nums, return True if the array was originally sorted in non-decreasing order and then rotated some number of positions (including 0 times). Otherwise, return False.