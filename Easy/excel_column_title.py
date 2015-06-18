class ExcelColumnTitle:
    # @param {integer} n
    # @return {string}
    # Test on LeetCode - 43ms
    def convert_to_title(self, n):
        base = ord('A') - 1
        result = []
        while n > 0:
            module = n % 26
            if module == 0:
                module = 26
            result.insert(0, chr(base + module))
            n /= 26
            if module == 26:
                n -= 1
        return ''.join(result)

    # Test on LeetCode - 48ms
    def convert_to_title_concise(self, n):
        """trick to handle corner case of 26"""
        base = ord('A')
        result = []
        while n > 0:
            result.insert(0, chr(base + ((n - 1) % 26)))
            n = (n - 1) / 26
        return ''.join(result)


def main():
    test = ExcelColumnTitle()
    print test.convert_to_title(52)
    print test.convert_to_title_concise(52)

if __name__ == '__main__':
    main()