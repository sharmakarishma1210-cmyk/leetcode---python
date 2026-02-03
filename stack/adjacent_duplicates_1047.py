
def removeDuplicates(s):
	stack = []
	for char in s:
		if stack and stack[-1] == char:
			stack.pop()
		else:
			stack.append(char)
	result = ''.join(stack)
	return result
s = "abbaca"
# Output: "ca"
print(removeDuplicates(s))