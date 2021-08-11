# L=[1,2,3,4,5,6,7,8,9,'karan',"lappy",5,66,55,2,4,99]
# B=[5,6,7,8,9,'ds','ss',5]
# L.extend(B)
# print(L)
#
# a=(1,5,7,8,9)
# print(a.index(7))

def fact(n):
	if n==0 or n==1:
		return 1
	else:

		return n*fact(n-1)

print(fact(5))