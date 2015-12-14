# HashTable - Isomorphic Strings
class IsomorphicString:
    # @param {string} s
    # @param {string} t
    # @return {boolean}
    # Test on LeetCode - 96ms
    def isIsomorphic_one_map(self, s, t):
    	shape1 = self.getShape(s)
    	shape2 = self.getShape(t)
    	return shape1 == shape2
    	

    def getShape(self, s):
    	count = 0
    	dict = {}
    	shape = []
    	for i in range(0, len(s)):
    		c = s[i]
    		if dict.has_key(c):
    			index = dict[c]
    		else:
    			count += 1
    			dict[c] = count
    			index = count
    		shape.append(index)
    	print shape
    	return shape

    # Test on LeetCode - 96ms
    def isIsomorphic_two_maps(self, s, t):
        dict1, dict2 = {}, {}
        for i in range(0, len(s)):
            c1 = s[i]
            c2 = t[i]
            if dict1.has_key(c1) and dict2.has_key(c2):
                if not dict1[c1] == dict2[c2]:
                    return False
            elif not dict1.has_key(c1) and not dict2.has_key(c2):
                dict1[c1] = i
                dict2[c2] = i
            else:
                return False
        return True


def main():
	test = IsomorphicString()
	print test.isIsomorphic_two_maps('aab', 'aaa')

if __name__ == '__main__':
	main()

