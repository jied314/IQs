class PlusOne(object):
    # Test on LeetCode - 60ms
    def plus_one(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        length = len(digits)
        carry = 1
        for i in range(length-1, -1, -1):
            if carry > 0:
                if digits[i] == 9:  # need to carry
                    digits[i] = 0
                else:
                    digits[i] += 1  # no carry
                    carry = 0
        if carry == 1:
            digits.insert(0, 1)
        return digits

    # Test on LeetCode - 52ms
    # No need to loop through the array. if not 9, return.
    # Append 0 to the end - avoid array elements shifting
    def plus_one_nice(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        length = len(digits)
        carry = 1
        for i in range(length-1, -1, -1):
            if digits[i] == 9:  # need to carry
                digits[i] = 0
            else:
                digits[i] += 1  # no carry
                return digits
        digits[0] = 1
        digits.append(0)
        return digits

