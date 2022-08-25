class Solution:
    def canConstruct(self, ransomNote, magazine):
        """
        type ransomNote: str, magazine: str
        rtype: bool
        """
        magazine_alphabet = {}
        
        for i in magazine: 
            magazine_alphabet[i] = magazine_alphabet.get(i, 0) + 1
        
        for i in ransomNote: 
            if i not in magazine_alphabet: return False
            if magazine_alphabet[i] == 0: return False
            magazine_alphabet[i] -=1
        
        return True

if __name__ == '__main__': 
    s = Solution()
    print(s.canConstruct("a", "b")) #false
    print(s.canConstruct("aa", "ab"))   #false
    print(s.canConstruct("aa", "aab"))  #true