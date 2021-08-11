# a=20
# b=50
# c=30
# d=60
# while True:
#     num=int(input("enter number "))
#     if num>a:
#         print("this is greater number")
#     elif num==a:
#         print("this is the accurate guessing")
#     elif num<a:
#         print("this is lesser number")
#     else:
#         print("try again")

a = 63
g=10
print(" CREATED BY AMAN JAISWAL ")
print(" WELCOME !!!! TO THE GAME ....GUESS THE NUMBER ????? ")
print("guess the number which is hidden you only have 10 attempts to find it .  ")
while (g > 0):
    b = int(input())
    if b == a:
        print(" CONGRATULATION !!!!!!  YOU GUESS THE CORRECT NUMBER .")
        print(" YOU WON THE GAME ")
        break
    elif (b > a):
            print("enter the value less than earlier ")
            g=g-1
            print(" you have only ",g," attempts left  ")
    elif g==1 :
            print(" YOU LOSE THE GAME.........BETTER LUCK NEXT TIME.. CORRECT ANS. IS  63 ")
            break
    else:
            print("enter the value more than earlier ")
            g=g-1
            print(" you have only ", g, " attempts left ")