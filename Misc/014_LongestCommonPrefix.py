class Solution:
    def longestCommonPrefix(self, strs: 'List[str]') -> 'str':
        if not strs:
            return ""
        elif len(strs) == 1:
            return strs[0]
        else:
            shortest = min(strs, key=len)
            for i, char in enumerate(shortest):
                for j in strs:
                    if j[i] != char:
                        return shortest[:i]
            return shortest 
