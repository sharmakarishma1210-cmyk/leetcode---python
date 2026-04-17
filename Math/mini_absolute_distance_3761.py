def minMirrorPairDistance(self, nums: List[int]) -> int:
	def reverse(x):
		return int(str(x)[::-1])
	seen = {}  
	ab = float('inf')
	for j in range(len(nums)):
		curr = nums[j]
		if curr in seen:
			i = seen[curr]
			dist = j - i
			if dist < ab:
				ab = dist
		rev = reverse(curr)
		seen[rev] = j

	if ab == float('inf'):
		return -1
	else:
		return ab


# Example 1:

# Input: nums = [12,21,45,33,54]

# Output: 1

# Explanation:

# The mirror pairs are:

# (0, 1) since reverse(nums[0]) = reverse(12) = 21 = nums[1], giving an absolute distance abs(0 - 1) = 1.
# (2, 4) since reverse(nums[2]) = reverse(45) = 54 = nums[4], giving an absolute distance abs(2 - 4) = 2.
# The minimum absolute distance among all pairs is 1.