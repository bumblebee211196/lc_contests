class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        l = r = groups = 0

        # Sort the elements
        nums = sorted(nums)
        
        while r < n:
            # Move right pointer until the difference between the left and the right pointer is <= k
            if nums[r] - nums[l] <= k:
                r += 1
            # Update the group count and the left pointer
            else:
                groups += 1
                l = r
        
        return groups + 1
                