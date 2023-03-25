# write a python script to check whether a given pair of number are co-prime of not
print("enter two number to check co prime or not")
num1,num2=int(input()),int(input())
min= num1 if num1<num2 else num2
for i in range(2,min+1):
    if num1%i==0 and num2%i==0:
        print("%d and %d are both Coprime"%(num1,num2))
        break;
else:
    print("{} and {} are Coprime".format(num1,num2))