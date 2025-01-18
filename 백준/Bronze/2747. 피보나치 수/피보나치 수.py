n = int(input()) #n번째 항

#피보나치 수열
a,b = 0,1

while n>0:
    a,b = b,a+b
    n -= 1
    
print(a)