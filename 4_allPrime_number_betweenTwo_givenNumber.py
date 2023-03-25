# write a python  script to print all  prime numbers between two  given   numbers(both value inclusive)
print("enter two number in between you want to access all prime  numbers")
num1,num2=int(input()),int(input())
max= num1 if num1>num2 else num2
min=num1 if  num1<num2 else num2
print("---prime numbers are---")
for number in range(min,max+1):
    if number>1:
        for   e in range(2,number):
            if number%e==0:
                break
        else:
            print(number)