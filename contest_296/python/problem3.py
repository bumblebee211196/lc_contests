class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        
        # Initialize the value to index mapper
        idx_mapper = {num : i for i, num in enumerate(nums)}
        
        for u, v in operations:
            # Find the index of u
            idx = idx_mapper[u]
            # Remove u from the index mapper
            idx_mapper.pop(u)
            # Update the new value in nums
            nums[idx] = v
            # Update the new value's index
            idx_mapper[v] = idx
        
        return nums
