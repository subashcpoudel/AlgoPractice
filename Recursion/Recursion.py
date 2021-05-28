# Power and Factorial functions using recursion

#Power Function
def power(num, pwr):
    if pwr == 0:
        return 1
    else:
        return num*power(num,pwr-1)

def factorial(num):
    if num == 0:
        return 1
    else:
        return num*factorial(num-1)
    
print("{} power {} is {}".format(5,3,power(5,3)))
print("{} power {} is {}".format(1,1000,power(1,900)))
print("{} power {} is {}".format(9,12,power(9,12)))
print("{}! is {}".format(5,factorial(5)))


#A bit of Fun :D 
a=994
while(a>0):
    print("{}! is {}".format(a,factorial(a)))
    a-=1

a=994
while(a>0):
    print("{} power {} is {}".format(a,a,power(a,a)))
    a-=1
