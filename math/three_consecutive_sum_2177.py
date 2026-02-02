
def sumOfThree(num):
	x = int(num/3)
	a = x -1
	c = x + 1
	new = [a , x , c]
	for item in new:
		if item + 1 in new and item + 2 in new:
			if item + (item+1) + (item +2) == num:
				return new
				break
		return []
        
num = 33
print(sumOfThree(num))