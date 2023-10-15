import java.util.Arrays;

public class MajorityElement {
    /**
     * * the majority element must be the middle element of the sorted array
     * */
    public int MajorityElementArray(int[] nums) {
        Arrays.sort(nums);
        return nums[nums.length/2];
    }
}