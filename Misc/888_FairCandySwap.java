//O(n^2) - 52/75 test cases passed;

import java.util.stream.*; 

class Solution {
    public int[] fairCandySwap(int[] A, int[] B) {
        int tempA = 0;
        int tempB = 0;
        int sumA = 0;
        int sumB = 0;
        int[] output = {0, 0};
        
        for (int i = 0; i<A.length; i++) {
            for (int j = 0; j<B.length; j++) {
                tempA = A[i];
                tempB = B[j];
                A[i] = tempB;
                B[j] = tempA;
                sumA = IntStream.of(A).sum();
                sumB = IntStream.of(B).sum();
                
                if (sumA == sumB) {
                    output[0] = tempA;
                    output[1] = tempB; 
                    return output;
                }
                
                A[i] = tempA;
                B[j] = tempB;
            }
        }
        
        return output;
    }
}
