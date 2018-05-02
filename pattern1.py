s=input("enter a character")
n=ord(s)
if n>64 and n<92:
	if s=='A' or s=='E' or s=='I' or s=='O' or s=='U':
		print("you entered capital vowel")
	else:
		print("you entered capital consonant")
elif n>96 and n<123:
	if s=='a' or s=='e' or s=='i' or s=='o' or s=='u':
		print("you entered small vowel")
	else:
		print("you entered small consonant")


