a=print("here in this game you have to guess a number if you guessed correct You will be rewarded ")
guessing_number=39
number_of_guess=5
while number_of_guess>=0:
    num=int(input("guess the number "))
    if num>guessing_number:
        print("Your Number is greater than expected try lesser ")
        print ("your remaining life is ",number_of_guess-1)
    elif num<guessing_number:
        print("Your Number is lesser than expected try graeater ")
        print ("your remaining life is ",number_of_guess-1)
    elif num==guessing_number:
        print("You guessed a correct number")
        print ("your remaining life is ",number_of_guess-1)
        break
    number_of_guess=number_of_guess-1

    if number_of_guess==0:
        print("Game over")
        break
