/**
 * 12/20 - Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
 */

import java.util.*;

public class MinStack {
    static class Element {
        int val;
        int min;
        Element(int val, int min) {
            this.val = val;
            this.min = min;
        }
    }
    
    Deque<Element> stack;
    
    MinStack() {
        this.stack = new ArrayDeque<>();
    }    
    
    public void push(int x) {
        this.stack.addFirst(new Element(x, this.stack.isEmpty()? x: Math.min(x, getMin())));
    }

    public void pop() {
        this.stack.removeFirst();
    }

    public int top() {
        return this.stack.peekFirst().val;
    }

    public int getMin() {
        return this.stack.peekFirst().min;
    }

    public static void main(String[] args) {
        MinStack test = new MinStack();
        System.out.println(test.getMin());
    }
}