# write a python script to print all  prime numbers unser 100

for number in range(2,100+1):
    for e  in range(2,number):
        if number%e==0:
            break
    else:
        print(number,end=',')