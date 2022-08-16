import collections
class Solution:
    def firstUniqChar_1(self, s: str) -> int:
        d = {}
        for i in s: 
            d[i] = d.get(i, 0) + 1
        for item in d.items(): 
            if item[1] == 1: return s.index(item[0])
        return -1

    #Use collections.Counter
    from collections import Counter
    def firstUniqChar_2(self, s: str) -> int:
        
        mapping = collections.Counter(s)
        
        for k, v in mapping.items():
            if v == 1:
                return s.index(k)
        return -1

    def firstUniqChar_3(self, s: str) -> int:
        counts =  collections.Counter(s)
        
        for i in range(len(s)):
            if counts.get(s[i]) == 1:
                return i
        return -1

if __name__ == '__main__':
    s = Solution()
    print(s.firstUniqChar_1("leetcode")) #returns 0
    print(s.firstUniqChar_2("loveleetcode")) #returns 2
    print(s.firstUniqChar_3("aabb")) #returns -1