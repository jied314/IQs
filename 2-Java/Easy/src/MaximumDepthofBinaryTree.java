/**
 * 12/14 - Tree, DFS
 * Given a binary tree, find its maximum depth.
 * The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
 * Note: how to do DFS
 */
public class MaximumDepthofBinaryTree {
    public int height = 0;

    public int maxDepth(TreeNode root) {
        this.height = 0;
        maxDepthHelper(root, 0);
        return this.height;
    }

    public void maxDepthHelper(TreeNode node, int height) {
        if (node == null) {
            return;
        }
        height++;
        this.height = Math.max(this.height, height);
        maxDepthHelper(node.left, height);
        maxDepthHelper(node.right, height);
    }

    public int maxDepthNice(TreeNode root) {
        if (root == null) return 0;
        return 1 + Math.max(maxDepthNice(root.left), maxDepthNice(root.right));
    }
}