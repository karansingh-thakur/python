# def helthmonitor():
# client=int(input("Enter\n1 for karan\n2 for shivani\n3 for mummy -> "))
# action=int(input("Enter\n1 for food\n2 for exercise -> "))
# add_action=input("enter What you want to add -> ")


def getdate():
		import datetime
		return datetime.datetime.now()
def addplan():
	if client==1:
		print(action)
		if action==1:
			with open("karan_food.txt","a") as f:
				a=f.write(str([ [getdate()] ,add_action]))
				print("successful")
		elif action==2:
			with open("karan_exercise.txt","a") as f:
				a=f.write(str([getdate(),add_action]))
				print("successful")
		else:
			print("Somthing wrong")

	elif client==2:
		print(action)
		if action==1:
			with open("shivani_food.txt","a") as f:
				a=f.write(str([getdate(),add_action]))
				print("successful")
		elif action==2:
			with open("shivani_exercise.txt","a") as f:
				a=f.write(str([getdate(),add_action]))
				print("successful")
		else:
			print("something gets wrong")

	elif client==3:
		print(action)
		if action==1:
			with open("mummy_food","a") as f:
				a=f.write(str([getdate(),add_action]))
				print("successful")
		elif action==2:
			with open("mummy_exercise.txt","a") as f:
				a=f.write(str([getdate(),add_action]))
				print("successful")
	else:
		print("do it again")

def retrieve():
	if client==1:
		print(action)
		if action==1:
			with open("karan_food.txt","rt") as f:
				for i in f:
					print(i,end="")
		elif action==2:
			with open("karan_exercise.txt","rt")as f:
				for i in f:
					print(i,end="")


	if client==2:
		print(action)
		if action==1:
			with open("shivani_food.txt","rt") as f:
				for i in f:
					print(i,end="")
		elif action==2:
			with open("shivani_exercise.txt","rt")as f:
				for i in f:
					print(i,end="")


	if client==3:
		print(action)
		if action==1:
			with open("mummy_food.txt","rt") as f:
				for i in f:
					print(i,end="")
		elif action==2:
			with open("mummy_exercise.txt","rt")as f:
				for i in f:
					print(i,end="")


client=int(input("Enter\n1 for karan\n2 for shivani\n3 for mummy \n-> "))
if client in range(1,4):
	cmd=int(input("\nEnter\n1 for add\n2 for retrieve \n-> "))
	if cmd in range(1,3):
		action=int(input("\nEnter\n1 for food\n2 for exercise \n-> "))
		if cmd==1:
			if action in range(1,3):
				add_action=input("\nenter What you want to add \n-> ")
				addplan()
		elif cmd==2:
			retrieve()
else: print("Wrong input")