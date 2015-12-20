/**
 * 12/14 - Bit Manipulation
 * Note: n is treated as an unsigned value -> while (n != 0) instead of while (n > 0)
 *       use >>> insteadof >> -> use unsigned shift (don't want to add the sign bit after shift)
 */
public class NumberOf1Bits {
    // you need to treat n as an unsigned value
    public int hammingWeight(int n) {
        int ret = 0;
        while (n != 0) {
            ret += n & 1;
            n >>>= 1;
        }
        return ret;
    }
}