class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        self.helper(n, n, '', res)
        return res

    def helper(self, left, right, path, res):
        if left == 0 and right == 0:
            res.append(path)
        elif left < right:
            if left > 0:
                self.helper(left-1, right, path+'(', res)
            if right > 0:
                self.helper(left, right-1, path+')', res)
        elif left == right:
            if left > 0:
                self.helper(left-1, right, path+'(', res)

if __name__ == '__main__':
    s = Solution()
    print s.generateParenthesis(3)