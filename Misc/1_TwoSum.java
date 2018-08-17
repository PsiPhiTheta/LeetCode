class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[] result = new int[2] ;
        int first_num = 0;
        int sum = 0;

        for (int i = 0; i < nums.length; i++) {
            first_num = nums[i];
            
            for(int j = i+1; j < nums.length; j++) {
                sum = first_num+nums[j];       
                if(sum == target) {
                    result[0]=i;
                    result[1]=j;
                    return result;
                }
            }
        }
        return result;
    }
}
