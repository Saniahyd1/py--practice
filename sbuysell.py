nums=[int(x) for x in input("enter the array:").split(",")]
def stock(price):
    n = len(price)
    max_profit= 0
    min_price= float('inf')
    for i in range(0,n):  
        min_price=min(min_price, price[i])
        max_profit= max(max_profit,price[i]-min_price)
    return max_profit
result = stock(nums)
print(result)