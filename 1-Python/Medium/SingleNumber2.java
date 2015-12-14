import java.util.Arrays;

/**
 * 6/28 Bit Manipulation
 * Given an array of integers, every element appears three times except for one. Find that single one.
 * Use Java because of negative numbers
 * Also check Python Version
 */
public class SingleNumber2 {
    public int singleNumber(int[] A) {
    	int[] result = new int[32];
    	int num = 0;
    	for (int i = 0; i < 32; i++) {
    		for (int j = 0; j < A.length; j++) {
    			result[i] += (A[j] >> i) & 1;
    		}
    		result[i] %= 3;
    		num += (result[i] & 1) << i;
    	}
    	// System.out.println(Arrays.toString(result));
    	return num;
    }

    public int singleNumber_first(int[] A) {
    	int[] result = new int[32];
    	int num = 0;
    	for (int i = 0; i < 32; i++) {
    		for (int j = 0; j < A.length; j++) {
                // wrong - result[i] += A[j] & (1 << i); 
    			result[i] += (A[j] & (1 << i)) == 0 ? 0: 1;
    		}
    		result[i] %= 3;
    		num += (result[i] & 1) << i;
    	}
    	// System.out.println(Arrays.toString(result));
    	return num;
    }

    /**
     * use bitmask variables
     * 1. ones as a bitmask to represent the ith bit had appeared once.
     * 2. twos as a bitmask to represent the ith bit had appeared twice.
     * 3. threes as a bitmask to represent the ith bit had appeared three times.
     * When the ith bit had appeared for the third time, clear the ith bit of both ones and twos to 0. 
     * The final answer will be the value of ones.
     */
    public int singleNumber(int A[], int n) {
        int ones = 0, twos = 0, threes = 0;
        for (int i = 0; i < n; i++) {
            twos |= ones & A[i]; // find the common bit patterns (appear twice)
            ones ^= A[i];
            threes = ones & twos;
            ones &= ~threes;
            twos &= ~threes;
        }
        return ones;
    }

    public static void main(String[] args) {
    	SingleNumber test = new SingleNumber();
    	System.out.println(test.singleNumber(new int[] {-2,-2,1,1,-3,1,-3,-3,-4,-2}));
    	System.out.println(test.singleNumberError(new int[] {-2,-2,1,1,-3,1,-3,-3,-4,-2}));
    }
}