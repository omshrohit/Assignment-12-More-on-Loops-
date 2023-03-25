# write a python script to reverse a number.
num=1234
reverse=0
while(num>0):
    r=num%10
    reverse=reverse*10+r
    num//=10
print(reverse)