# write a python script to find next prime number of a given number
n=int(input("enter the number"))
while True:
    n+=1
    if  n>1:
        for i in   range(2,n):
            if n%i==0:
                break
        else:
            print(n)
            break
