arr= [int(x) for x in input("Enter an array").split(",") ]
#mysolution
def movezeroes(nums):
    n=len(nums)
    for i in range(0,n):
        for j in range(i+1, n):
            if nums[i] !=0:
                i+=1
            if nums[i]==0 and nums[j]!=0:
                nums[i], nums[j]= nums[j], nums[i]
        return nums
print(movezeroes(arr))