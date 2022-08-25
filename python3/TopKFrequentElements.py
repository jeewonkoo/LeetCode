class Solution:
    def topKFrequent(self, nums, k):
        """
        type nums: : List[int], k: int
        rtype: List[int]
        """
        frequency = {}
        
        for i in nums:
            frequency[i] = frequency.get(i, 0) + 1
        
        sorted_frequency = sorted(frequency.items(), key=lambda item:item[1], reverse=True)
        top_k_frequency = [i[0] for i in sorted_frequency]
        return top_k_frequency[:k]

if __name__ == '__main__':
    s = Solution()
    print(s.topKFrequent([1,1,1,2,2,3], 2)) #prints [1,2]
    print(s.topKFrequent([1], 1))    #prints 1