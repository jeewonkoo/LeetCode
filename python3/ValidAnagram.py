class Solution:
    def isAnagram_1(self, s, t):
        """
        type s: str, t: str
        rtype: bool
        """
        frequency = {}
        for i in s: 
            frequency[i] = frequency.get(i, 0) + 1
        for i in t:
            if i not in frequency: return False
            if frequency[i] < 1: return False
            frequency[i] -= 1
        for i in frequency.values(): 
            if i != 0: return False
        
        return True  

    def isAnagram_2(self, s, t):
        """
        type s: str, t: str
        rtype: bool
        """
        frequency_s, frequency_t= {}, {}

        for i in s: 
            frequency_s[i] = frequency_s.get(i, 0) + 1
        for i in t:
            frequency_t[i] = frequency_t.get(i, 0) + 1
        
        return frequency_s == frequency_t