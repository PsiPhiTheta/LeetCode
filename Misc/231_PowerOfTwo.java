class Solution {
    public boolean isPowerOfTwo(int n) {
        if (n<=0) {
            return false;
        }
    
        if (n == Math.pow(2, Math.round(Math.log(n)/Math.log(2)))) {
            return true;
        }
        else {
            return false;
        }
    }
}
