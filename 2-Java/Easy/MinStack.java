import java.util.Arrays;

/*
 * LeetCode - MinStack
 * Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
 * Use minStack to keep track of mins
 * Note: space-time tradeoff & duplicates
 */
public class MinStack {
	private int[] internalArray;
	private int nextIndex;
	private int[] minStack;
	private int minIndex;

	public MinStack() {
		this(100);
	}

	public MinStack(int initialSize) {
		internalArray = new int[initialSize];
		nextIndex = 0;
		minStack = new int[initialSize];
		minIndex = 0;
	}

	// push into the stack, expand the internalArray if necessary
	// update minStack
	public void push(int x) {
		internalArray = checkCapacity(internalArray, nextIndex);
		internalArray[nextIndex++] = x;
		checkPushMinStack(x);
	}


	public int pop() {
		assert nextIndex > 0;  // cannot pop if empty
		int top = internalArray[--nextIndex];
		internalArray[nextIndex] = 0;
		checkPopMinStack(top);
		return top;
	}


	public int top() {
		if (nextIndex == 0) return 0;
		else return internalArray[nextIndex - 1];
	}


	public int getMin() {
		/** int min = internalArray[0];
		for (int i = 1; i < nextIndex; i++) {  // note to use nextIndex, not length
			if (min > internalArray[i]) min = internalArray[i];
		}
		return min; */
		return minStack[minIndex - 1];
	}


	private int[] checkCapacity(int[] someArray, int endIndex) {
		if (endIndex == someArray.length) { // array is full
			int[] tempArray = someArray;
			someArray = new int[(int)(tempArray.length * 1.5)];
			for(int i = 0; i < tempArray.length; i++) {
				someArray[i] = tempArray[i];
			}
		}
		return someArray;
	}


	// push to stack if x is minimum
	private void checkPushMinStack(int x) {
		if (minIndex == 0) minStack[minIndex++] = x;  // empty stack
		else if (minStack[minIndex - 1] >= x) {  // '='' for duplicates
			minStack = checkCapacity(minStack, minIndex);
			minStack[minIndex++] = x;
		}
	}


	// pop if x is minimum
	private void checkPopMinStack(int x) {
		if (x == minStack[minIndex - 1]) minStack[--minIndex] = 0;
	}


	private void printArray() {
		System.out.println(Arrays.toString(internalArray));
		System.out.println(Arrays.toString(minStack));
	}


	public static void main(String[] args) {
		MinStack ms = new MinStack(3);
		ms.push(4);
		ms.push(2);
		ms.push(2);
		ms.printArray();
		ms.push(1);
		ms.printArray();
		ms.push(2);
		ms.printArray();
		System.out.format("Min is %d\n", ms.getMin());
		System.out.format("top is %d\n", ms.top());
		System.out.format("pop %d\n", ms.pop());
		System.out.format("Min is %d\n", ms.getMin());
		ms.printArray();
		System.out.format("pop %d\n", ms.pop());
		System.out.format("Min is %d\n", ms.getMin());
		ms.printArray();
		System.out.format("pop %d\n", ms.pop());
		System.out.format("Min is %d\n", ms.getMin());
		ms.printArray();
	}
}
