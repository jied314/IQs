public class ExcelSheetColumnNumber {
    public int titleToNumber(String s) {
        int BASE = 26;
        int length = s.length();
        int number = 0;
        for (int i = 0; i < length; i++) {
            // number += (s.charAt(i) - 'A' + 1) * (int)(Math.pow(BASE, (length-1-i)));
            number = number * BASE + s.charAt(i) - 'A' + 1;
        }
        return number;
    }
}