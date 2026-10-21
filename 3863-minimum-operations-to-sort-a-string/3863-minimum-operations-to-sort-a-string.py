class Solution:
    def minOperations(self, s: str) -> int:
        # Check if the string is already sorted
        if all(a <= b for a, b in zip(s, s[1:])):
            return 0
        
        # If length is 2 and unsorted, a proper substring cannot be sorted
        if len(s) == 2:
            return -1
            
        mn, mx = min(s), max(s)
        
        # If the minimum is at the start or maximum is at the end
        if s[0] == mn or s[-1] == mx:
            return 1
            
        # If the minimum or maximum appears in the interior
        if any(c == mn or c == mx for c in s[1:-1]):
            return 2
            
        return 3