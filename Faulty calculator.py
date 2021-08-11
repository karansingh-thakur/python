

def add(x, y):
    return (x+y)
def sub(x, y):
    return (x-y)
def mul(x, y):
    return (x*y)
def div(x, y):
    return (x/y)
while True:
    x=int(input("enter first number "))
    y=int(input("enter second number "))
    print("1 for addition\n"
      "2 for subtraction\n"
      "3 for multiplication\n"
      "4 for division\n")
    z=int(input("enter operation number"))

    """45*3=555, 56+9=77,56/6=4"""

    if x==45 and y==3 and z==3:
        print(555)
    elif x==56 and y==9 and z==1:
        print(77)
    elif x==56 and y==6 and z==4:
        print(4)

    elif z==1:
        print(add(x,y))
    elif z==2:
        print(sub(x,y))
    elif z==3:
        print(mul(x,y))
    elif z==4:
        print(div(x,y))
    else:
        print("do it again")
    # break