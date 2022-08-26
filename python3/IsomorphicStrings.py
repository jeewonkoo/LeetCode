class Solution:
    def isIsomorphic(self, s, t):
        """
        type s: str, t: str
        rtype: bool
        """
        s_dictionary, t_dictionary = {}, {}
        for s_c, t_c in zip(s, t):
            if s_c not in s_dictionary and t_c not in t_dictionary: 
                s_dictionary[s_c] = t_c
                t_dictionary[t_c] = s_c
            elif s_dictionary.get(s_c) != t_c or t_dictionary.get(t_c) != s_c:
                return False  
            
        return True

if __name__ == "__main__":
    s = Solution()
    print(s.isIsomorphic("egg", "add"))    
    print(s.isIsomorphic("foo", "bar"))
    print(s.isIsomorphic("paper", "title"))
    print(s.isIsomorphic("badc", "babc"))