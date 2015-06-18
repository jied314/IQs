# Math - Excel Sheet Column Number
# 6/17
class ExcelColumnNumber:
    # @param {string} s
    # @return {integer}
    # Test on LeetCode 76ms
    def title_to_number(self, s):
        result = 0
        for i in range(0, len(s)):
            result = result * 26 + ord(s[i]) - ord('A') + 1
        return result

def main():
    test = ExcelColumnNumber()
    print test.title_to_number('BA')

if __name__ == '__main__':
    main()