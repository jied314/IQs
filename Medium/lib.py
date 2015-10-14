# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# read tree's serialized interpretation
def read_tree(array):
    root = TreeNode(array[0])
    parents = [root]
    index, length = 1, len(array)
    while index < length:
        children = []
        for node in parents:
            if index < length:
                if node is not None:  # if none, no children
                    left = array[index]
                    if left is not None:
                        left = TreeNode(left)
                    node.left = left
                    index += 1
                    children.append(node.left)
                    if index < length:
                        right = array[index]
                        if right is not None:
                            right = TreeNode(right)
                        node.right = right
                        index += 1
                    else:
                        break
                    children.append(node.right)
            else:
                break
            parents = children

    # tree = []
    # dfs(root, tree)
    # print tree
    return root


# DFS the tree
def dfs(root, result):
    node = root
    if node is not None:
        dfs(node.left, result)
        result.append(node.val)
        dfs(node.right, result)


def main():
    a1 = [1,-2,-3,1,3,-2,None,-1]
    r1 = read_tree(a1)


if __name__ == '__main__':
    main()
