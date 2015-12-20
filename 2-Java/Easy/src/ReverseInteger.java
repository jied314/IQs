/**
 * Created by jie on 12/18/15.
 * In case of overflow, use long.
 */
public class ReverseInteger {
    public int reverse(int x) {
        if (x == 0) return 0;
        int sign = 1;
        long max = Integer.MAX_VALUE;
        if (x < 0) {
            sign = -1;
            x = Math.abs(x);
            max++;
        }
        int i = 0; long ret = 0;
        for (; i < 9; i++) {
            if (x > 0) {
                ret = (ret * 10) + (x % 10);
                x /= 10;
            } else {
                break;
            }
        }
        if ((x > 0) && (i == 9)) {
            if (((ret * 10) + (x % 10)) > max) return 0;
            ret = (ret * 10) + (x % 10);
        }
        return (int)(sign * ret);
    }
}