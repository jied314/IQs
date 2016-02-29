class ZigZag:
    # @param {string} s
    # @param {integer} numRows
    # @return {string}
    # Idea:
    #   use a list to store result
    #   convert i to the right row -> i%unit or unit - i%unit
    def convert_list(self, s, numRows):
        if numRows < 2:
            return s
        length = len(s)
        unit = numRows + numRows - 2
        result = [[] for i in range(0, numRows)]
        i = 0
        while i < length:
            row = i % unit
            if numRows <= row < unit:
                row = unit - row
            result[row].append(s[i])
            i += 1
        #print result
        return ''.join([''.join(x) for x in result])

    # Idea:
    #   traverse for each row.
    def convert_locally(self, s, numRows):
        if numRows < 2:
            return s
        length = len(s)
        unit = numRows + numRows - 2
        result = []
        for i in range(0, numRows):
            index = i
            gap = unit - index * 2
            while index < length:
                result.append(s[index])
                if i == 0 or i == numRows - 1:  # the first and last row
                    index += unit
                else:  # the middle rows
                    index += gap
                    gap = unit - gap
        return ''.join(result)

def main():
    test = ZigZag()
    print test.convert_locally("PAYPALISHIRING", 4)

if __name__ == '__main__':
    main()
