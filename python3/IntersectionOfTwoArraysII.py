class Solution:
    def intersect(self, nums1, nums2):
        seen = {}
        output = []
        is_nums1_longer = True if len(nums1) >= len(nums2) else False
        
        if is_nums1_longer:
            for i in nums1:
                seen[i] = seen.get(i, 0) + 1
        else: 
            for i in nums2: 
                seen[i] = seen.get(i, 0) + 1

        if is_nums1_longer: 
            for i in nums2:
                if i in seen and seen[i]:
                    seen[i] -= 1
                    output.append(i)
        else: 
            for i in nums1:
                if i in seen and seen[i]:
                    seen[i] -= 1
                    output.append(i)
        return output