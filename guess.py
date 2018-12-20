# This is a Guess the Number game
import random
guessesTaken = 0

print('Hello! What is your name?')
myName = input()

number = random.randint(1, 20)
print('Well, ' + myName + ', I am thinking of a number between 1 and 20. Can you guess the number within 10 tries?')

for guessesTaken in range(10):
	print('Guess the number!')
	guess = input()
	guess = int(guess)

	if guess < number:
		print('That number is too low, ' + myName + '.')

	if guess > number:
		print('That number is too high, ' + myName + '.')

	if guess == number:
		break

if guess == number:
	guessesTaken = str(guessesTaken + 1)
	print('Good job, ' + myName + '! You guesses the correct number in ' + guessesTaken + ' guesses!')

if guess != number:
	number = str(number)
	print('Sorry, ' + myName + '. You did not guess my number. I was thinking of: ' + number + '.')
