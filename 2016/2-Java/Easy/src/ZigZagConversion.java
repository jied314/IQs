/**
 * Created by jie on 12/18/15.
 */
public class ZigZagConversion {
    public String convert(String s, int numRows) {
        if (numRows == 1) return s;
        char[] ca = s.toCharArray();
        int length = s.length();
        StringBuilder[] sa = new StringBuilder[numRows];
        for (int i = 0; i < numRows; i++) {
            sa[i] = new StringBuilder();
        }
        int i = 0;
        int row, unit = numRows + numRows - 2;
        while (i < length) {
            row = i % unit;
            if (row >= numRows) {
                row = unit - row;
            }
            sa[row].append(ca[i++]);
        }
        for (i = 1; i < numRows; i++) {
            sa[0].append(sa[i]);
        }
        return sa[0].toString();
    }

    public static void main(String[] args) {
        ZigZagConversion test = new ZigZagConversion();
        System.out.println(test.convert("ABCD", 3));
    }
}
