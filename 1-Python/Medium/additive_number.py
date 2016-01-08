# 12/1 - BackTracking
# Additive number is a string whose digits can form additive sequence.
# A valid additive sequence should contain at least three numbers. Except for the first two numbers,
# each subsequent number in the sequence must be the sum of the preceding two.
#
# For example:
# "112358" is an additive number because the digits can form an additive sequence: 1, 1, 2, 3, 5, 8.
#   1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8
# "199100199" is also an additive number, the additive sequence is: 1, 99, 100, 199.
#   1 + 99 = 100, 99 + 100 = 199
# Note: Numbers in the additive sequence cannot have leading zeros, so sequence 1, 2, 03 or 1, 02, 3 is invalid.
#
# Given a string containing only digits '0'-'9', write a function to determine if it's an additive number.
# Follow up:
#   How would you handle overflow for very large input integers?
#
# Solution:
#   Determine the first two numbers, all the other numbers are determined by the first two.
#   Use BackTracking to keep trying.
#   Use a helper function to add two string numbers
#   Avoid '0' - if num[0] == '0' and l2 > 1
#
# Note:
#   Termination Condition - max(l1, l2) * 2 < total_length or max(l1, l2) <= sum_length (length-l1-l2)
#   Use Two for loops to adjust lengths and check for termination conditions
#   Use Long can be faster than use string number addition
#
# Test on LeetCode - 52ms
class Solution(object):
    first_length, second_length = 0, 1

    def is_additive_number(self, num):
        """
        :type num: str
        :rtype: bool
        """
        if len(num) < 3:
            return False
        Solution.first_length, Solution.second_length = 0, 1
        return self.is_additive_number_helper(num)

    def is_additive_number_helper(self, num):
        if not self.adjust_lengths(num):
            return False
        s1 = 0
        l1 = Solution.first_length
        s2 = s1 + l1
        l2 = Solution.second_length
        return self.check_additive_number(s1, l1, s2, l2, num)

    # BackTracking - adjust lengths of the first two numbers
    # Need to check the first two lengths can not be too long
    def adjust_lengths(self, num):
        if Solution.first_length + Solution.second_length > len(num):
            return False
        if Solution.second_length == 1:  # should increase length
            new_length = Solution.first_length + Solution.second_length + 1
            Solution.first_length = 1
            Solution.second_length = new_length - 1
        else:  # adjust two lengths
            Solution.first_length += 1
            Solution.second_length -= 1
        if Solution.second_length > 1 and num[Solution.first_length] == '0':
            self.adjust_lengths(num)
        return True

    # recursive checking whether num[s1: s1+l1] + num[s2: s2+l2] == nums[s2+l2:...]
    # if yes, move rightward and test again; else, change l1 and l2 to try again.
    def check_additive_number(self, s1, l1, s2, l2, num):
        length = len(num)
        if max(l1, l2) > len(num) - s2 - l2:
            return self.is_additive_number_helper(num)
        num1 = num[s1: s1 + l1]
        num2 = num[s2: s2 + l2]
        sum = self.string_add(num1, num2)
        if self.string_match(sum, s2 + l2, num):
            s1, l1 = s2, l2
            s2, l2 = s2 + l2, len(sum)
            if s2 + l2 == length:
                return True
            return self.check_additive_number(s1, l1, s2, l2, num)
        return self.is_additive_number_helper(num)

    # add string numbers, return the sum in string format.
    def string_add(self, num1, num2):
        carry = 0
        ret = ""
        length1, length2 = len(num1), len(num2)
        length = max(length1, length2)
        for i in range(0, length):
            if i < length1:
                digit1 = int(num1[length1 - 1 - i])
            else:
                digit1 = 0
            if i < length2:
                digit2 = int(num2[length2 - 1 - i])
            else:
                digit2 = 0
            sum = digit1 + digit2 + carry
            carry, digit = divmod(sum, 10)
            ret = str(digit) + ret
        if carry == 1:
            ret = '1' + ret
        return ret

    def string_match(self, target, start, num):
        target_length, length = len(target), len(num)
        if start + target_length <= length:
            for i in range(0, target_length):
                if target[i] != num[start + i]:
                    return False
            return True
        return False


# Use two for loops to set requirements for l1 and l2, and adjust lengths
class AdditiveNumber(object):
    def is_additive_number(self, num):
        """
        :type num: str
        :rtype: bool
        """
        length = len(num)
        for i in range(1, length/2+1):
            j = 1
            while max(i, j) <= (length-i-j):
                if num[i] == "0" and j > 1:
                    break
                # check if meet requirements
        return False

# 1/2 - Revisit
# adjust l1 and l2, check leading zeros.
class SolutionRevisit(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        if num is None or len(num) < 3:
            return False
        length = len(num)
        max_l1_and_l2 = 2 * length / 3
        for l1 in range(1, length/2+1):
            for l2 in range(1, length/2+1):
                if l1 + l2 <= max_l1_and_l2:
                    if self.check(0, l1, l1, l1 + l2, num):
                        return True
        return False

    def check(self, s1, e1, s2, e2, num):
        str1, str2 = num[s1:e1], num[s2:e2]
        if self.check_leading_zeros(str1) or self.check_leading_zeros(str2):
            return False
        sum = self.add(str1, str2)
        s3, e3 = e2, e2 + len(sum)
        if e3 <= len(num) and num[s3:e3] == sum:
            if e3 == len(num):
                return True
            else:
                return self.check(s2, e2, s3, e3, num)
        return False

    def add(self, str1, str2):
        return str(int(str1) + int(str2))

    def check_leading_zeros(self, str):
        return str[0] == '0' and len(str) > 1

def main():
    test = Solution()
    print test.is_additive_number('112358')
    print test.is_additive_number('199100199')
    print test.is_additive_number('1203')
    print test.is_additive_number('101')
    print test.is_additive_number('100010')

if __name__ == "__main__":
    main()