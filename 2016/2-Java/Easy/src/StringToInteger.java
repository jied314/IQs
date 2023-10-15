/**
 * Created by jie on 12/20/15.
 */
public class StringToInteger {
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
                if ((ret > (Integer.MAX_VALUE / 10)) || ((ret == (Integer.MAX_VALUE / 10)) && (c > '7'))) {
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
}
