elements= [int(x) for x in input("Enter the numbers:").split(" ")]
def missingNumber( nums: list[int]) -> int:
    n=len(nums)
    k= n*(n+1)//2
    s=sum(nums)
    return k-s
print(missingNumber(elements))