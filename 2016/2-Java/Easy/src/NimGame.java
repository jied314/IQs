/**
 * 12/14 - Easy
 * You are playing the following Nim Game with your friend:
 * There is a heap of stones on the table, each time one of you take turns to remove 1 to 3 stones.
 * The one who removes the last stone will be the winner. You will take the first turn to remove the stones.
 * Both of you are very clever and have optimal strategies for the game. Write a function to determine whether you can
 * win the game given the number of stones in the heap.
 * For example, if there are 4 stones in the heap, then you will never win the game:
 * no matter 1, 2, or 3 stones you remove, the last stone will always be removed by your friend.
 *
 * Math, DP
 * Idea:
 * n  =  1  2  3   4  5  6  7   8  9  10
 * dp = [1, 1, 1, -1, 1, 1, 1, -1, 1, 1, ...]
 * dp(n) = 1 if (dp(1) == 1 and dp(n-1) == -1) or (dp(2) == 1 and dp(n-2) == -1) or (dp(3) == 1 and dp(n-3) == -1)
 * I pick k (k = 1, 2, 3), dp(n-k) has to lose.
 * Observing the above combinations, k can not be multiply of 4.
 */
public class NimGame {
    public boolean canWinNim(int n) {
        return n % 4 != 0;
    }

    public static void main(String[] args) {
        NimGame test = new NimGame();
        System.out.println(test.canWinNim(7));
    }
}