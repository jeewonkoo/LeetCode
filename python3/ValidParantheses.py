class Solution:
    def isValid(self, s):
        """
        type s: str
        rtype: bool
        """
        
        # use dictionary since lookup for dictionary is O(1) but list is O(n)
        mapping = {"(":")", "{":"}", "[":"]"}
        
        # use stack to store open parantheses
        stack = []
        
        # iterate parantheses is s
        for i in s:
            # if paranthese is open parantheses, append it to stack
            if i in mapping.keys(): stack.append(i)
            #if paranthese is close parantheses
            else:
                # if there stack is empty, it means there are no open parantheses. 
                # Therefore, cannot make valid parantheses. Return False
                if not stack: return False\
                # if close paranthese is not equal to value of last element of stack, 
                # it means it is not valid parantheses. Return False
                if i != mapping[stack[-1]]: 
                    return False
                #if they are equal, it means valid parantheses. 
                # Therefore, pop open parantheses as we already checked. 
                else: stack.pop()
        # Since there are extra open parantheses in s, if length of stack is not equal to 0, return False
        # else, return True. 
        # If length of stack is equal to 0, it means all open parantheses have checked and 
        # have appropriate close parantheses
        return len(stack) == 0
            
if __name__ == '__main__':
    s = Solution()
    print(s.isValid("()"))
    print(s.isValid("()[]{}"))
    print(s.isValid("(]"))
    print(s.isValid("("))
    print(s.isValid("]"))