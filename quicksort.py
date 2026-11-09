arr= [int(x) for x in input("Enter the numbers:").split(",")]
def partition(nums, low, high):
    i=low
    j=high
    pivot= nums[low]
    n= len(nums)
    while i<j:
        while nums[i]<=pivot and i<=high-1:
            i+=1
        while nums[j]>= pivot and j>= low+1:
            j-=1
        if i<j:
            nums[i], nums[j]= nums[j], nums[i]
    nums[j], nums[low]= nums[low], nums[j]
    return j
def quick_sort(nums, low, high):
    if low<high:
        p_ind=partition(nums, low, high)
        quick_sort(nums, low, p_ind-1)
        quick_sort(nums, p_ind+1, high)
    return nums
print(quick_sort(arr, 0, len(arr)-1))