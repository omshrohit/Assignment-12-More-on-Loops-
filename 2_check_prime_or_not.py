# write a python script to check wheter a given number is prime or  not
num=int(input("enter a number"))
if num==1:
    print("%d is not a prime number"%num)
elif num>1:
    for i in range(2,num):
        if num%i==0:
            print("%d is not a prime number"%num)
            break
    else:
        print("%d is prime number"%num)
else:
    print("Negative or   Zero  can't be prime")