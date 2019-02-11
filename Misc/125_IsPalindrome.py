class Solution:
    def isPalindrome(self, s: 'str') -> 'bool':
        clean = str.lower(''.join(filter(str.isalnum, s)))
        clean_inv = clean[::-1]
        
        print(clean, clean_inv)
        
        if clean == clean_inv:
            return True
        else:
            return False
