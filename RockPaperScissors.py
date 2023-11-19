from random import randint

def rps_judge(p1, p2):
	"""
		0 for tie
		1 for player 1
		2 for player 2
	"""
	draw = 0
	win = 1
	lose = 2

	return [
		[draw ,lose ,win],
		[win ,draw ,lose],
		[lose ,win ,draw]
	][p1][p2]

def user_choice(s):
	match s[0].lower():
		case 'r': return 0
		case 'p': return 1
		case 's': return 2
		case _:
			raise ValueError

def result(i):
	return [
			"Tie",
			"You won",
			"You lost"
		][i]


# options=["Rock", "Paper", "Scissors"]

if __name__=="__main__":
	while True:
		c= randint(0,2)
		print("Rock, Paper, Scissors? (or quit)")
		while True:
			try:
				p1 = user_choice(input())
				break
			except ValueError:
				print("invalid choice, retry")

		print(result(rps_judge(p1, c)))

		if input("Do you want to play again. Y/N: ")[0].lower()=='n':
			break


