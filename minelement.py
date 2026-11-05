elements= [int(x) for x in input("Enter the elements:").split(',')]

def minelements(nums):
    n=len(nums)
    left, right=0,n-1
    
    min_element=float('inf')
    while left<=right:
        min_element=min(min_element, nums[left], nums[right])
        left+=1
        right-=1
    return min_element


print(minelements(elements)) 