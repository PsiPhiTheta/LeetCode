class Solution {
    public int rob(int[] nums) {
        int even_total = 0;
        int odd_total = 0;
        
        for (int i = 0; i < nums.length; i++) {
            if (i % 2 == 0) {
                even_total += nums[i];
                if (even_total>odd_total) {
                    even_total = even_total;
                }
                else {
                     even_total = odd_total;
                }
            } 
            else {
                odd_total += nums[i];
                if (even_total>odd_total) {
                    odd_total = even_total;
                }
                else {
                     odd_total = odd_total;
                }
            }
        }
        if (even_total>odd_total) {
            return even_total;
        }
        else {
             return odd_total;
        }
    }
}
