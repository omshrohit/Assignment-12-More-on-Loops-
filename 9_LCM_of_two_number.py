# write a python script to calculate LCM of two numbers

num1=int(input("enter the first number"))
num2=int(input("enter the second number"))
max=num1 if num1>num2 else num2

for i in range(max,num1*num2+1,max):
    if i%num1==0 and i%num2==0:
        print("lcm is {}".format(i))
        break
