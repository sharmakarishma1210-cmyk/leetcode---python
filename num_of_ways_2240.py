
# Problem: 2240. Number of Ways to Buy Pens and Pencils
# Approach: Iterate over possible pen counts and calculate remaining pencils
# Time Complexity: O(n)
# Space Complexity: O(1)

def waysToBuyPensPencils(total , cost1 , cost2):
	if total < cost1 and total < cost2:
		return 1
	ans = 0
	limit_pen = total // cost1
	for i in range(limit_pen + 1):
		remains = total - i*cost1
		pencils = remains//cost2
		ans += pencils+1
	return ans
total = 20
cost1 = 10
cost2 = 5
print(waysToBuyPensPencils(total , cost1 , cost2))