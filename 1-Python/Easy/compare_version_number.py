class CompareVersionNumber:
    # @param {string} version1
    # @param {string} version2
    # @return {integer}
    # Test on LeetCode - 56ms
    def compare_version(self, version1, version2):
        nums1 = version1.split('.')
        nums2 = version2.split('.')
        self.trim_zero(nums1)
        self.trim_zero(nums2)
        length1 = len(nums1)
        length2 = len(nums2)
        if length1 == length2:
            flag = 0
            loop = length1
        elif length1 < length2:
            flag = -1
            loop = length1
        else:
            flag = 1
            loop = length2

        for i in range(0, loop):
            v1 = int(nums1[i])
            v2 = int(nums2[i])
            if v1 < v2:
                return -1
            elif v1 > v2:
                return 1

        return flag

    def trim_zero(self, nums):
        while nums:
            num = int(nums[len(nums) - 1])
            if num == 0:
                nums.pop()
            else:
                break


def main():
    test = CompareVersionNumber()
    print test.compare_version("19.8.3.17.5.01.0.0.4.0.0.0.0.0.0.0.0.0.0.0.0.0.00.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.000000.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.000000", "19.8.3.17.5.01.0.0.4.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0000.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.000000")

if __name__ == '__main__':
    main()



