package Tree

/**
 * Serialization is the process of converting a data structure or object into a sequence of bits so that it can be
 * stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the
 * same or another computer environment.
 *
 * Design an algorithm to serialize and deserialize an N-ary tree. An N-ary tree is a rooted tree in which each node
 * has no more than N children. There is no restriction on how your serialization/deserialization algorithm should work.
 * You just need to ensure that an N-ary tree can be serialized to a string and this string can be deserialized to
 * the original tree structure.
 */

// Definition for an N-ary tree node.
class NaryTreeNode(var num: Int) {
    var children: List<NaryTreeNode>? = null
}


class Codec {
    // Encodes a tree to a single string.
    fun serialize(root: NaryTreeNode?): String {
        return ""
    }

    // Decodes your encoded data to tree.
    fun deserialize(data: String?): NaryTreeNode? {
        return null
    }
}


// Your Codec object will be instantiated and called as such:
// Codec codec = new Codec();
// codec.deserialize(codec.serialize(root));