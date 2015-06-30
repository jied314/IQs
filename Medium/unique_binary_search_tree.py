class UniqueBinarySearchTree:
    # @param {integer} n
    # @return {integer}
    # Test on LeetCode - 36ms
    def num_trees(self, n):
        nums = []
        nums.append(1)
        nums.append(1)
        nums.append(2)
        for i in range(3, n + 1):
            num = 0
            for j in range(1, i + 1):
                num += nums[j - 1] * nums[i - j]
            nums.append(num)
        return nums[n]

    # Test on LeetCode - 52ms    
    def num_trees_map(self, n):
        nums = {}
        nums[0] = 1
        nums[1] = 1
        nums[2] = 2
        for i in range(3, n + 1):
            num = 0
            for j in range(1, i + 1):
                num += nums[j - 1] * nums[i - j]
            nums[i] = num
        return nums[n]

def main():
    test = UniqueBinarySearchTree()
    print test.num_trees_map(3)


if __name__ == '__main__':
    main()