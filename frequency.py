arr = [int(x) for x in input("Enter numbers:").split(" ")]
def frequency(nums):
    freq_map= dict()
    n = len(nums)
    for i in range(0,n):
        if nums[i] in freq_map:
            freq_map[nums[i]]+=1
        else:
            freq_map[nums[i]]=1
    return freq_map
print(frequency(arr)) 