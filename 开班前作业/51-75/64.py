# 64. Python 实现一条链表，并打印输出链表内的元素内容（元素类型设置为整型即可）

# 链节点类
class ListNode:
    def __init__(self, val:int=0, next=None):
        self.val = val
        self.next = next

# 链表类
class LinkedList:
    def __init__(self):
        self.head = None

    # 根据 data 初始化一个新链表
    def create(self, data):
        self.head = ListNode(0)
        cur = self.head
        for i in range(len(data)):
            node = ListNode(val=data[i])
            cur.next = node
            cur = cur.next

data = [i for i in range(100)]
ll = LinkedList()
ll.create(data)
node = ll.head
for _ in data:
    node = node.next
    print(node.val)