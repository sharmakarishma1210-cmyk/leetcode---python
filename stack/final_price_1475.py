
def finalPrices(prices):
	new = []
	for i in range(len(prices)):
		dis = 0
		for j in range(i+1 , len(prices)):
			if prices[j] <= prices[i]:
				dis = prices[j]
				break
		new.append(prices[i] - dis)
	return new
prices = [8,4,6,2,3]
print(finalPrices(prices))
# output: [4,2,4,2,3]