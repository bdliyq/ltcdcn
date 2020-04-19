class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        q = [[beginWord, 1]]
        while len(q) > 0:
            word, step = q.pop(0)
            if word == endWord:
                return step
            for i in range(len(word)):
                for j in 'abcdefghijklmnopqrstuvwxyz':
                    if word[i] == j:
                        continue
                    t = ''.join([word[:i], j, word[i+1:]])
                    if t in wordList:
                        q.append([t, step+1])
                        wordList.remove(t)
        return 0

if __name__ == '__main__':
    s = Solution()
    print s.ladderLength('hit', 'cog', ["hot","dot","dog","lot","log","cog"])