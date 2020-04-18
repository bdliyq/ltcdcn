class Solution(object):
    def suggestedProducts(self, products, searchWord):
        """
        :type products: List[str]
        :type searchWord: str
        :rtype: List[List[str]]
        """
        tree = TrieTree(products)
        res = []
        for i in range(len(searchWord)):
            res.append(tree.search(searchWord[:i+1]))
        return res

class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.values = []

class TrieTree(object):
    def __init__(self, products):
        self.root = TrieNode()
        for p in products:
            node = self.root
            for c in p:
                if node.children.has_key(c):
                    node.children[c].values.append(p)
                    node.children[c].values = sorted(node.children[c].values)
                    if len(node.children[c].values) > 3:
                        node.children[c].values = node.children[c].values[:3]
                else:
                    node.children[c] = TrieNode()
                    node.children[c].values.append(p)
                node = node.children[c]

    def search(self, word):
        node = self.root
        for c in word:
            if node.children.has_key(c):
                node = node.children[c]
            else:
                return []
        return node.values

if __name__ == '__main__':
    s = Solution()
    print s.suggestedProducts(["mobile","mouse","moneypot","monitor","mousepad"], 'mouse')

