def moveZeroes(nums):
    j = 0  # position for next non-zero element
    for i in range(len(nums)):
        if nums[i] != 0:
            # swap only if needed
            if i != j:
                nums[j], nums[i] = nums[i], nums[j]
            j += 1
if __name__ == "__main__":
    nums = list(map(int, input("Enter numbers separated by space: ").split()))  
    moveZeroes(nums)
    print("Output:", nums)