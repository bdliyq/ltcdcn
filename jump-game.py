class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        max_dist = 0
        for i, n in enumerate(nums):
            if i > max_dist or max_dist >= len(nums)-1:
                break
            max_dist = max(max_dist, n + i)
        return max_dist >= len(nums)-1

if __name__ == '__main__':
    s = Solution()
    print s.canJump([0,2,3])