# Given a complete binary tree, count the number of nodes.
# Utilize the attribute of complete binary tree. Need to be efficient!
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class CountCompleteBinaryTree:
    # @param {TreeNode} root
    # @return {integer}
    # Test on LeetCode - Time Limit Exceed (TLE)
    def count_nodes(self, root):
    	count = 0
    	if root:
	    	nodes = [root]
	    	level = 1
	    	children = []
	    	flag = False
	    	while True:
	    		if level:
	    			if nodes[0].left.left is not None:
	    				level += 1
	    				for node in nodes:
	    					children.append(node.left)
	    					children. append(node.right)
	    			node = level.pop(0)
	    			count += 1
	    			if node.left is not None:
	    				children.append(node.left)
	    				if node.right is not None:
	    					children.append(node.right)
	    				else:
	    					flag = True
	    			else:
	    				flag = True
	    		if flag:
	    			count += len(children)
	    			break
	    		else:
	    			level = children
	    			children = []
    	return count


    def left_height(self, root):
    	hl = 1
    	node = root
    	while node.left is not None:
    		hl += 1
    		node = node.left
    	return hl

    def right_height(self, root):
    	hr = 1  
    	node = root  	
    	while node.right is not None:
    		hr += 1
    		node = node.right
    	return hr

    # # Test on LeetCode - Time Limit Exceed (TLE)
    def count_nodes_second(self, root):
    	if root is None:
    		return 0
    	hl = self.left_height(root)
    	hr = self.right_height(root)
    	if hl == hr:
    		return (2 ** hl) - 1
    	else:
    		count = (2 ** hr) - 1
    		nodes = [root]
    		children = []
    		for i in range(0, hr - 1):
    			for node in nodes:
    				children.append(node.left)
    				children.append(node.right)
    			nodes = children
    			children = []
    		for i in range(0, len(nodes)):
    			node = nodes[i]
    			if node.left is None:
    				return count + 2 ** i
    			if node.right is None:
    				return count + 2 ** i + 1

    # Test on LeetCode - 324ms, Time - O(lgn * lgn)
    def count_nodes_efficient(self, root):
        if root is None:
            return 0
        hl = self.height(root.left)
        hr = self.height(root.right)
        if hl == hr:  # the last node on the right subtree
            return 2 ** hl + self.count_nodes_efficient(root.right)
        else:  # the last node on the left subtree
            return 2 ** hr + self.count_nodes_efficient(root.left) 

    def height(self, node):
        height = 0
        while node:
            height += 1
            node = node.left
        return height

    # Test on LeetCode - 328ms
    def count_nodes_iterative(self, root):
        if root is None:
            return 0
        count = 0
        while root:
            hl = self.height(root.left)
            hr = self.height(root.right)
            if hl == hr:
                count += 2 ** hl
                root = root.right
            else:
                count += 2 ** hr
                root = root.left
        return count
   	 

def main():
	test = CountCompleteBinaryTree()
	one = TreeNode(1)
	two = TreeNode(2)
	three = TreeNode(3)
	four = TreeNode(4)
	five = TreeNode(5)
	six = TreeNode(6)
	one.left = two
	one.right = three
	two.left = four
	two.right = five
	#three.left = six
	print test.count_nodes_iterative(one)


if __name__ == '__main__':
	main()
