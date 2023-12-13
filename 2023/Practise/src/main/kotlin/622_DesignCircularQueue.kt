/**
 * Design your implementation of the circular queue.
 * The circular queue is a linear data structure in which the operations are performed based on FIFO
 * (First In First Out) principle, and the last position is connected back to the first position to make a circle.
 * It is also called "Ring Buffer".
 *
 * One of the benefits of the circular queue is that we can make use of the spaces in front of the queue.
 * In a normal queue, once the queue becomes full, we cannot insert the next element even if there is a space
 * in front of the queue. But using the circular queue, we can use the space to store new values.
 *
 * Implement the MyCircularQueue class:
 *
 * MyCircularQueue(k) Initializes the object with the size of the queue to be k.
 * int Front() Gets the front item from the queue. If the queue is empty, return -1.
 * int Rear() Gets the last item from the queue. If the queue is empty, return -1.
 * boolean enQueue(int value) Inserts an element into the circular queue. Return true if the operation is successful.
 * boolean deQueue() Deletes an element from the circular queue. Return true if the operation is successful.
 * boolean isEmpty() Checks whether the circular queue is empty or not.
 * boolean isFull() Checks whether the circular queue is full or not.
 * You must solve the problem without using the built-in queue data structure in your programming language.
 *
 * Example:
 * Input
 *     ["MyCircularQueue", "enQueue", "enQueue", "enQueue", "enQueue", "Rear", "isFull", "deQueue", "enQueue", "Rear"]
 *     [[3], [1], [2], [3], [4], [], [], [], [4], []]
 * Output
 *     [null, true, true, true, false, 3, true, true, true, 4]
 *
 * Solutions:
 * 1. Array based circular queue - use head, count & capacity
 *    tailIndex == (headIndex + count − 1) % capacity
 *    Note: do not rely on head, tail & capacity since it is more complicated to check size.
 *    O(1) Time Complexity & O(N) Space Complexity
 *
 * 2. Singly-Linked List
 *    Rely on head, tail, count & capacity
 *    More efficient than array based solution since no need to pre-allocate space
 *    O(1) Time Complexity & O(N) Space Complexity
 */

class MyCircularQueueWithArray(k: Int) {

    private val capacity = k
    private val data = IntArray(k)
    private var head = 0
    private var count = 0

    fun enQueue(value: Int): Boolean {
        if (isFull()) return false

        count++
        val tail = (head + count - 1) % capacity
        data[tail] = value
        return true
    }

    fun deQueue(): Boolean {
        if (isEmpty()) return false

        count--
        head = (head + 1) % capacity
        return true
    }

    fun Front(): Int {
        return if (isEmpty()) -1 else data[head]
    }

    fun Rear(): Int {
        if (isEmpty()) return -1
        val tail = (head + count - 1) % capacity
        return data[tail]
    }

    fun isEmpty(): Boolean { // or size == 0
        return count == 0
    }

    fun isFull(): Boolean { // or size == k
        return count == capacity
    }
}

class MyCircularQueueLinkedList(k: Int) {

    internal class Node(val num: Int) {
        var next: Node? = null
    }

    private val capacity = k
    private var count = 0
    private var headNode: Node? = null
    private var tailNode: Node? = null

    fun enQueue(value: Int): Boolean {
        if (isFull()) return false

        val newNode = Node(value)
        if (isEmpty()) {
            headNode = newNode
            tailNode = headNode
        } else {
            tailNode!!.next = newNode
            tailNode = newNode
        }
        count++
        return true
    }

    fun deQueue(): Boolean {
        if (isEmpty()) return false

        count--
        headNode = headNode!!.next
        return true
    }

    fun Front(): Int {
        return if (isEmpty()) -1 else headNode!!.num
    }

    fun Rear(): Int {
        if (isEmpty()) return -1
        return tailNode!!.num
    }

    fun isEmpty(): Boolean {
        return count == 0
    }

    fun isFull(): Boolean {
        return count == capacity
    }
}

fun main() {
    val myQueue = MyCircularQueueLinkedList(3)
    println(myQueue.enQueue(1)) // return True
    println(myQueue.enQueue(2)) // return True
    println(myQueue.enQueue(3)) // return True
    println(myQueue.enQueue(4)) // return False
    println(myQueue.Rear())     // return 3
    println(myQueue.isFull())   // return True
    println(myQueue.deQueue())  // return True
    println(myQueue.enQueue(4)) // return True
    println(myQueue.Rear())     // return 4
}