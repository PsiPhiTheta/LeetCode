import java.util.stream.*; 

class Solution {
    public int[] fairCandySwap(int[] A, int[] B) {
        int sumA = 0;
        int sumB = 0;
        int[] output = {0, 0};
        sumA = IntStream.of(A).sum();
        sumB = IntStream.of(B).sum();
        int diff = (sumA - sumB)/2;
        
        for (int i = 0; i < A.length; i++) {
            for (int j = 0; j < B.length; j++) {
                if (A[i] - B[j] == diff) {
                    output[0] = A[i];
                    output[1] = B[j];
                    return output;          
                }
            }
        }
        return output;
    }
}
