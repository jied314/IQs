class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class RotateArray:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {void} Do not return anything, modify nums in-place instead.
    # Test on LeetCode - require in-place solution
    def rotate_list(self, nums, k):
        k %= len(nums)
        if k == 0:
            return nums
        head = Node(nums[0])
        prev = head
        for i in range(1, len(nums)):
            current = Node(nums[i])
            prev.next = current
            prev = current
        prev.next = head
        i = 0
        k = len(nums) - k
        while i < k:
            head = head.next
            i += 1
        return self.traverse(head)

    def traverse(self, head):
        node = head.next
        result = [head.val]
        while node != head:
            result.append(node.val)
            node = node.next
        return result

    # Test on LeetCode - 112ms
    def rotate_memory_1(self, nums, k):
        n = len(nums)
        k %= n
        if k == 0:
            return
        i = 0
        cycle = 0
        index = 0
        value = nums[index]
        while i < n:  # potential repeating
            index = (index + k) % n
            temp = nums[index]
            nums[index] = value
            value = temp
            if cycle == index:
                index += 1
                cycle = index
                value = nums[index]
            i += 1

    # Test on LeetCode - 96ms
    def rotate_memory_n(self, nums, k):
        n = len(nums)
        k %= n
        if k == 0:
            return
        temps = nums[k*-1:n]
        for i in range(n-1, k-1, -1):
            nums[i] = nums[i - k]
        for i in range(0, k):
            nums[i] = temps[i]

    # Test on LeetCode - 87ms
    # better performance due to not repeating
    def rotate_recursive(self, nums, k):
        n = len(nums)
        k %= n
        if k == 0:
            return
        nums.reverse()
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, n - 1)

    # reverse part (start to end) of the list
    def reverse(self, lst, start, end):
        while start < end:
            temp = lst[start]
            lst[start] = lst[end]
            lst[end] = temp
            start += 1
            end -= 1

def main():
    test = RotateArray()
    nums = [1, 2, 3, 4, 5, 6]
    test.rotate_memory_n(nums, 2)
    print nums

if __name__ == '__main__':
    main()