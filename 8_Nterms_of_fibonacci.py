# write  a python  script to print first N terms of a fibonacci series
num=int(input("enter how many fibonacci series you want"))
a=0
b=1
print(a)
print(b)
i=3
while(i<=num):
    c=a+b
    a=b
    b=c
    print(c)
    i+=1