import java.util.Arrays;

/**
 * Created by jie on 6/8/15.
 * Find the total area covered by two rectilinear rectangles in a 2D plane.
 * Steps:
 * 		1. check whether overlapping
 *		2. calculate overlapping area
 */
public class RectangleArea_DJ {
	private boolean isOverlapping = true;

    public int computeArea(int A, int B, int C, int D, int E, int F, int G, int H) {
    	int[] Xs = edges(A, C, E, G);
    	System.out.println(Arrays.toString(Xs));
    	if (!isOverlapping) return totalArea(A, B, C, D, E, F, G, H);    	
    	int [] Ys = edges(B, D, F, H);
    	System.out.println(Arrays.toString(Ys));
    	if (!isOverlapping) return totalArea(A, B, C, D, E, F, G, H);    	
    	return totalArea(A, B, C, D, E, F, G, H) - recArea(Xs[0], Ys[0], Xs[1], Ys[1]);
    }

    private int[] edges(int A, int C, int E, int G) {
    	int[] result = new int[2];
    	if (E >= A) {
    		if (E < C) {
    			result[0] = E;
    			result[1] = (G > C) ? C : G;
    		} else { // no overlapping
    			isOverlapping = false;
    		}
    	} else {
    		return edges(E, G, A, C);
    	}
    	return result;
    }

    private int totalArea(int A, int B, int C, int D, int E, int F, int G, int H) {
    	return recArea(A, B, C, D) + recArea(E, F, G, H);
    }

 	private int recArea(int A, int B, int C, int D) {
 		return (C - A) * (D - B);
 	}
 	

 	public static void main(String[] args) {
 		RectangleArea_DJ ra = new RectangleArea_DJ();
 		System.out.println(ra.computeArea(-1, 0, 1, 2, 0, -1, 2, 1)); 
 		System.out.println(ra.computeArea(0, -1, 2, 1, -1, 0, 1, 2)); // reverse above
 		System.out.println(ra.computeArea(-1, 0, 1, 2, 0, 1, 2, 3));
 		System.out.println(ra.computeArea(-1, 0, 1, 2, 0, 0, 2, 2));
 		System.out.println(ra.computeArea(-1, 0, 1, 2, 2, -1, 4, 1)); // non-overlapping
 	}
}
