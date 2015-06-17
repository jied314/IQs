# Bit Manipulation - Reverse Bits
# Reverse bits of a given 32 bits unsigned integer.
#
class ReverseBits:
    # @param n, an integer
    # @return an integer
    def reverse_bits_DJ(self, n):
        result = 0
        i = 0
        while i < 32:
            result = (result << 1) + n % 2
            n >>= 1
            i += 1
        return result

    # consider reversing 8 bits at a time, use cache to improve performance
    def reverse_bits_nice(self, n):
        result, i = 0, 0
        while i < 32:
            result = (result << 1) + (n & 1)
            n >>= 1
            i += 1
        return result

def main():
    test = ReverseBits()
    print test.reverse_bits_DJ(43261596)
    print test.reverse_bits_nice(43261596)

if __name__ == '__main__':
    main()
