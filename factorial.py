# import math
fact=1
num=int(input("enter a number whose factorial you want "))
if num==0 or num==1:
    print(1)
else:
#     num *factorial(num-1)
#     print (factorial(num))
#
# a=(math.factorial(num))
# print(a)
    for i in range(1,num+1):
        fact= fact*i
        print(fact)
        # print


num = 7
factorial = 1
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("The factorial of",num,"is",factorial)
