# Maximum Nesting Depth of the Parentheses

def maxDepth(self, s: str) -> int:
	curr = 0
	curr_max = 0
	for ch in s:
		if ch == "(":
			curr+=1
			curr_max = max(curr_max , curr)
		if ch == ")":
			curr-=1
	return curr_max


# Example 1:

# Input: s = "(1+(2*3)+((8)/4))+1"
# Output: 3

# Explanation:
# Digit 8 is inside of 3 nested parentheses in the string.

# Example 2:
# Input: s = "(1)+((2))+(((3)))"
# Output: 3

# Explanation:
# Digit 3 is inside of 3 nested parentheses in the string.

# Example 3:
# Input: s = "()(())((()()))"
# Output: 3