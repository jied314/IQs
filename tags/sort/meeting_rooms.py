# 1/27 - Sort, Greedy
# Given a array of pairs where each pair contains the start and end time of a meeting (as in int),
# Determine if a single person can attend all the meetings
# For example:
#   Input array { pair(1,4), pair(4, 5), pair(3,4), pair(2,3) }
#   Output: false
#
# Follow up:
#   see http://www.fgdsb.com/2015/01/30/meeting-rooms/
#   Determine the minimum number of meeting rooms needed to hold all the meetings.
#   Input array { pair(1, 4), pair(2,3), pair(3,4), pair(4,5) }
#   Output: 2


class Solution(object):
    # Idea:
    #   sort, then find any overlap exist
    def attend_all(self, meetings):
        """
        :param meetings: List[List[int, int]]
        :return: Boolean
        """
        if meetings is None or len(meetings) < 2:
            return True
        sorted_meetings = sorted(meetings, key=lambda meeting: meeting[0])
        for i in range(1, len(meetings)):
            if sorted_meetings[i][0] < sorted_meetings[i-1][1]:
                return False
        return True

    # Idea:
    #   sort, then record each meeting room by its finishing time
    #   for each new interval, if its start time < any meeting room's end time, add a new room;
    #   else, update the meeting room's end time
    # Proof:
    #   the min room should be the max rooms needed for the durations of all meetings. keep track of
    # all rooms needed at each time, the max is the result.
    # Complexity: O(N*N)
    def min_rooms(self, meetings):
        """
        :param meetings: List[List[int, int]]
        :return: int
        """
        if meetings is None:
            return 0
        if len(meetings) < 2:
            return len(meetings)
        sorted_meetings = sorted(meetings, key=lambda meeting: meeting[0])
        end_meetings = []
        for i in range(0, len(meetings)):
            next_meeting = sorted_meetings[i]
            flag = True
            for j in range(0, len(end_meetings)):
                if next_meeting[0] >= end_meetings[j]:  # can use the room
                    end_meetings[j] = max(end_meetings[j], next_meeting[1])
                    flag = False
                    break
            if flag:
                end_meetings.append(next_meeting[1])
        return len(end_meetings)

    # Borrow from Yanxing
    # Idea:
    #   store all time (starting time and end time as negative), then sort.
    def min_rooms_nice(self, meetings):
        times = []
        for m in meetings:
            times.append(m[0])
            times.append(-m[1])
        st = sorted(times, cmp=self.my_cmp)
        ret, cur = 0, 0
        for t in st:
            if t >= 0:
                cur += 1
                ret = max(ret, cur)
            else:
                cur -= 1
        return ret

    def my_cmp(self, a, b):
        if abs(a) == abs(b):
            if a < b:
                ret = -1
            else:
                ret = 1
        else:
            if abs(a) < abs(b):
                ret = -1
            else:
                ret = 1
        return ret

    def min_rooms_tree(self, meetings):
        """
        :param meetings: List[List[int, int]]
        :return: int
        """

        if meetings is None:
            return 0
        if len(meetings) < 2:
            return len(meetings)
        self.min_room = 1
        sorted_meetings = sorted(meetings, key=lambda meeting: meeting[0])
        root = Node(sorted_meetings[0][0], sorted_meetings[0][1])
        for i in range(1, len(meetings)):
            next_meeting = sorted_meetings[i]
            self.check_room(root, next_meeting)
        return self.min_room

    # use Tree to store meeting rooms - O(NlgN)
    def check_room(self, node, meeting):
        if meeting[0] >= node.end:  # can use the room
            node.end = meeting[1]
        else:  # need a new room
            if meeting[0] < node.start:
                if node.left is None:
                    self.min_room += 1
                    node.left = Node(meeting[0], meeting[1])
                else:
                    self.check_room(node.left, meeting)
            else:
                if node.right is None:
                    self.min_room += 1
                    node.right = Node(meeting[0], meeting[1])
                else:
                    self.check_room(node.right, meeting)



class Node(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.left = None
        self.right = None

test = Solution()
print test.attend_all([[1,4], [4,5], [3,4], [2,3]])
print test.min_rooms([[1,4], [4,5], [3,4], [2,3]])
print test.min_rooms_nice([[1,4], [4,5], [3,4], [2,3]])
print test.min_rooms_tree([[1,4], [4,5], [3,4], [2,3]])
