class Solution:
    def longestCommonPrefix(self, strs):
        min_length_word = min(strs, key=len)
        prefix = len(min_length_word)
        i = 0
        while i < len(strs):
            if strs[i][:prefix] != min_length_word[:prefix]:
                prefix -= 1
                i = 0
            else: i +=1 
            # print(prefix)
        return strs[0][:prefix]