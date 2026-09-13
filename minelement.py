def find_min_rotated_array(nums: list[int]) -> int:
    left, right = 0, len(nums) - 1 
    # If the array is not rotated at all
    if nums[left] <= nums[right]:
        return nums[left]   
    while left <= right:
        mid = (left + right) // 2 
        # Check if mid+1 is the minimum element
        if mid < right and nums[mid] > nums[mid + 1]:
            return nums[mid + 1]        
        # Check if mid itself is the minimum element
        if mid > left and nums[mid - 1] > nums[mid]:
            return nums[mid]        
        # Decide whether to go left or right
        if nums[mid] >= nums[left]:
            left = mid + 1  # Minimum is in the right half
        else:
            right = mid - 1 # Minimum is in the left half           
    return nums[0]
# Example Usage:
# nums = [4, 5, 6, 7, 0, 1, 2]
# Output: 0
