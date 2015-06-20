# Math - Palindrome Number
# Determine whether an integer is a palindrome. Do this without extra space.
# Note: 
# 	1. Negative Numbers are not considered as palindrome
# 	2. Overflow (check before happening)
class PalindromeNumber:
    # @param {integer} x
    # @return {boolean}
    # Test on LeetCode - 252ms
    def is_palindrome(self, x):
    	result = True
    	if x < 0:
    		result = False
    	if x >= 10:
    		n = x
    		m = 0
    		while n > 0:
    			digit = n % 10
    			if m > 214748364 or (m == 214748364 and digit > 7) :
    				return False
    			m = m * 10 + digit
    			n /= 10
    		result = m == x
    	return result


def main():
	test = PalindromeNumber()
	print test.is_palindrome(214744447412)

if __name__ == '__main__':
	main()
    	