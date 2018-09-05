class Solution:
    def isPalindrome(self, x):
        if (x < 0):
            return False
        
        copy = x
        reverse = 0

        while copy:
            reverse *= 10
            reverse += copy % 10
            copy //= 10

        return (x == reverse)
