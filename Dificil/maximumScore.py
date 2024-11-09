class Solution(object):
    def maximumScore(self, nums, multipliers):
        n, m = len(nums), len(multipliers)
        dp = [[0] * (m + 1) for _ in range(m + 1)]

        for i in range(m - 1, -1, -1):
            for l in range(i, -1, -1):
                mult = multipliers[i]
                dp[i][l] = max(
                    mult * nums[l] + dp[i + 1][l + 1],  
                    mult * nums[n - 1 - (i - l)] + dp[i + 1][l]  
                )
        
        return dp[0][0]
