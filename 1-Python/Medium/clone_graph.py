# 10/15 - DFS, BFS, Graph (M)
# Definition for a undirected graph node
class UndirectedGraphNode(object):
    def __init__(self, x):
        self.label = x
        self.neighbors = []

from collections import deque

class CloneGraph(object):
    # Test on LeetCode - 196ms
    # Idea:
    #   use dictionary to hold all cloned nodes
    #   cloning node one by one, remember visited and not-visited ones
    #   BFS style
    def clone_graph_bfs(self, node):
        """
        :type node: UndirectedGraphNode
        :rtype: UndirectedGraphNode
        """
        if node is None:
            return None

        node_dict = {}  # store node_label -> node pairs
        not_visit_node_ref = set()
        not_visit_node_ref.add(node)
        visited_node_labels = set()

        # keep cloning nodes until visiting all nodes
        while not_visit_node_ref:
            cur_node = not_visit_node_ref.pop()
            node_label = cur_node.label
            visited_node_labels.add(node_label)

            if node_label not in node_dict:
                node_dict[node_label] = UndirectedGraphNode(node_label)
            node_copy = node_dict[node_label]

            neighbors = cur_node.neighbors
            for neighbor in neighbors:
                neighbor_label = neighbor.label
                if neighbor_label not in node_dict:
                    node_dict[neighbor_label] = UndirectedGraphNode(neighbor_label)
                neighbor_copy = node_dict[neighbor_label]
                node_copy.neighbors.append(neighbor_copy)
                if neighbor_label not in visited_node_labels:
                    not_visit_node_ref.add(neighbor)
        return node_dict[node.label]

    # 1/1 - Revisit
    # Test on LeetCode - 84ms
    # BFS - use dictionary to record nodes
    def clone_graph_bfs_nice(self, node):
        if node is None:
            return None
        clone_node_dict = {}
        root = node
        clone_root = UndirectedGraphNode(root.label)
        clone_node_dict[root.label] = clone_root
        nodes = deque()
        nodes.append(root)
        while nodes:
            node = nodes.popleft()
            for neighbor in node.neighbors:
                if neighbor.label not in clone_node_dict:
                    clone_node_dict[neighbor.label] = UndirectedGraphNode(neighbor.label)
                    nodes.append(neighbor)
                clone_node_dict[node.label].neighbors.append(clone_node_dict[neighbor.label])
        return clone_root

    # Test on LeetCode - 232ms
    # use DFS, visit neighbors, clone if necessary.
    # Note: Remember visited nodes
    def clone_graph_dfs(self, node):
        visited = {}
        return self.clone_node(node, visited)

    def clone_node(self, node, visited):
        if node is None:
            return None

        node_clone = UndirectedGraphNode(node.label)
        node_label = node.label
        if node_label not in visited:
            visited[node_label] = node_clone
        for neighbor in node.neighbors:
            neighbor_label = neighbor.label
            if neighbor_label in visited:
                neighbor_clone = visited[neighbor_label]
            else:
                neighbor_clone = self.clone_node(neighbor, visited)
            node_clone.neighbors.append(neighbor_clone)
        return node_clone