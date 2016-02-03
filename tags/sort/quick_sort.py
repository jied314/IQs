class Solution(object):
    def quickSort(self, array, low, high):
        if low >= high:
            return
        pivot = self.partition(array, low, high)
        self.quickSort(array, low, pivot-1)
        self.quickSort(array, pivot+1, high)

    def partition(self, array, low, high):
        pivot = array[high]
        pi = low
        for i in range(low, high):
            if array[i] < pivot:
                array[i], array[pi] = array[pi], array[i]
                pi += 1
        array[pi], array[high] = array[high], array[pi]
        return pi+1

    # Nice Quick-Sort in Python
    def quick_sort(self, nums):
        less, equal, greater = [], [], []
        if len(nums) > 1:
            pivot = nums[0]
            for num in nums:
                if num < pivot:
                    less.append(num)
                elif num == pivot:
                    equal.append(num)
                else:
                    greater.append(num)
            return self.quick_sort(less) + equal + self.quick_sort(greater)
        else:
            return nums