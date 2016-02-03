# 12/2 - Sort
# Given a list of non negative integers, arrange them such that they form the largest number.
# For example, given [3, 30, 34, 5, 9], the largest formed number is 9534330.
# Note: The result may be very large, so you need to return a string instead of an integer.
# Idea:
#   Sort all numbers based on the custom sorting function (to make the final number large)
#
class LargestNumber(object):
    # Test on LeetCode - 100ms (11.87%)
    def largest_number(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        if nums is None or len(nums) == 0:
            return ""
        length = len(nums)
        if length == 1:
            return str(nums[0])
        # reorder numbers and store in ret
        ret = [nums[0]]
        for i in range(1, length):
            num = nums[i]
            ret.insert(self.custom_bs(num, ret), num)

        is_zero = True
        for i in range(0, length):
            digit = ret[i]
            if digit != 0:
                is_zero = False
            ret[i] = str(digit)
        if is_zero:
            return "0"
        return "".join(ret)

    # find the insert position for key in array
    # note the array is in descending order
    def custom_bs(self, key, array):
        low, high = 0, len(array) - 1
        while low <= high:
            mid = low + (high - low) / 2
            compare_ret = self.custom_compare(key, array[mid])
            if compare_ret == -1:  # key < array[mid]
                low = mid + 1
            elif compare_ret == 1:  # key > array[mid]
                high = mid - 1
            else:  # key == array[mid]
                return mid
        return low

    # Compare n1 and n2 to make the final concatenation large
    # e.g. 56, 566 -> 566|56, 54, 544 -> 54|544
    # The comparison does the most l1 + l2 times.
    def custom_compare(self, n1, n2):
        digits1, digits2 = self.split_digit(n1), self.split_digit(n2)
        l1, l2 = len(digits1), len(digits2)
        length = l1 + l2
        for i in range(0, length):
            digit1 = digits1[i % l1]  # if i >= l1, back the the beginning
            digit2 = digits2[i % l2]
            if digit1 < digit2:
                return -1
            elif digit1 > digit2:
                return 1
        return 0

    # Convert the integer to a list of digits
    def split_digit(self, num):
        if num == 0:
            return [0]
        ret = []
        while num > 0:
            num, digit = divmod(num, 10)
            ret.append(digit)
        ret.reverse()
        return ret

# Test on LeetCode - 56ms
# Instead of manually sorting numbers, define a comparator function and supply it to sort()
# Convert integer to string, since this is the final result. (avoid converting integers to list)
# Learn:
#   define a comparator and supply to sort()
#   string comparison in Python. e.g. '1' < '2', 'A' < 'a'
class LargestNumberBetter(object):
    def largest_number(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        if nums is None or len(nums) == 0:
            return ""
        ret = []
        for num in nums:
            ret.append(str(num))
        ret.sort(cmp=self.comparator1, reverse=True)
        largest = "".join(ret)
        if largest[0] == "0":
            largest = "0"
        return largest

    def comparator(self, s1, s2):
        l1, l2 = len(s1), len(s2)
        length = l1 + l2
        for i in range(0, length):
            digit1 = s1[i % l1]  # if i >= l1, back the the beginning
            digit2 = s2[i % l2]
            if digit1 < digit2:
                return -1
            elif digit1 > digit2:
                return 1
        return 0

    def comparator1(self, s1, s2):
        c1, c2 = s1+s2, s2+s1
        if c1 < c2:
            return -1
        elif c1 > c2:
            return 1
        else:
            return 0



def main():
    # test = LargestNumber()
    test = LargestNumberBetter()
    print test.largest_number([3, 30, 34, 5, 9])
    print test.largest_number([54, 544])
    print test.largest_number([56, 566])
    print test.largest_number([1,2,3,4,5,6,7,8,9,0])
    print test.largest_number([121, 12])
    print test.largest_number([0,0])

if __name__ == '__main__':
    main()