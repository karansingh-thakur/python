num1=int(input("enter num 1 --> "))
num2=int(input("enter num 2 --> "))
num3=int(input("enter num 3 --> "))

print("greatest of two")

if num1>num2:
	print(f"num 1 is greater {num1}")
else:print(f"num 2 is greater {num2}")

print("greatest of 3")

if num1>num2 and num1>num3:
	print(f"num 1 is greater {num1}")
elif num2>num3 and num2>num1:
	print(f"num 2 is greater {num2}")
else:print(f"num 3 is greater {num3}")