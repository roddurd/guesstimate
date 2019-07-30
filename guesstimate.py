import timeit, math
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
		num1,num2 = randint(8,10000), randint(8,10000)
		return ("What is " + str(num1) + " x " + str(num2) + "?", num1*num2)
	elif difficulty == "h":
		num1,num2 = randint(101,3000000), randint(108,3000000)
		return ("What is " + str(num1) + " x " + str(num2) + "?", num1*num2)
		
def divide():
	global difficulty
	if difficulty == "e":
		num1,num2 = randint(2,100), randint(2,100)
		return ("What is " + str(num1) + " / " + str(num2) + "?", num1/num2)
	elif difficulty == "m":
		num1,num2 = randint(8,10000), randint(8,10000)
		return ("What is " + str(num1) + " / " + str(num2) + "?", num1/num2)
	elif difficulty == "h":
		num1,num2 = randint(101,3000000), randint(108,3000000)
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
		num1,num2 = randint(2,100), randint(2,100)
		return ("What is " + str(num1) + " ^ " + str(num2) + "?", num1**num2)
	elif difficulty == "m":
		num1,num2 = randint(8,10000), randint(8,10000)
		return ("What is " + str(num1) + " ^ " + str(num2) + "?", num1**num2)
	elif difficulty == "h":
		num1,num2 = randint(101,3000000), randint(108,3000000)
		return ("What is " + str(num1) + " ^ " + str(num2) + "?", num1**num2)



		
while True:
	question, answer = choice((multiply(), divide(), add(), subtract(), exponentiate()))
	guess = input(question+"\nYour answer: ")
	if guess[0].lower() == 'q':
		break
	guess = int(guess)
	score += abs(answer - guess) / 10**(math.log10(max((answer,guess)))-1)
	print("The correct answer was:", answer)
	print("You were off by ", abs(guess-answer))
	print("Score: ", score,"\n")
	


