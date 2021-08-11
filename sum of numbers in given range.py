start=int(input("enter the starting range -> "))
end=int(input("enter the ending value -> "))
value=0
for i in range(start,end+1):
	value=value+i
print(f"sum in the given range is {value}")
g