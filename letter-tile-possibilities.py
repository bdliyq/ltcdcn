class Solution(object):
    def numTilePossibilities(self, tiles):
        """
        :type tiles: str
        :rtype: int
        """
        input = list(tiles)
        input.sort()
        res = []
        self.dfs(input, [], [], res)
        return len(res)

    def dfs(self, tiles, prefix, used, res):
        if len(prefix) != 0 and ''.join(prefix) not in res:
            res.append(''.join(prefix))
        for i in range(len(tiles)):
            if i not in used:
                prefix.append(tiles[i])
                used.append(i)
                self.dfs(tiles, prefix, used, res)
                del used[-1]
                del prefix[-1]

if __name__ == '__main__':
    s = Solution()
    print s.numTilePossibilities('AAB')