# year=int(input("enter year to know it is leap or not -> "))
# if year%4==0:
# 	if year%100==0:
# 		if year%400==0:
# 			print("True")
# 		else:
# 			print("False")
# 	else:
# 		print("True")
# else:
# 	print("False")

def is_leap(input_year):
    leap=False
    if (input_year % 4) == 0:
        if (input_year % 100) == 0:
            if (input_year % 400) == 0:
                return True
            else:return False
        else:return True
    else:return False

year = int(input())
print(is_leap(year))