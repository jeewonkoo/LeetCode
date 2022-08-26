from curses.ascii import SO


class Solution:
    def reverseString(self, s) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        """
        type s: List[str]
        rtype: None
        """
        start, end = 0, len(s)-1
        
        while start < end: 
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1
            
        return s

if __name__ == '__main__':
    s = Solution()
    print(s.reverseString(["h","e","l","l","o"]))
    print(s.reverseString(["H","a","n","n","a","h"]))