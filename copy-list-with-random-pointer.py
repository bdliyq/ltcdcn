# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random

def print_list(head):
    res = []
    nodes = {}
    node = head
    idx = 0
    while node is not None:
        res.append([node.val, None])
        nodes[node] = idx
        node = node.next
        idx += 1

    node = head
    idx = 0
    while node is not None:
        if node.random is not None:
            res[idx][1] = nodes[node.random]
        idx += 1
        node = node.next

    print res

def create_list(input):
    dummy = Node(0)
    cursor = dummy
    nodes = []

    for item in input:
        node = Node(item[0])
        cursor.next = node
        nodes.append(node)
        cursor = node

    cursor = dummy
    for idx, item in enumerate(input):
        cursor = cursor.next
        if item[1] is not None:
            cursor.random = nodes[item[1]]

    return dummy.next

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        dummy = Node(0)
        node = head
        cursor = dummy
        while node is not None:
            next = node.next
            cursor.next = node
            cursor = cursor.next
            cursor.next = Node(node.val)
            cursor = cursor.next
            node = next

        cursor = dummy.next
        while cursor is not None and cursor.next is not None:
            if cursor.random is not None:
                cursor.next.random = cursor.random.next
            cursor = cursor.next.next

        cursor = dummy
        while cursor is not None and cursor.next is not None:
            oldnext = cursor.next
            newnext = cursor.next.next
            cursor.next = newnext
            cursor = cursor.next
            oldnext.next = cursor.next

        return dummy.next

if __name__ == '__main__':
    head = create_list([[7,None],[13,0],[11,4],[10,2],[1,0]])
    print_list(head)
    s = Solution()
    print_list(s.copyRandomList(head))
    print_list(head)