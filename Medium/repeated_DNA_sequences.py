# 12/2 - Hash Table, Bit Manipulation
# All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T, for example: "ACGAATTCCG".
# When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.
# Write a function to find all the 10-letter-long sequences (substrings) that occur more than once
# in a DNA molecule.
# For example,
#   Given s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT",
#   Return: ["AAAAACCCCC", "CCCCCAAAAA"].
#
class RepeatedDNASequences(object):
    # Time Limit Exceed - string search is expensive
    def find_repeated_dna_sequences_string_search(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if s is None or len(s) < 21:
            return []
        ret = []
        length = len(s)
        for i in range(0, length - 19):
            sequence = s[i: i + 10]
            if sequence not in ret and sequence in s[i+10:]:
                ret.append(sequence)
        return ret

    # store seen DNA sequence into hash. if appear again, return.
    # TLE - storing string is expensive => should be able to think of using some decoding or less memory expensive way
    def find_repeated_dna_sequences_hash(self, s):
        if s is None or len(s) < 21:
            return []
        ret = []
        seen_sequences = set()
        length = len(s)
        for i in range(0, length - 9):
            sequence = s[i: i + 10]
            if sequence in seen_sequences:
                ret.append(sequence)
            else:
                seen_sequences.add(sequence)
        return ret

    # Test on LeetCode - 444ms
    # Idea:
    #   take advantage that only 4 DNA tag - A, C, G, T
    #   represent each string using two bits and decode each 10 letter sequence into an integer
    #   "A" - 00, "C" - 01, "G" - 10, "T" - 11
    #    A  A  C  C  T  C  C  G  G  T
    #   00 00 01 01 11 01 01 10 10 11 = 00000101110101101011 (binary) = 23915 (decimal)
    # Note:
    #   if found repeated sequence, still need to check whether this sequence has already been included
    #   reason for using double_words
    def find_repeated_dna_sequences_bits(self, s):
        if s is None or len(s) < 11:
            return []
        ret = []
        single_word = set()
        double_words = set()
        decode_dict = {"A": 0, "C": 1, "G": 2, "T": 3}
        length = len(s)
        for i in range(0, length - 9):
            decoding = 0
            for j in range(i, i+10):
                decoding <<= 2
                decoding += decode_dict[s[j]]
            if decoding in single_word and decoding not in double_words:
                    double_words.add(decoding)
                    ret.append(s[i:i+10])
            else:
                single_word.add(decoding)
        return ret



def main():
    test = RepeatedDNASequences()
    print test.find_repeated_dna_sequences_hash("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT")
    print test.find_repeated_dna_sequences_bits("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT")
    print test.find_repeated_dna_sequences_bits("AAAAAAAAAAAA")

if __name__ == "__main__":
    main()