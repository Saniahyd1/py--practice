arr= [int(x) for x in input("Enter the numbers:").split(',')]
k=int(input("Enter the no. of times to rotate"))

def reverse(nums, left, right):
    
    while left<right:
        nums[left], nums[right]= nums[right], nums[left]
        left+=1
        right-=1
def rotate(nums, k):    
    n=len(arr)
    if n==0:
        return nums
    k=k%n
    reverse(nums,n-k, n-1)
    reverse(nums,0, n-k-1)
    reverse(nums, 0, n-1)
    return nums

print("Rotated array:", rotate(arr, k))