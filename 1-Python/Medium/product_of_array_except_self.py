# 7/19 - Array
# Idea:
#   two scans: first calculate product to the left side, then to the right side

class ProductOfArrayExceptSelf:
    # @param {integer[]} nums
    # @return {integer[]}

    # Test on LeetCode - 188ms
    def product_except_self(self, nums):
        result = [1]
        for i in range(1, len(nums)):
            result.append(result[i-1] * nums[i-1])
        right = 1
        for j in range(len(nums)-1, -1, -1):
            result[j] *= right
            right *= nums[j]
        return result


def main():
    test = ProductOfArrayExceptSelf()
    print test.product_except_self([0,0])


if __name__ == '__main__':
    main()