from random import randint

Random_Number = randint(1,10)

Input_Number = input("Guess the number: ")

while (Random_Number != int(Input_Number)):
	print ("Wrong, try again!") 
	Input_Number = input("Guess the number: ")
else: 
	print ("Correct!")

