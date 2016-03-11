def getHammingDistance(str1, str2):
	# the Hamming Distance of those two strings are the number of inversions per
	# character need to transform str1 to str2 or vise-versa.
	hammingDistance = 0

	if len(str1) != len(str2):
		return ("Error! Strings are not equal.")
	if len(str1) <= 0:
		return ("Invalid input.")

	for i in range(0, len(str1)):
		if str1[i] != str2[i]:
			hammingDistance += 1

	return hammingDistance


def countSubstrPattern(original, pattern):
	#  count the number of occurrence of pattern in original
	occurrence = 0;

	for i in range(0, len(original)):
		if original[i:i + len(pattern)] == pattern:
			occurrence += 1

	return occurrence


def isValidString(str1, alphabet):
	# function returns true if the string str is a valid string 
	# based on the letters of alphabet.

	for i in range(0, len(str1)):
		if str1[i] not in alphabet:
			return False

	return True

def getSkew(str1, n):
	# returns the number of Gs minus the number of Cs in the first n nucleotides
	skew = 0

	if len(str1) < n or len(str1) <= 0:
		return ("Invalid input.")

	for i in range(0, n):
		if str1[i] == "G":
			skew += 1
		elif str1[i] == "C":
			skew -= 1

	return skew

def getMaxSkewN(str1, n):
	# returns the maximum value of the number of Gs minus the 
	# number of Cs in the first n nucleotides
	maxSkew = 0

	if len(str1) < n or len(str1) <= 0:
		return ("Invalid input.")

	for i in range(1, n+1):
		if maxSkew < getSkew(str1, i):
			maxSkew = getSkew(str1, i)

	return maxSkew


def getMinSkewN(str1, n):
	# returns the minimum value of the number of Gs minus
	# the number of Cs in the first n nucleotides
	minSkew = len(str1)

	if len(str1) < n or len(str1) <= 0:
		return ("Invalid input.")

	for i in range(1, n+1):
		if minSkew > getSkew(str1, i):
			minSkew = getSkew(str1, i)

	return minSkew