class Solution:
    def threeSum(self, nums:list[int])->list[list[int]]:
        result= set() 

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):

                    if nums[i] + nums[k] + nums[j] == 0:
                        triplet = tuple(sorted([nums[i], nums[j], nums[k]]))
                        result.add(triplet)
        return [list(t) for t in result]

if __name__ == "__main__":
    nums = input("Enter the array elements separated by spaces: ").split()
    nums = [int(x) for x in nums if x.strip()]
    solution = Solution()
    print("Unique triplets that sum to zero:", solution.threeSum(nums))