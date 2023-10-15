/**
 * Created by jie on 12/14/15.
 * Special Cases:
 * 1. empty spaces
 * 2. sign
 * 3. overflow
 * 4. invalid input (stop parsing)
 */

import java.util.*;

public class Test {
    public int myAtoi(String str) {
        int i = 0, length = str.length(), sign = 1, ret = 0;

        // skip beginning white spaces
        while (i < length) {
            if (str.charAt(i) != ' ')
                break;
            else
                i++;
        }
        if (i == length) { return 0; }

        // read sign if exists
        if (str.charAt(i) == '+') {
            i++;
        } else if (str.charAt(i) == '-') {
            sign = -1;
            i++;
        }

        char c;
        while (i < length) {
            c = str.charAt(i);
            if (isNumeric(c)) {
                if ((ret > (Integer.MAX_VALUE / 10)) || ((ret == (Integer.MAX_VALUE / 10)) || (c > '7'))) {
                    return (sign == 1) ? Integer.MAX_VALUE : Integer.MIN_VALUE;
                }
                ret = ret * 10 + (c - '0');
                i++;
            } else break;
        }
        return ret * sign;
    }

    private boolean isNumeric(char c) {
        return ((c >= '0') && (c <= '9'));
    }

    public static void main(String[] args) {
        Test test = new Test();
        System.out.println(test.myAtoi("123"));
        // System.out.println(test.compareVersion("1", "0"));
    }
}
