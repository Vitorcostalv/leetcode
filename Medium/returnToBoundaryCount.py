class Solution(object):
    def returnToBoundaryCount(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        position = 0
        boundary_count = 0

        for step in nums:
            position += step
            if position == 0:
                boundary_count += 1

        return boundary_count

solution = Solution()
print(solution.returnToBoundaryCount([2, 3, -5]))  # Output: 1
print(solution.returnToBoundaryCount([3, 2, -3, -4]))  # Output: 0
