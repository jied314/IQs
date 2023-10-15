import java.util.*;

public class ContainsDuplicate {
    public boolean containsDuplicateDict(int[] nums) {
        if (nums == null || (nums.length < 2)) return false;
        Map<Integer, Integer> num_dict = new HashMap<Integer, Integer> ();
        for (int num : nums) {
            if (num_dict.containsKey(num)) return true;
            else num_dict.put(num, 1);
        }
        return false;
    }

    /* much faster than dictionary version - also avoid boundary check */
    public boolean containsDuplicateSet(int[] nums) {
        final Set<Integer> distinct = new HashSet<>();
        for (int num : nums) {
            if (!distinct.add(num)) return true;
        }
        return false;
    }
}