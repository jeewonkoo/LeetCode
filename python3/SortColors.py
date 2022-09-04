class Solution:
    def sortColors_naive(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        count = {}
        for i in nums:
            count[i] = count.get(i, 0) + 1
        idx_count = 0

        for i in sorted(count.items()):
            for j in range(i[1]):
                nums[idx_count] = i[0]
                idx_count += 1
    
    def sortColors_dutch_partitioning(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        red_pointer, white_pointer, blue_pointer = 0, 0, len(nums)-1
        
        while white_pointer <= blue_pointer:
            if nums[white_pointer] == 0: 
                nums[white_pointer], nums[red_pointer] = nums[red_pointer], nums[white_pointer]
                white_pointer +=1
                red_pointer +=1 
            
            elif nums[white_pointer] == 1:
                white_pointer +=1
                
            else: 
                nums[white_pointer], nums[blue_pointer] = nums[blue_pointer], nums[white_pointer]
                blue_pointer -= 1