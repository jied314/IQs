/**
 * Created by jie on 6/7/15.
 * LeetCode - Interleaving String
 * Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.
 * Idea:
 * 		1. check whether exhause any of the string
 *		2. check whether the next character is the same
 */
public class Solution {
	public boolean isInterleave(String s1, String s2, String s3) {
		boolean result = true;
		if (result = checkLength(s1, s2, s3)) {
			int index1 = 0;
			int index2 = 0;
			int index3 = 0;
			int match = 0;
			while (index3 < s3.length()) {
				if ((index1 >= s1.length()) || (index2 >= s2.length())) {
					result = checkExhaust(s1, s2, s3, index1, index2, index3);
					break;
				} else {
					// compare s1 and s2 against s3
					if (s1.charAt(index1) != s3.charAt(index3) && (s2.charAt(index2) != s3.charAt(index3))) { 
						result = false; // cannot find match
						break;
					} else {
						while (s1.charAt(index1) == s2.charAt(index2)) { // same character, check the following characters
							match++;
							index3++;
							index1++;
							index2++;
							if ((index1 >= s1.length()) && (index2 >= s2.length())) {
								return true;
							}
							if (index1 >= s1.length()) {
								if (s2.charAt(index2) == s3.charAt(index3)) {
									index2++;
									index1--;
									index3++;
									return checkExhaust(s1, s2, s3, index1, index2, index3);
								} else {
									return checkExhaust(s1, s2, s3, index1, index2 - match, index3);
								}
							} else if (index2 >= s2.length()) {
								if (s1.charAt(index1) == s3.charAt(index3)) {
									index1++;
									index2--;
									index3++;
									return checkExhaust(s1, s2, s3, index1, index2, index3);
								} else {
									return checkExhaust(s1, s2, s3, index1 - match, index2, index3);
								}
							}
						}
						/* int temp = match;
						while ((temp > 0) && (s3.charAt(index3) == s1.charAt(index1 - temp))) {
							temp--;
							index3++;
						}*/
						// not the same character
						if (s1.charAt(index1) == s3.charAt(index3)) {		
							index2 -= match;
							if (s1.charAt(index1) != s2.charAt(index2)) {
								index1++;	
								index3++;	
							}
						} else if (s2.charAt(index2) == s3.charAt(index3)) {
							index1 -= match;
							if (s2.charAt(index2) != s1.charAt(index1)) {
								index2++;
								index3++;
							}
						} else {
							index3 += match;
						}
						match = 0;		
					}				
				}				
			}
		}
		return result;
    }


    private boolean checkExhaust(String s1, String s2, String s3, int index1, int index2, int index3) {
    	boolean result = false;
    	if (index1 >= s1.length()) { // exhause s1, compare s2 and s3
			result = strMatch(s2, index2, s3, index3);
		} else if (index2 >= s2.length()) { // exhause s2, compare s1 and s3
			result = strMatch(s1, index1, s3, index3);
		}
		return result;
    }


    private boolean checkLength(String s1, String s2, String s3) {
    	return s3.length() == s1.length() + s2.length();
    }


    private boolean strMatch(String source, int sourceIndex, String destination, int destinationIndex) {
    	for (int i = 0; i < destination.length() - destinationIndex; i++) {
    		if (destination.charAt(destinationIndex + i) != source.charAt(sourceIndex + i)) {
    			return false;
    		}
    	}
    	return true;
    }


    public static void main(String[] args) {
    	Solution s = new Solution();
    	//System.out.println(s.isInterleave("aabcc", "dbbca", "aadbbcbcac"));
		//System.out.println(s.isInterleave("aabcc", "dbbca", "aadbbbaccc"));
		System.out.println(s.isInterleave("aabd", "abdc", "aabdabcd"));
		//System.out.println(s.isInterleave("", "", "a"));
		//System.out.println(s.isInterleave("aa", "ab", "aaba"));
		//System.out.println(s.isInterleave("aa", "ab", "aaab"));
    }
}
