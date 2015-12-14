# HashTable, Math - Happy Number
#
class HappyNumber:
    # @param {integer} n
    # @return {boolean}
    # Test on LeetCode - 68ms
    def is_happy_iterative(self, n):
        not_happy_set = set()
        if n == 0:
            return False
        if n < 0:
            n *= -1
        while True:
            digits = []
            while n > 0:
                digits.append(n % 10)
                n /= 10
            digits.sort()
            number = 0
            result = 0
            for digit in digits:
                result += digit * digit
                number = number * 10 + digit
            if result == 1:
                return True
            if number in not_happy_set:
                break
            not_happy_set.add(number)
            n = result
        return False

    # Test on LeetCode - 72ms
    def is_happy_recursive(self, n):
        if n == 0:
            return False
        if n < 0:
            n *= -1
        not_happy_set = set()
        return self.is_happy(n, not_happy_set)

    def is_happy(self, n, not_happy_set):
        digits = self.get_digits(n)
        number = 0
        result = 0
        for digit in digits:
            result += digit * digit
            number = number * 10 + digit
        if result == 1:
            return True
        if number in not_happy_set:
            return False
        not_happy_set.add(number)
        return self.is_happy(result, not_happy_set)

    def get_digits(self, n):
        digits = []
        while n > 0:
            digits.append(n % 10)
            n /= 10
        digits.sort()
        return digits

def main():
    test = HappyNumber()
    print test.is_happy_iterative(58)
    print test.is_happy_recursive(-19)

if __name__ == '__main__':
    main()