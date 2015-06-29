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

    public int singleNumberError(int[] A) {
    	int[] result = new int[32];
    	int num = 0;
    	for (int i = 0; i < 32; i++) {
    		for (int j = 0; j < A.length; j++) {
    			result[i] += (A[j] & (1 << i)) == 0 ? 0: 1;
    		}
    		result[i] %= 3;
    		num += (result[i] & 1) << i;
    	}
    	// System.out.println(Arrays.toString(result));
    	return num;
    }

    public static void main(String[] args) {
    	SingleNumber test = new SingleNumber();
    	System.out.println(test.singleNumber(new int[] {-2,-2,1,1,-3,1,-3,-3,-4,-2}));
    	System.out.println(test.singleNumberError(new int[] {-2,-2,1,1,-3,1,-3,-3,-4,-2}));
    }
}