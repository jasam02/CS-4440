#!/usr/bin/python3
import sys
ciphertext = sys.argv[1]

# Dictionary of English-language letter frequencies.
f = {"A": .08167, "B": .01492, "C": .02782, "D": .04253, "E": .12702, "F": .02228,
     "G": .02015, "H": .06094, "I": .06966, "J": .00153, "K": .00772, "L": .04025,
     "M": .02406, "N": .06749, "O": .07507, "P": .01929, "Q": .00095, "R": .05987,
     "S": .06327, "T": .09056, "U": .02758, "V": .00978, "W": .02360, "X": .00150,
     "Y": .01974, "Z": .00074}

# Returns index for a given letter.
def index(letter):
    return sorted(list(f.keys())).index(letter)

# Returns letter for a given index.
def letter(index):
    if index > 25: index = index-26
    return sorted(list(f.keys()))[index]

#------------------------------------------

#Gets every eihgth letter from cipher and stores it in a dictionary to get the columns
columns = {}
for c in range(8):
	for i in range(c, len(ciphertext), 8):
		if (c not in columns):
			columns[c] = ciphertext[i]
		else:
			columns[c] += ciphertext[i]

#Takes in a column and gets every possible reverse shift for the column
def getShifts(column):
	shifts = {}
	for shiftNum in range(26):
		shifted = ""
		for i in range(len(column)):
			ind = index(column[i])
			ind = ind - shiftNum
			let = letter(ind)
			shifted += let
		shifts[shiftNum] = shifted
	return shifts

#Calculates the chiSquared value for each shift in the dictionary then assigns the result to the corresponding key
def getChiSquared(shiftedStrings):
	for i in range(len(shiftedStrings)):
		cipher = shiftedStrings[i]
		chiResult = 0.0
		
		for letter, englishFreq in f.items():
			Oi = cipher.count(letter)
			Ei = englishFreq * len(cipher)
			
			if(Ei > 0):
				chiResult += ((Oi - Ei) ** 2) / Ei
		shiftedStrings[i] = chiResult
	return shiftedStrings
	
#Builds the key
key = ""
for i in range(len(columns)):
	shiftedStrings = getShifts(columns[i])
	shiftedStrings = getChiSquared(shiftedStrings)
	minValueKey = min(shiftedStrings, key=shiftedStrings.get)
	key += letter(minValueKey)
#------------------------------------------


print(key)
