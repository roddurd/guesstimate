import math
from time import time
from random import randint, choice
difficulty = input("Select difficulty: (E)asy (M)edium (H)ard\n")
difficulty = difficulty[0].strip().lower()
while difficulty not in ("e", "m", "h"):
	print("Your input didn't make sense. Try again.")
	difficulty = input("Select difficulty: (E)asy (M)edium (H)ard\n")
score = 0

print("Prepare to Guesstimate!")
print("=========================")
print("enter 'quit' or 'q' at any time to quit the game")

	
def multiply():
	global difficulty
	if difficulty == "e":
		num1,num2 = randint(2,100), randint(2,100)
		return ("What is " + str(num1) + " x " + str(num2) + "?", num1*num2)
	elif difficulty == "m":
		num1,num2 = randint(8,1000), randint(8,1000)
		return ("What is " + str(num1) + " x " + str(num2) + "?", num1*num2)
	elif difficulty == "h":
		num1,num2 = randint(101,30000), randint(108,30000)
		return ("What is " + str(num1) + " x " + str(num2) + "?", num1*num2)
		
def divide():
	global difficulty
	if difficulty == "e":
		num1,num2 = randint(2,100), randint(2,100)
		return ("What is " + str(num1) + " / " + str(num2) + "?", num1/num2)
	elif difficulty == "m":
		num1,num2 = randint(8,1000), randint(8,1000)
		return ("What is " + str(num1) + " / " + str(num2) + "?", num1/num2)
	elif difficulty == "h":
		num1,num2 = randint(101,300000), randint(108,30000)
		return ("What is " + str(num1) + " / " + str(num2) + "?", num1/num2)
def add():
	global difficulty
	if difficulty == "e":
		num1,num2 = randint(2,100), randint(2,100)
		return ("What is " + str(num1) + " + " + str(num2) + "?", num1+num2)
	elif difficulty == "m":
		num1,num2 = randint(8,10000), randint(8,10000)
		return ("What is " + str(num1) + " + " + str(num2) + "?", num1+num2)
	elif difficulty == "h":
		num1,num2 = randint(101,3000000), randint(108,3000000)
		return ("What is " + str(num1) + " + " + str(num2) + "?", num1+num2)
def subtract():
	global difficulty
	if difficulty == "e":
		num1,num2 = randint(2,100), randint(2,100)
		return ("What is " + str(num1) + " - " + str(num2) + "?", num1-num2)
	elif difficulty == "m":
		num1,num2 = randint(8,10000), randint(8,10000)
		return ("What is " + str(num1) + " - " + str(num2) + "?", num1-num2)
	elif difficulty == "h":
		num1,num2 = randint(101,3000000), randint(108,3000000)
		return ("What is " + str(num1) + " - " + str(num2) + "?", num1-num2)
def exponentiate():
	global difficulty
	if difficulty == "e":
		num1,num2 = randint(2,100), randint(2,9)
		return ("What is " + str(num1) + " ^ " + str(num2) + "?", num1**num2)
	elif difficulty == "m":
		num1,num2 = randint(8,10000), randint(2,15)
		return ("What is " + str(num1) + " ^ " + str(num2) + "?", num1**num2)
	elif difficulty == "h":
		num1,num2 = randint(101,3000000), randint(8,26)
		return ("What is " + str(num1) + " ^ " + str(num2) + "?", num1**num2)



		
while True:
	question, answer = choice((multiply(), divide(), add(), subtract(), exponentiate()))
	start = time()
	guess = input(question+"\nYour answer: ")
	end = time()
	if guess[0].lower() == 'q':
		break
	while not isinstance(guess, int):
		try:
			guess = int(guess)
		except ValueError as verr:
			print("Your answer didn't make sense. Try again: ")
			guess = input()
			end = time()


	score += abs(answer - guess) / 10**(math.log10(max((abs(answer),abs(guess))))-2)
	print("The correct answer was:", answer)
	print("You were off by ", abs(guess-answer))
	print("You took: ", str(round(end-start,2)), " seconds")
	print("Score: ", round(score,2),"\n")
	


