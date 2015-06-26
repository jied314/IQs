/**
 * 6/25 & 6/26 - Data Structure, Binary Search Tree
 * (inspired by submitted solutions)
 * Given an array of integers, find out whether there are two distinct indices i and j 
 * in the array such that the difference between nums[i] and nums[j] is at most t and 
 * the difference between i and j is at most k.
 * 
 * Note: 
 * 	Integer Overflow
 * 	Maintain a tree - O(NlgN) 
 * 	Bucket with sliding window - O(N) use hasing idea
 */

import java.util.TreeSet;
import java.util.HashMap;

public class ContainDuplicate3 {
	// utilize tree
    public boolean containsNearbyAlmostDuplicateTree(int[] nums, int k, int t) {
        if (nums == null || nums.length == 0 || k <= 0) return false;

        TreeSet<Integer> values = new TreeSet<> ();  // use tree to back up a set, preserve natural ordering, O(lgn)
        for (int index = 0; index < nums.length; index++) {
        	Integer floor = values.floor(nums[index] + t);
        	Integer ceiling = values.ceiling(nums[index] - t);
        	if ((floor != null && floor >= nums[index]) || ceiling != null && ceiling <= nums[index]) {
        		return true;
        	}
        	values.add(nums[index]);

        	// k contraint
        	if (index >= k) {
        		values.remove(nums[index - k]);
        	}
        }
        return false;
    }

    // utilize hashing 
    public boolean containsNearbyAlmostDuplicateBucket(int[] nums, int k, int t) {
    	if (nums == null || nums.length < 2 || k < 1) return false;

        Map<Long, Long> map = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            long remappedNum = (long) nums[i] - Integer.MIN_VALUE;  // deal with negatives
            long bucket = remappedNum / ((long) t + 1);
            if (map.containsKey(bucket)
                    || (map.containsKey(bucket - 1) && remappedNum - map.get(bucket - 1) <= t)
                        || (map.containsKey(bucket + 1) && map.get(bucket + 1) - remappedNum <= t))
                            return true;
            if (map.entrySet().size() >= k) {
                long lastBucket = ((long) nums[i - k] - Integer.MIN_VALUE) / ((long) t + 1);
                map.remove(lastBucket);
            }
            map.put(bucket, remappedNum);
        }
        return false;
    }

    public static void main(String[] args) {
    	ContainDuplicate3 test = new ContainDuplicate3();
    	System.out.println(test.containsNearbyAlmostDuplicateTree(new int[] {1,3,1}, 2, 1));
    }
}
