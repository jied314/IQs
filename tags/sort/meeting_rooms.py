# 1/27 - Sort, Greedy, Heap
# Given an array of pairs where each pair contains the start and end time of a meeting (as in int),
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
import heapq


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
    #   sort by the starting time, then record each meeting room by its finishing time
    #   for each new interval, if its start time < any meeting room's end time, add a new room;
    #   else, update the meeting room's end time
    # Proof:
    #   the min room should be the max rooms needed for the durations of all meetings. keep track of
    # all rooms needed at each time, the max is the result.
    # Complexity: O(N*N)
    def min_rooms_greedy(self, meetings):
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

    # similar idea, but use tree to expedite searching for the right finishing-time meeting room
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

    # similar idea, but use heap to store meeting rooms (end time)
    # can be viewed as a variant of tree solution
    def min_rooms_heap(self, meetings):
        if meetings is None or len(meetings) == 0:
            return 0
        # sort by starting time
        sorted_meetings = sorted(meetings, key=lambda meeting: meeting[0])

        # use a min heap to track the minimum end time of merged intervals
        heap = Heap()
        heap.push(sorted_meetings[0])

        for i in range(1, len(meetings)):
            next_meeting = sorted_meetings[i]
            min_room = heap.pop()
            if next_meeting[0] >= min_room[1]:  # update end time
                min_room[1] = next_meeting[1]
            else:  # add a new meeting room
                heap.push(next_meeting)
            heap.push(min_room)
        return heap.size()

    def min_rooms_fast(self, meetings):
        starts = sorted(i[0] for i in meetings)
        ends = sorted(i[1] for i in meetings)

        e = 0
        numRooms = available = 0
        for start in starts:
            while ends[e] <= start:
                available += 1
                e += 1
            if available:
                available -= 1
            else:
                numRooms += 1

        return numRooms

class Node(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.left = None
        self.right = None


class Heap(object):
    def __init__(self):
        self._data = []

    def push(self, item):
        heapq.heappush(self._data, (item[1], item))

    def pop(self):
        return heapq.heappop(self._data)[1]

    def poll(self):
        return heapq[0][1]

    def size(self):
        return len(self._data)


test = Solution()
print test.attend_all([[1,4], [4,5], [3,4], [2,3]])
print test.min_rooms([[1,4], [4,5], [3,4], [2,3]])
print test.min_rooms_nice([[1,4], [4,5], [3,4], [2,3]])
print test.min_rooms_tree([[1,4], [4,5], [3,4], [2,3]])
print test.min_rooms_heap([[1,4], [4,5], [3,4], [2,3]])
print test.min_rooms_fast([[1,4], [4,5], [3,4], [2,3]])
