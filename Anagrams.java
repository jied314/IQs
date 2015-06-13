import java.util.List;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Arrays;

/**
 * Created by jie on 6/9/15.
 * Given an array of strings, return all groups of strings that are anagrams.
 * Step:
 *      1. store all str into hashmap, key is an ascending order array of all characters.
 *      2. return all hash value greater than 1.
 */
public class Anagrams {
    public List<String> anagrams(String[] strs) {
        HashMap<String, ArrayList<String>> dict = new HashMap<>();
        ArrayList<String> result = new ArrayList<>();
        char[] sorted;
        String str, sortedString;
        for (int i = 0; i < strs.length; i++) {
            str = strs[i];
            sorted = str.toCharArray();
            Arrays.sort(sorted);
            sortedString = new String(sorted);
            if (!dict.containsKey(sortedString)) {
                ArrayList<String> values = new ArrayList<>();
                values.add(str);
                dict.put(sortedString, values);
            } else {
                dict.get(sortedString).add(str);
            }
        }
        for (String key : dict.keySet()) {
            if (dict.get(key).size() > 1) {
                for (String string : dict.get(key)) {
                    result.add(string);
                }
            }
        }
        return result;
    }

    public static void main(String[] args) {
        Anagrams test = new Anagrams();
        for (String s: test.anagrams(new String[] {"listen", "silent", "william shakepeare", "i am a weakish speller"})) {
            System.out.println(s);
        }
    }
}
