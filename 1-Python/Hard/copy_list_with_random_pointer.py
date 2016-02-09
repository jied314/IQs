# 1/16 - Hash Map, LL
# A linked list is given such that each node contains an additional random pointer which could point
# to any node in the list or null.
# Return a deep copy of the list.

# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


class Solution(object):
    # initial trial
    # use lists to store nodes, randoms and distance from node to its randoms
    # built on the condition that nodes not have distinct labels
    # TLE - but still worth trying
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if head is None:
            return head
        nodes = []  # store all nodes
        randoms = []  # store node's random
        not_visited = []
        node = head
        # init
        while node is not None:
            nodes.append(node)
            randoms.append(node.random)
        # calculate distance from node to ist random
        length = len(nodes)
        rdists = [-1] * length  # store distance from node to its random (if None, 0; elif not filled, -1; else, store distance)
        for i in range(0, length):
            if randoms[i] is None:
                rdists[i] = 0  # random is None
            else:
                not_visited.append(i)  # needs to check distance
        for i in not_visited:
            nrdm = randoms[i]
            for j in range(0, length):
                node = nodes[j]
                if node is nrdm:  # identity check
                    rdists[i] = j - i
        # deep copy
        copy_nodes = []
        for node in nodes:
            copy = RandomListNode(node.label)
            copy_nodes.append(copy)
        for i in range(0, length-1):
            cur, next = copy_nodes[i], copy_nodes[i+1]
            cur.next = next
            cur.random = copy_nodes[i+rdists[i]]
        copy_nodes[-1].random = copy_nodes[length-1+rdists[-1]]
        return copy_nodes[0]

    # Test on LC - 132ms, 40%
    # use map to store node label -> easy for lookup
    # However, on the condition that node labels are all distinct
    def copy_random_list_map(self, head):
        if head is None:
            return head

        node_dict = {}
        node = head
        while node is not None:
            node_val = node.label
            node_dict[node_val] = RandomListNode(node_val)
            node = node.next

        node = head
        while node is not None:
            next = node.next
            random = node.random
            copy_node = node_dict[node.label]
            if next is not None:
                copy_node.next = node_dict[next.label]
            if random is not None:
                copy_node.random = node_dict[random.label]
            node = node.next
        return node_dict[head.label]

    # Test on LC - 136ms, 30%
    # copy node and insert it right behind the original node
    # for each random, node.next.random = node.random.next
    # divide the node into two independent lists
    def copy_random_list_nice(self, head):
        if head is None:
            return head

        # insert copy behind the original
        node = head
        while node is not None:
            node_val = node.label
            copy = RandomListNode(node_val)
            copy.next = node.next
            node.next = copy
            node = copy.next

        # add random pointer
        node = head
        while node is not None:
            if node.random is not None:
                node.next.random = node.random.next
            node = node.next.next

        new_head = head.next
        node, copy = head, head.next
        while copy.next is not None:
            next = copy.next
            copy_next = next.next
            node.next = next
            copy.next = copy_next
            node, copy = node.next, copy.next
        node.next = None
        return new_head