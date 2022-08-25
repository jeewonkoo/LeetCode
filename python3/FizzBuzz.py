class Solution:
    def fizzBuzz(self, n):
        """
        type n: int
        rtype List[str]
        """
        answer = []
        for i in range(1, n+1):
            if i % 3 == 0 and i % 5 == 0: answer.append("FizzBuzz")
            elif i % 3 == 0: answer.append("Fizz")
            elif i % 5 == 0: answer.append("Buzz")
            else: answer.append(str(i))
            
        return answer
    
if __name__ == '__main__': 
    s = Solution()
    print(s.fizzBuzz(3))
    print(s.fizzBuzz(5))
    print(s.fizzBuzz(15))