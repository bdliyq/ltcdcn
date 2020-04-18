class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        res = 0
        left, right = 0, len(height)-1
        while left < right:
            if height[left] <= height[right]:
                sec_height = height[left]
                res = max(res, sec_height * (right-left))
                left += 1
            else:
                sec_height = height[right]
                res = max(res, sec_height * (right-left))
                right -= 1
        return res

if __name__ == '__main__':
    s = Solution()
    print s.maxArea([1,8,6,2,5,4,8,3,7])