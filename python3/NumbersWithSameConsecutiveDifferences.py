class Solution:
    def numsSameConsecDiff(self, n: int, k: int):
        output = []
        def recurse(curr):
            if len(curr) == n:
                output.append(int("".join(map(str, curr))))
                return
            last_digit = curr[-1]
            if 0 <= last_digit + k <= 9:
                recurse(curr + [last_digit+k])
            if 0 <= last_digit - k <= 9:
                recurse(curr + [last_digit-k])
            
        for i in range(1, 10):
            recurse([i])
        return set(output)