class Solution {
    public int reverse(int x) {
        int x_reverse = 0;

        while (x != 0) {
            int digit = x_reverse*10 + x%10;

            if ((digit - x%10)/10 != x_reverse) {
                return 0;
            } 
            else {
                x_reverse = digit;
            }
            
            x = x/10;   
        }
        return x_reverse;
    }
}
