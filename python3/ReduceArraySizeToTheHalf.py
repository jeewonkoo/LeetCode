class Solution:
    def minSetSize(self, arr):
        """
        type  arr: List[int]
        rtype int
        """
        count = {}
        size = len(arr)
        for i in arr: 
            count[i] = count.get(i, 0) + 1
        
        min_size = 0
        occur = 0
        for k, v in sorted(count.items(), key=lambda item: item[1], reverse=True):
            if occur >= (size / 2): return min_size
            occur += v
            min_size += 1
            
        return 1

if __name__ == '__main__':
    s = Solution()
    print(s.minSetSize([3,3,3,3,5,5,5,2,2,7])) #prints 2
    print(s.minSetSize([7,7,7,7,7,7])) #prints 1