print("******Python Calculator******")

num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
print("select the option")

print("1. Addition\n" 
      "2. Subtraction\n"
      "3. Multiplication\n" 
      "4. Division\n"
      "5. Modulus\n"
      "6. Exponentiation\n"
      "7. Floor Division\n"
      "8. Average\n"
      "9. Exit")
option= int(input("enter the option:"))
if option ==1:
    print("Addition of 2 numbers is:",num1+num2)
elif option ==2:
    print("Subtraction is: ",num1-num2)
elif option ==3:
    print("multiplication of 2 numbers is:",num1*num2)
elif option==4:
    print("division is:",num1/num2)
elif option==5:
    print("modulus is:",num1%num2)
elif option==6:
    print("exponentiation is:",num1**num2)
elif option==7:
    print("floor division is:",num1//num2)
elif option==8:
    print("average is:",(num1+num2)/2)
elif option==9:
    print("Exiting...")
else:
    print("Invalid option")