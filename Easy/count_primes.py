import math

class CountPrimes:
    # @param {integer} n
    # @return {integer}
    def countPrimes(self, n):
    	if n < 4:
    		return n
        primes = [1, 2 ,3]
        for i in range(4, n + 1):
        	flag = False
        	max_prime = int(math.sqrt(i))
        	prime_candidates = [x for x in primes if x > 1 and x <= max_prime]
    		for prime in prime_candidates:
    			if i % prime == 0:
    				flag = True
    				break
    		if not flag:
    			primes.append(i)
        	#print i, primes
        return len(primes)


def main():
	test = CountPrimes()
	print test.countPrimes(499979)

if __name__ == '__main__':
	main()
