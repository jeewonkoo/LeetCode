class Solution:
    def isPalindrome_two_pointer(self, s: str) -> bool:
        s = s.lower()
        start, end = 0, len(s)-1
        while start <= end:
            # print(s[start], s[end])
            
            if not s[start].isalnum(): start += 1
            if not s[end].isalnum(): end -= 1
            elif s[start].isalnum() and s[end].isalnum():
                if s[start] == s[end]: start, end = start + 1, end - 1
                else: return False
                
            
        return True

    def isPalindrome_extra_string(self, s: str) -> bool:
        string = ""
        for i in s: 
            if i.isalpha() or i.isnumeric(): string += i.lower()
        return string == string [::-1]