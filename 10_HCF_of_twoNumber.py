# write a python script to  calculate HCF of two numbers.
num1=int(input("enter the 1st number"))
num2=int(input("enter the 2nd number"))
min=num1 if num1<num2 else num2
for i in range(min,0,-1):
    if num1%i==0 and num2%i==0:
        print("HCF IS {}".format(i))
        break
