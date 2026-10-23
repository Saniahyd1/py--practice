prices= [int(x) for x in input("enter the list:").split(',')]
def stockbuy(nums):
    max_profit=0
    min_price=float('inf')
    n=len(nums)
    for i in range(0,n):
        min_price=min(min_price,nums[i])
        max_profit=max(max_profit, nums[i]-min_price)
    return max_profit
result = stockbuy(prices)
print("result:",{result})