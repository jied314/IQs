# 10/19 - Backtracking, String
# Given a digit string, return all possible letter combinations that the number could represent.
# A mapping of digit to letters (just like on the telephone buttons) is given below.
# Input:Digit string "23"
# Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].


class LetterCombinationsOfAPhoneNumber(object):

    # Test on LeetCode - 48ms
    # DFS, or Backtracking
    # Idea:
    #   recursively visit each digit, add the letter when visiting the digit, remove letter after visiting the digit.
    #   avoid copying string multiple times by using prefix = prefix[:-1] which producing a new string
    # Note:
    #   special cases when the digit has no corresponding letters.
    def letter_combinations_recursive(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits is None or len(digits) < 1:
            return []
        combinations = []
        digit_letter_map = {"0": [" "], "1": [], "2": ["a", "b", "c"], "3": ["d", "e", "f"], "4": ["g", "h", "i"],
                            "5": ["j", "k", "l"], "6": ["m", "n", "o"], "7": ["p", "q", "r", "s"], "8": ["t", "u", "v"],
                            "9": ["w", "x", "y", "z"], "*": ["+"], "#": []}
        length = len(digits)
        self.combine(digits, 0, length, digit_letter_map, "", combinations)
        return combinations

    def combine(self, digits, visiting_index, length, digit_letter_map, prefix, combinations):
        digit = digits[visiting_index]
        letters = digit_letter_map[digit]
        if len(letters) > 0:  # has corresponding letters
            for letter in letters:
                prefix += letter
                if visiting_index == length - 1:  # if the last digit, add to combinations
                    combinations.append(prefix)
                else:  # visit the next digit
                    self.combine(digits, visiting_index+1, length, digit_letter_map, prefix, combinations)
                prefix = prefix[:-1]  # need to pop the last digit. this statement produces a new string.
        else:  # not have corresponding letters
            if visiting_index < length - 1:  # skip the current digit
                self.combine(digits, visiting_index+1, length, digit_letter_map, prefix, combinations)
            else:  # if the last digit, add to combinations
                combinations.append(prefix)

    # Test on LeetCode - 48ms
    # Idea:
    #   BFS
    #   visit each digit and record intermediate results
    def letter_combinations_iterative(self, digits):
        if digits is None or len(digits) < 1:
            return []
        combinations = []
        digit_letter_map = {"0": [" "], "1": [], "2": ["a", "b", "c"], "3": ["d", "e", "f"], "4": ["g", "h", "i"],
                            "5": ["j", "k", "l"], "6": ["m", "n", "o"], "7": ["p", "q", "r", "s"], "8": ["t", "u", "v"],
                            "9": ["w", "x", "y", "z"], "*": ["+"], "#": []}
        for digit in digits:
            temp = []
            letters = digit_letter_map[digit]
            if len(letters) > 0:  # has corresponding letters
                if len(combinations) > 0:  # not empty
                    for letter in letters:
                        for e in combinations:
                            temp.append(e + letter)
                else:  # empty, just add all letters
                    for letter in letters:
                        temp.append(letter)
                combinations = temp
        return combinations


def main():
    test = LetterCombinationsOfAPhoneNumber()
    print test.letter_combinations_recursive("258")
    print test.letter_combinations_recursive("12")
    print test.letter_combinations_recursive("21")
    print test.letter_combinations_recursive("1212")

    print test.letter_combinations_iterative("258")
    print test.letter_combinations_iterative("12")
    print test.letter_combinations_iterative("21")
    print test.letter_combinations_iterative("1212")



if __name__ == "__main__":
    main()