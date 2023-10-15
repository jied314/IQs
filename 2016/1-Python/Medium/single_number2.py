# 6/26, 28 - Hash, Bit Manipulation
# Given an array of integers, every element appears three times except for one. Find that single one.
# Note: Python integer range
#
class SingleNumber2:
    # @param {integer[]} nums
    # @return {integer}

    # Use Hash Table, Test on LeetCode - 68ms
    def single_number_hash(self, nums):
        values = {}
        for num in nums:
            if values.has_key(num):
                values[num] += 1
                if values[num] == 3:
                    del values[num]
            else:
                values[num] = 1
        return values.keys()[0]

    # Use Bit Manipulation, Test on LeetCode - 168ms
    def single_number_bit_negative(self, nums):
        bit_count = [0 for i in range(0, 32)]
        # count bit pattern appearances
        for num in nums:
            for i in range(31, -1, -1):
                if num != 0:
                    if num & 1:
                        bit_count[i] += num & 1
                    num >>= 1
        for i in range(0, 32):
            if bit_count[i]:
                bit_count[i] %= 3

        # Convert to negative if necessary
        flag = False
        if bit_count[0] == 1:  # negative number
            flag = True
            for i in range(0, 32):
                bit_count[i] = 1 if bit_count[i] == 0 else 0

        # binary to integer (note how to deal with negatives)
        result = 0
        for bit in bit_count:
            result <<= 1
            result |= bit
        if flag:
            result = (result + 1) * -1
        return result

    # Use Bit Manipulation, Test on LeetCode - 120ms
    def single_number_bit_revisit(self, nums):
        bit_count = [0] * 32
        for i in range(0, 32):
            for num in nums:
                bit_count[i] += (num >> i) & 1
            bit_count[i] %= 3
            
        flag = False
        if bit_count[-1] == 1:
            flag = True
            for i in range(0, 32):
                bit_count[i] = 1 - bit_count[i]
        
        result = 0
        for i in range(0, 32):
            result += bit_count[i] << i
        if flag:
            result = (result + 1) * -1
        return result
        

    # Java Version produces correct result due to integer range
    # in Python, integer have no true range, since they are only limited to available memory
    def single_number_bit_nice(self, nums):
        bit_count = [0 for i in range(0, 32)]
        result = 0
        for i in range(0, 32):
            for num in nums:
                bit_count[i] += (num >> i) & 1
            bit_count[i] %= 3
            result += ((bit_count[i] & 1) << i)
        print bit_count  # same as Java result
        return result


def main():
    test = SingleNumber2()
    # print test.single_number_bit([1, 2, 2, 1, 2, 1, 3])
    print test.single_number_bit_nice([-2, -2, 1, 1, -3, 1, -3, -3, -4, -2])


if __name__ == '__main__':
    main()