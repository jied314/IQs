package LinkedList

/**
 * Design your implementation of the linked list. You can choose to use a singly or doubly linked list.
 * A node in a singly linked list should have two attributes: val and next. val is the value of the current node,
 * and next is a pointer/reference to the next node.
 * If you want to use the doubly linked list, you will need one more attribute prev to indicate the previous node
 * in the linked list. Assume all nodes in the linked list are 0-indexed.
 */

class ListNode(var num: Int) {
    var next: ListNode? = null
}
class MyLinkedListSingly {

    private val head = ListNode(-1)
    var size = 0

    /**
     * Get the value of the index node in the linked list. If the index is invalid, return -1
     */
    fun get(index: Int): Int {
        if (index >= size || index < 0 || size == 0) return -1
        var node = head
        for (i in 0..index) {
            node = node.next!!
        }
        return node.num
    }

    /**
     * Add a node of value val before the first element of the linked list. After the insertion,
     * the new node will be the first node of the linked list.
     */
    fun addAtHead(`val`: Int) {
        addAtIndex(0, `val`)
    }

    /**
     * Append a node of value val as the last element of the linked list.
     */
    fun addAtTail(`val`: Int) {
        addAtIndex(size, `val`)
    }

    /**
     * Add a node of value val before the index node in the linked list. If index equals the length of the linked list,
     * the node will be appended to the end of the linked list. If index is greater than the length, the node will not
     * be inserted.
     */
    fun addAtIndex(index: Int, `val`: Int) {
        if (index > size) return
        var prev = head
        for (i in 0..<index) {
            prev = prev.next!!
        }
        val next = prev.next
        val newNode = ListNode(`val`)
        newNode.next = next
        prev.next = newNode
        size++
    }

    /**
     * Delete the index node in the linked list, if the index is valid.
     */
    fun deleteAtIndex(index: Int) {
        if (index < 0 || index >= size) return
        var prev = head
        for (i in 0..<index) {
            prev = prev.next!!
        }
        val nodeToDelete = prev.next
        prev.next = nodeToDelete!!.next
        nodeToDelete.next = null
        size--
    }

    fun toList(): List<Int> {
        val list = mutableListOf<Int>()
        var node = head.next
        while (node != null) {
            list.add(node.num)
            node = node.next
        }
        return list
    }
}

fun main() {
    val myLinkedList = MyLinkedListSingly()
    myLinkedList.addAtHead(1)
    println(myLinkedList.toList())
    myLinkedList.addAtTail(3)
    println(myLinkedList.toList())
    myLinkedList.addAtIndex(1, 2) // linked list becomes 1->2->3
    println(myLinkedList.toList())

    println(myLinkedList.get(1)) // return 2

    myLinkedList.deleteAtIndex(1) // now the linked list is 1->3
    println(myLinkedList.toList())

    println(myLinkedList.get(1)) // return 3
}