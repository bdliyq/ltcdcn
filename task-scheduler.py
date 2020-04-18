import heapq
class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """

        tasks_count = {}
        for t in tasks:
            if tasks_count.has_key(t):
                tasks_count[t] += 1
            else:
                tasks_count[t] = 1

        h = []
        for k, v in tasks_count.items():
            heapq.heappush(h, (-v, k))

        res = 0
        while len(h) > 0:
            tmp = []
            for i in range(n+1):
                if len(h) > 0:
                    t = heapq.heappop(h)
                    if -t[0] > 1:
                        tmp.append((-(-t[0]-1), t[1]))
                res += 1
                if len(h) == 0 and len(tmp) == 0:
                    break
            for t in tmp:
                heapq.heappush(h, t)

        return res

if __name__ == '__main__':
    s = Solution()
    print s.leastInterval(["A","A","A","A","A","A","B","C","D","E","F","G"], 2)