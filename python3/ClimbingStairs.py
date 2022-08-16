class Solution:

    # Naive Solution - Time Limit Exceeded 
    def climbStairs_1(self, n: int) -> int:
        if n == 1: return 1
        if n == 2 : return 2
        return self.climbStairs_1(n-1)+self.climbStairs_1(n-2)

    #Memoization - recursively call helper function 
    def climbStairs_2(self, n: int) -> int:
        step_table = {}
        step_table[0] = 0
        step_table[1] = 1
        step_table[2] = 2
        
        def get_step(n: int) -> int:
            if n in step_table:
                return step_table[n]
            step_table[n] = get_step(n-2) + get_step(n-1)
            return step_table[n]
        
        return get_step(n)
	
    #Dynamic Programming - List
    def climbStairs_3(self, n: int) -> int:
        if n == 0 :return 0
        if n == 1: return 1
        if n == 2: return 2

        d = [0] * (n+1)
        d[1] = 1				
        d[2] = 2
        for i in range(3, n+1):
            d[i] = d[i-1] + d[i-2]
        return d[n]

    #Dynamic Programming - Dictionary
    def climbStairs_4(self, n: int) -> int:
        d= {0:0, 1:1, 2:2}
        for i in range(3, n+1):
            d[i] = d[i-1] + d[i-2]
        return d[n]
	
    #Dynamic Programming 
    def climbStairs_5(self, n: int) -> int:
        a, b = 1, 1
        for i in range(n):
            a, b = b, a + b
        return a
    #a, b = 1, 2
    #a, b = 2, 3
    #a, b = 3, 5

if __name__ == '__main__':
    s = Solution()
    # All prints 1836311903
    # print(s.climbStairs_1(45)) TLE
    print(s.climbStairs_2(45))
    print(s.climbStairs_3(45))
    print(s.climbStairs_4(45))
    print(s.climbStairs_5(45))
