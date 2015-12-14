import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

/**
 * 12/14 - Array, HashTable, Sort
 */
public class ValidAnagram {
    public boolean isAnagramDict(String s, String t) {
        if (s.length() != t.length()) return false;
        Boolean isValidAnagram = true;
        Map<Character, Integer> charDict = new HashMap<Character, Integer>();
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (!charDict.containsKey(c)) {
                charDict.put(c, 0);
            }
            charDict.put(c, charDict.get(c)+1);
        }
        for (int i = 0; i < t.length(); i++) {
            char c = t.charAt(i);
            if (!charDict.containsKey(c) || charDict.get(c) == 0) {
                isValidAnagram = false;
            } else {
                charDict.put(c, charDict.get(c)-1);
            }
        }
        return isValidAnagram;
    }

    /* much faster than dictionary version */
    public boolean isAnagramArray(String s, String t) {
        if (s.length() != t.length()) return false;
        Boolean isValidAnagram = true;
        int[] chars = new int[26];
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            chars[c-'a']++;
        }
        for (int i = 0; i < t.length(); i++) {
            char c = t.charAt(i);
            if (chars[c-'a'] == 0) {
                isValidAnagram = false;
            } else {
                chars[c-'a']--;
            }
        }
        return isValidAnagram;
    }

    /* second fast - faster than dictionary version */
    public boolean isAnagramSort(String s, String t) {
        if (s.length() != t.length()) return false;
        char[] ss = s.toCharArray();
        char[] tt = t.toCharArray();
        Arrays.sort(ss);
        Arrays.sort(tt);
        for (int i = 0; i < s.length(); i++) {
            if (ss[i] != tt[i]) return false;
        }
        return true;
    }

    public static void main(String[] args) {
        ValidAnagram test = new ValidAnagram();
        System.out.println(test.isAnagramDict("anagram", "nagaram"));
        System.out.println(test.isAnagramArray("anagram", "nagaram"));
        System.out.println(test.isAnagramSort("anagram", "nagaram"));
    }
}
