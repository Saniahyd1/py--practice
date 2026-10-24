arr= [int(x) for x in input("Enter list:").split(' ')]
def bubblesort(nums):
    n= len(nums)
    for i in range(n-2,-1,-1):
        swapped = False
        for j in range(0,n-1):
            if nums[j]>nums[j+1]:
                nums[j], nums[j+1]= nums[j+1], nums[j]
                if swapped==False: 
                    swapped = True
                
        if not swapped:
            
            break
                
    return nums, swapped

print(bubblesort(arr))