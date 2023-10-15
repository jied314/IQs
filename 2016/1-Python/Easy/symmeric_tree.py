# 10/2 - Tree, DFS (E)
# Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

# Definition for a binary tree node.
# class TreeNode(object):
# def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Test on LeetCode - 52ms
class SymmericTree_Recursive(object):
    result = True  # if False, immediately stop comparing

def is_symmetric(self, root):
    """
        :type root: TreeNode
        :rtype: bool
        """
    SymmericTree_Recursive.result = True
    if root is None:
        return True
    self.check_symmeric(root.left, root.right)
    return SymmericTree_Recursive.result

def check_symmeric(self, node1, node2):
    if SymmericTree_Recursive.result:
        if node1 is None and node2 is None:
            return
        if node1 is None or node2 is None:
            SymmericTree_Recursive.result = False
        else:
            if node1.val == node2.val:
                self.check_symmeric(node1.left, node2.right)
                self.check_symmeric(node1.right, node2.left)
            else:
                SymmericTree_Recursive.result = False


# Test on LeetCode 136ms
class SymmericTree_Iteratve(object):
    result = True
    def is_symmeric(self, root):
        if root is None:
            return True
        candidates = [[root.left, root.right]]
        while SymmericTree_Iteratve.result and len(candidates) > 0:
            candidate = candidates.pop(0)
            node1, node2 = candidate[0], candidate[1]
            if node1 is not None or node2 is not None:
                if node1 is None or node2 is None:
                    SymmericTree_Iteratve.result = False
                    break
                else:
                    if node1.val == node2.val:
                        candidates.append([node1.left, node2.right])
                        candidates.append([node1.right, node2.left])
                    else:
                        SymmericTree_Iteratve.result = False
        return SymmericTree_Iteratve.result


