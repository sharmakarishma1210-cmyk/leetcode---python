
def alternateDigitSum(n)
	sp = 0
	nstr = str(n)
	for i in range(len(nstr)):
		if i % 2 == 0:
			sp+=int(nstr[i])
		else:
			sp-=int(nstr[i])
	return sp

n = 521
# Output: 4
print(alternateDigitSum(n))

        