class Solution:
    def uniqueMorseRepresentations(self, words):
        """
        type words: List[int]
        return int
        """
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        morse_code_set = set()
        
        for word in words:
            morse_code = ""
            for alphabet in word:
                morse_code += morse[(ord(alphabet) - 97)]
            morse_code_set.add(morse_code)
        
        return len(morse_code_set)
        
if __name__ == '__main__':
    s = Solution()
    print(s.uniqueMorseRepresentations(["gin","zen","gig","msg"])) #prints 2
    print(s.uniqueMorseRepresentations(["a"])) #prints 1