class Node():
    def __init__(self, value):
        self.value = value
        self.next = None

class SingleLinkList(object):
    def __init__(self):
        self._head = None

    def is_empty(self):
        return self._head is None

    def length(self):
        count = 0
        current = self._head
        while current is not None:
            count = count + 1
            current = current.next
        return count

    def items(self):
        current = self._head
        while current is not None:
            yield current.value
            current = current.next

    def insert_head(self, value):
        new_node = Node(value)
        new_node.next = self._head
        self._head = new_node

    def append(self, value):
        new_node = Node(value)
        if self.is_empty():
            self._head = new_node
        else:
            current = self._head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def insert_index(self, index, value):
        if index <= 0:
            self.insert_head(value)
        elif index > (self.length()-1):
            self.append(value)
        else:
            new_node = Node(value)
            current = self._head
            for _ in range(index-1):
                current = current.next
            new_node.next = current.next
            current.next = new_node

    def remove(self, value):
        current = self._head
        pre = None
        while current is not None:
            if current.value == value:
                if not pre:
                    self._head = current.next
                else:
                    pre.next = current.next
                return True
            else:
                pre = current
                current = current.next

    #返回目标值index，无则返回-1
    def find(self, value):
        current = self._head
        count=0
        while current is not None:
            if current.value == value:
                return count
            else:
                current = current.next
                count+=1
        return -1
        #return value in self.items()

    def modify(self, value, new_value):
        index=self.find(value)
        if index==-1:
            return False
        self.remove(value)
        self.insert_index(index,new_value)

if __name__ == "__main__":
    link_list = SingleLinkList()
    node1 = Node(1)
    node2 = Node(2)
    link_list._head = node1
    node1.next = node2
    for i in range(5):
        link_list.append(i)
    link_list.insert_head(10)
    print('顺序构建链表并在头部插入10:',list(link_list.items()))
    link_list.insert_index(3, 20)
    print('index=3的位置插入值20:     ',list(link_list.items()))
    link_list.remove(2)
    print('删除首个value=2的节点:     ',list(link_list.items()))
    link_list.modify(3, -5)
    print('首个value=3的节点值改为-5: ',list(link_list.items()))
    print('查询首个value=4的index为:  ',link_list.find(4))
    print('查询首个value=100的index为:',link_list.find(100))