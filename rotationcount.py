def find_rotation_count(nums: list[int]) -> int:
    left, right = 0, len(nums) - 1
    # Case 1: Array is not rotated at all
    if nums[left] <= nums[right]:
        return 0 
    while left <= right:
        mid = (left + right) // 2  
        # Case 2: Check if mid + 1 is the minimum element
        if mid < right and nums[mid] > nums[mid + 1]:
            return mid + 1     
        # Case 3: Check if mid itself is the minimum element
        if mid > left and nums[mid - 1] > nums[mid]:
            return mid    
        # Case 4: Decide to discard left half or right half
        if nums[mid] >= nums[left]:
            left = mid + 1  # Pivot is in the right half
        else:
            right = mid - 1 # Pivot is in the left half   
    return 0
# Example Usage:
# nums = [4, 5, 6, 7, 0, 1, 2]
# Output: 4 (Array was rotated 4 times)
 