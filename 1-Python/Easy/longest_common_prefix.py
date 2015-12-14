# Write a function to find the longest common prefix string amongst an array of strings.
# Note - Corner Cases
#
class LongestCommonPrefix:
    # @param {string[]} strs
    # @return {string}
    # Test on LeetCode - 64ms
    def longest_common_prefix(self, strs):
    	if strs:
    		first = strs[0]
    		if len(first) > 0 and len(strs) > 1:	
		    	rest = strs[1:]
		    	for i in range(0, len(first)):
		    		for str in rest:
		    			if i >= len(str) or first[i] != str[i]:
		    				return first[:i]
	    	return first
    	else:
    		return ""


def main():
	test = LongestCommonPrefix()
	print test.longest_common_prefix(['100', '10', '1000'])
	print test.longest_common_prefix(['110'])
	print test.longest_common_prefix([])
	print test.longest_common_prefix(["","b"])
	print test.longest_common_prefix(["a","ac"])

if __name__ == '__main__':
	main()
