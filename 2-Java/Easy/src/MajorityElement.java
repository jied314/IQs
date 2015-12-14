public class Solution {
	/**
	 * the majority element must be the middle element of the sorted array
	 */
    public int MajorityElementArray(int[] nums) {
        Arrays.sort(nums);
        return nums[nums.length/2];
    }
}