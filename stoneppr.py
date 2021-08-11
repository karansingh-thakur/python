import random as rd
print("Welcome to our game Stone-Paper-Scissor ")
name=input("enter your name -> ")
print("")
c=0
W = 'win'
L = 'loose'
pscr=0
cscr=0
tie =0
i=1
for i in range(5):
	cscr += 0
	pscr += 0
	tie  +=0

	list=['stone','paper','scissor']
	choice=rd.choice(list)
	print("moves --> stone, paper, scissor ")
	inp=input("enter your move -> ")
	print("computer -> ",choice)
	if inp=='stone' and choice=='paper':
		print(L, "\n")
		# print("computer score -> ")
		cscr=cscr + 1
		# print(cscr, "\n")
	elif inp=='paper' and choice=='scissor':
		print(L, "\n")
		# print("computer score -> ")
		cscr=cscr + 1
		# print(cscr, "\n")
	elif inp=='scissor' and choice=='stone':
		print(L, "\n")
		# print("computer score -> ")
		cscr=cscr + 1
		# print(cscr, "\n")
	elif inp=='paper' and choice=='stone':
		print(W, "\n")
		# print("your score -> ")
		pscr=pscr + 1
		# print(pscr, "\n")
	elif inp=='scissor' and choice=='paper':
		print(W, "\n")
		# print("your score -> ")
		pscr=pscr + 1
		# print(pscr, "\n")
	elif inp=='stone' and choice=='scissor':
		print(W, "\n")
		# print("your score -> ")
		pscr=pscr + 1
		# print(pscr, "\n")
	elif inp==choice:
		print("its same play again\n")
		tie=tie+1

	else: print("wrong input do it again")
f=f"{name} won with score of {pscr}:{cscr} tie {tie} times"
z=f"computor won with score of {cscr}:{pscr} tie {tie} times"
t=f"match is tie with score of {name} {pscr}:{cscr} computer"
if pscr>cscr:
	print(f)
elif pscr==cscr:
	print(t)
else:print(z)