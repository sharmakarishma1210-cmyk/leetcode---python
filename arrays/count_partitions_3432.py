
def countPartitions(nums):
	left = 0
	c = 0
	tot = sum(nums)
	for i in range(len(nums)-1):
		left += nums[i]
		right = tot - left
		d = abs(left - right)
		if d % 2 == 0:
			c+=1
	return c
nums = [10,10,3,7,6]
print(countPartitions(nums))