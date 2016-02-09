# 12/4 - Math, String
#
class Solution(object):
    NUMBER_DICT = {1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six",
                   7: "Seven", 8: "Eight", 9: "Nine", 10: "Ten", 11: "Eleven", 12: "Twelve",
                   13: "Thirteen", 14: "Fourteen", 15: "Fifteen", 16: "Sixteen", 17: "Seventeen", 18: "Eighteen",
                   19: "Nineteen", 20: "Twenty", 30: "Thirty", 40: "Forty", 50: "Fifty", 60: "Sixty",
                   70: "Seventy", 80: "Eighty", 90: "Ninety", 0: "Zero"}

    UNIT_DICT = {0: " Hundred", 1: "", 2: " Thousand", 3: " Million", 4: " Billion"}


    def number_to_words(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return Solution.NUMBER_DICT[num]
        digits = self.number_to_digits(num)
        length = len(digits)
        times = (length - 1) / 3 + 1
        i = 1
        ret = ""
        while i <= times:
            end = length - (i-1) * 3
            start = end - 3
            if start < 0:
                start = 0
            small_number = digits[start: end]
            small_number_english = self.small_number_to_words(small_number)
            ret = small_number_english + Solution.UNIT_DICT[i] + " " + ret
            i += 1
        return ret

    # convert small numbers to english words (number < 1000)
    def small_number_to_words(self, digits):
        length = len(digits)
        ret = ""
        # Take care of hundreds
        if length == 3 and digits[0] != 0:
            ret = Solution.NUMBER_DICT[digits[0]] + Solution.UNIT_DICT[0]
        # Take care the rest
        rest_num = 0
        if length > 1:  # tens
            digit = digits[length - 2]
            rest_num = 10 * digit
            if digit > 1:
                ret += " " + Solution.NUMBER_DICT[rest_num]
                rest_num = 0
        rest_num += digits[length-1]
        if rest_num > 0:
            ret += " " + Solution.NUMBER_DICT[rest_num]
        return ret

    def number_to_digits(self, num):
        digits = []
        while num > 0:
            num, digit = divmod(num, 10)
            digits.append(digit)
        digits.reverse()
        return digits

    # 1/10 Revisit - Test on LC 52ms 69%
    # Idea:
    #   recursion
    LESS_THAN_TWENTY = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven",
                        "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
    TENS = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
    THOUSANDS = ["", "Thousand", "Million", "Billion"]

    def number_to_words_nice(self, num):
        if num == 0:
            return 'Zero'
        i = 0
        ret = []
        while num > 0:
            if num % 1000 != 0:
                ret.append(self.helper(num % 1000) + " " + self.THOUSANDS[i])
            num /= 1000
            i += 1
        ret.reverse()
        return " ".join(ret).strip()

    # recursively translate small number to string
    def helper(self, num):
        ret = []
        if num == 0:
            return ""
        elif num < 20:
            ret.append(self.LESS_THAN_TWENTY[num])
        elif num < 100:
            ret.append(self.TENS[num/10])
            ret.append(self.helper(num % 10))
        else:
            ret.append(self.LESS_THAN_TWENTY[num/100])
            ret.append("Hundred")
            ret.append(self.helper(num % 100))
        return ' '.join(ret).strip()

test = Solution()
print test.number_to_words_nice(12300120)

