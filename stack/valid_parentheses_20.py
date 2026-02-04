
def isValid(s):
	stack = []
	open = {'(','{','['}
	match = {')':'(','}':'{',']':'['}

	for char in s:
		if char in open:
			stack.append(char)
		else:
			if not stack or stack[-1] != match.get(char):
				return False
			stack.pop()
	return not stack
s = "()[]{}"
print(isValid(s))




        