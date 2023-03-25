# write a python script to print first N prime numbers
n=int(input("enter how many prime   number you want to print"))
p=2
while(n>0):
    for i in range(2,p):
            if p%i==0:
                  break
    else:
          print(p)
         
          n-=1
    p+=1
    
