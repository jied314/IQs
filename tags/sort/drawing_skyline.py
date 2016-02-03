# http://www.fgdsb.com/2015/01/13/drawing-the-skyline/
#
# Idea:
#   basically, for each point, find the highest point.
# Use accumulative array - scan through the array, update height if it is greater.
# Good solution uses tree and heap.
#   http://www.shadabahmed.com/blog/2013/04/24/skyline-algorithm-a-binary-tree-approach/

class Building(object):
    def __init__(self, left, right, height):
        self.left = left
        self.right = right
        self.height = height

    def output(self):
        return [self.left, self.right, self.height]