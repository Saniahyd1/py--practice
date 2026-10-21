#common element
list1 = [int(x) for x in input("Enter numbers for list 1 (comma-separated): ").split(",")]
list2 = [int(x) for x in input("Enter numbers for list 2 (comma-separated): ").split(",")]
result = []
for item in list1:
  if item in list2:
    result.append(item)
print(result) 