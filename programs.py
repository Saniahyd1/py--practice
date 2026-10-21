#common element
#list1 = [int(x) for x in input("Enter numbers for list 1 (comma-separated): ").split(",")]
#list2 = [int(x) for x in input("Enter numbers for list 2 (comma-separated): ").split(",")]
#result = []
#for item in list1:
#  if item in list2:
#    result.append(item)
#print(result) 


#NO. of vowels
text = input("enter the string:")
count=0
for ch in text:
  if ch in "aeiou":
    count += 1
print(count)