class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        # Sliding Window with Bit Manipulation
        def add_right(window_OR, num):
            window_OR = num | window_OR
            i = 0
            # Update bit count for each bit position in num.
            while num:
                bit_count[i] += num % 2 # Add num's LSB to count. 1 if LSB == 1 else 0.
                num >>= 1 # Check next bit. LSB to MSB.
                i += 1
            return window_OR

        def remove_left(window_OR, num):
            i = 0
            while num:
                bit_count[i] -= num % 2 
                # If count drops to zero and num's LSB == 1, update window.
                if bit_count[i] == 0 and num % 2 == 1:
                    window_OR = window_OR ^ (1 << i) # Undo OR operation.
                num >>= 1
                i += 1
            return window_OR

        bit_count = [0] * 32
        window_OR = 0
        shortest = float('inf')
        left, right = 0, 0

        while right < len(nums):
            window_OR = add_right(window_OR, nums[right])

            while left <= right and window_OR >= k:
                shortest = min(shortest, right - left + 1)
                window_OR = remove_left(window_OR, nums[left])
                left += 1

            right += 1

        return shortest if shortest != float('inf') else -1

        # O(n) time.
        # O(1) space.