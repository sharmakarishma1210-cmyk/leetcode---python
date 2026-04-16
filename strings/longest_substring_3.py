def lengthOfLongestSubstring(s):
	max_len = 0
	left = 0
	seen = set()
	for right in range(len(s)):
		while s[right] in seen:
			seen.remove(s[left])
			left+=1
		seen.add(s[right])
		max_len = max(max_len , right - left +1)
	return max_len

# Input: 
# s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.