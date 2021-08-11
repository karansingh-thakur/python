"""method 1"""

n=int(input("enter number --> "))
n=n+1
value=0
for i in range(1,n):
	value=value+i
	# i+=i
print(f"sum of n number is -> {value}")


'''method 2'''
num=int(input("num"))
sum = (num * (num+1))/2
print(f"sum is {sum}")
