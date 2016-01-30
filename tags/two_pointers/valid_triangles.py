# 1/28 - not in LC, Sort, Two Pointers
# Three segments of lengths A, B, C form a triangle iff
#   A + B > C
#   B + C > A
#   A + C > B
# e.g. 6, 4, 5 can form a triangle, but 10, 2, 7 cannot.
#
# Given a list of segments lengths, your algorithm should find at least one triplet of segments
# that form a triangle (if any).
# Method should return an array of either:
#   3 elements: segments that form a triangle (i.e. satisfy the condition above).
#   empty array if there are no such segments.
#
# Follow up:
#   Could you return the number of all valid triangles? You can assume there is no duplicates in the original array.
#
# Follow up:
#   Could you return all valid triangles? You can assume there is no duplicates in the original array.


class ValidTriangles(object):
    # borrow from Yanxing
    # Idea:
    #   similar to 3 Sum, first sort then two pointers
    def valid_triangle(self, nums):
        """
        :param nums: List[double]
        :return: List[double]
        """
        nums.sort()
        for i in range(0, len(nums)-2):
            for j in range(i+1, len(nums)-1):
                for k in range(j+1, len(nums)):
                    if nums[i] + nums[j] > nums[k]:
                        return [nums[i], nums[j], nums[k]]
                    else:
                        break
        return []

    # similar idea as counting valid triangles
    def valid_triangle_nice(self, nums):
        """
        :param nums: List[double]
        :return: List[double]
        """
        nums.sort()
        for i in range(0, len(nums)-2):
            k = i + 2
            for j in range(i+1, len(nums)):
                if j != k and nums[i] + nums[j] > nums[k]:
                    return [nums[i], nums[j], nums[k]]
        return []

    # return the count of valid triangles
    # Time Complexity - O(N*N)
    # Note: k is initialized outside of the second loop
    def valid_triangle_num(self, nums):
        nums.sort()
        count = 0
        for i in range(0, len(nums)-2):
            k = i + 2
            for j in range(i+1, len(nums)):
                max_allowed = nums[i] + nums[j]
                while k < len(nums) and nums[k] < max_allowed:
                    k += 1
                count += k - j - 1
        return count

    # return all valid triangles
    def valid_triangles(self, nums):
        ret = []
        nums.sort()
        for i in range(0, len(nums)-2):
            k = i + 2
            for j in range(i+1, len(nums)):
                max_allowed = nums[i] + nums[j]
                while k < len(nums) and nums[k] < max_allowed:
                    k += 1
                for c in range(1, k-j):
                    ret.append([nums[i], nums[j], nums[c+j]])
        return ret