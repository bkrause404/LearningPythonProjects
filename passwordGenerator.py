import random

lowercase = ['a', 'b', 'c', 'd','e', 'f', 'g', 'h', 'i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
uppercase = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers = ['1','2','3','4','5','6','7','8','9','0']
specials = ['~','!','@','#','$','%','%', '^', '&','&','*','(',')','?','<','>','[',']']
password = ""

def weak():
	global password
	with open("EnglishWords.txt", "r") as f:
		weakWords = f.readlines()
	password = random.choice(weakWords).rstrip('\n') + random.choice(weakWords).rstrip('\n')
	return password

def medium(lowercase, numbers):
	global password
	for i in range(0,4):
		password += random.choice(lowercase).rstrip('\n') + random.choice(numbers).rstrip('\n')
	return password

def strong(lowercase, uppercase, numbers, specials):
	global password
	for j in range(0,4):
		password += random.choice(lowercase).rstrip('\n') + random.choice(uppercase).rstrip('\n') + random.choice(numbers).rstrip('\n') + random.choice(specials).rstrip('\n')
	return password

def main():
	passStrength = raw_input("What strength password would you like? (weak/medium/strong): ")
	if passStrength == 'weak':
		print "Your weak password is: ", weak()
	elif passStrength == 'medium':
		print "Your medium password is: ", medium(lowercase, numbers)
	elif passStrength == 'strong':
		print "Your strong password is: ", strong(lowercase, uppercase, numbers, specials)

if __name__ == "__main__": main()