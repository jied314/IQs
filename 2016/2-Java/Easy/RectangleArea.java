/**
 * Created by jie on 6/9/15.
 * Inspired by nice solutions on LeetCode.
 */
public class RectangleArea {
    // check condition for non-overlapping
    private boolean checkNonOverlapping(int A, int B, int C, int D, int E, int F, int G, int H) {
        return (A >= G || E >= C || B >= H || F >= D);
    }

    // check condition for overlapping
    private boolean checkOverlapping(int A, int B, int C, int D, int E, int F, int G, int H) {
        return (Math.min(D, H) > Math.max(F, B)) && (Math.min(G, C) > Math.max(A, E));
    }

    public int computeArea(int A, int B, int C, int D, int E, int F, int G, int H) {
        int overLappingarea = 0;
        int total = totalArea(A, B, C, D, E, F, G, H);
        if (!checkNonOverlapping(A, B, C, D, E, F, G, H)) {
            int x = Math.min(C, G) - Math.max(A, E);
            int y = Math.min(D, H) - Math.max(B, F);
            overLappingarea = x * y;
        }
        return total - overLappingarea;
    }

    private int totalArea(int A, int B, int C, int D, int E, int F, int G, int H) {
        return recArea(A, B, C, D) + recArea(E, F, G, H);
    }

    private int recArea(int A, int B, int C, int D) {
        return (C - A) * (D - B);
    }

    public static void main(String[] args) {
        RectangleArea ra = new RectangleArea();
        System.out.println(ra.computeArea(-1, 0, 1, 2, 0, -1, 2, 1));
        System.out.println(ra.computeArea(0, -1, 2, 1, -1, 0, 1, 2)); // reverse above
        System.out.println(ra.computeArea(-1, 0, 1, 2, 0, 1, 2, 3));
        System.out.println(ra.computeArea(-1, 0, 1, 2, 0, 0, 2, 2));
        System.out.println(ra.computeArea(-1, 0, 1, 2, 2, -1, 4, 1)); // non-overlapping
    }
}
