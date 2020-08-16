from string import printable
import random

digit = printable.strip()
passw  = []
lenght = input("Password Lenght ")
def passwords(lenght):
	if lenght == '':
		print("no password is of 0 words")
		exit()
	elif lenght.replace(' ','').isalpha() == True:
		print("type a number")
		exit()
	else:
		for _ in range(int(lenght)):
			passw.append(random.choice(digit))
	word = ''.join(passw)
	print(word)
passwords(lenght)