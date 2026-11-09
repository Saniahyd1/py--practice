nums1= [int(x) for x in input("Enter the nums:").split(",")]
nums2= [int(x) for x in input("Enter the nums:").split(",")]
def findMedianSortedArrays(nums1: list[int], nums2: list[int]) -> float:
    n= len(nums1)
    m= len(nums2)
    result=[]
    for i in range(len(nums1)):
        result.append(nums1[i])
    for j in range(len(nums2)):
        if nums2[j] not in result:
            result.append(nums2[j])
            result.sort()
            r=len(result)
        if r % 2 == 1:
            return float(result[r // 2])
        else:
            return (result[r // 2 - 1] + result[r // 2]) / 2.0
print(findMedianSortedArrays(nums1, nums2))