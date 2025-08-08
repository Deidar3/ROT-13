#!/usr/bin/python3
 
import sys
 
alphabet = ["A", "a", "B", "b", "C", "c", "D", "d", "E", "e", "F", "f", "G", "g", "H", "h", "I", "i", "J", "j", "K", "k", "L", "l", "M", "m", "N", "n", "O", "o", "P", "p", "Q", "q", "R", "r", "S", "s", "T", "t", "U", "u", "V", "v", "W", "w", "X", "x", "Y", "y", "Z", "z"]
 
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
 
if len(sys.argv) > 1:
	string = ""
	for i in range (1, len(sys.argv)):
		for n in sys.argv[i]:
			if n == " ":
				string += n
			for c in numbers:
				if n == str(c):
					string += str(c)
			for v in alphabet:
				if n == v:
					if alphabet.index(v) < 26:
						string += alphabet[alphabet.index(v) + 26]
					else:
						string += alphabet[alphabet.index(v) - 26]
			if n not in str(numbers) and n not in alphabet:
				string += n
		string += " "
	print(string)
else:
	print("Usage: {0} <input>".format(sys.argv[0]))

