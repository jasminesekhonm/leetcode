class Solution:
    def search(self, nums: list[int], target: int) -> int:

        n = len(nums)

        l, r = 0, n-1 

        while l <r:
            mid = (l + r) // 2
            left, right = nums[l], nums[r]
            middle = nums[mid]

            if middle > right: ## min is on right side
                l = mid + 1

            else:
                r = mid 

        pivot_index = l 

        shift = n - pivot_index 

        l, r = (pivot_index + shift) % n, (pivot_index + shift - 1) % n 

        while l <= r:
            mid = (l + r) // 2 
            if nums[(mid - shift) % n] == target:
                return (mid - shift) % n
            elif nums[(mid - shift) % n] > target:
                r = mid - 1
            else:
                l = mid + 1

        return -1 
