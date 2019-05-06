class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        # LRU 的大小
        self.capacity = capacity
        # LRU 当前的大小
        self.size = 0
        # root 指向下一个要被删除的node
        self.root = Node(-1,-1)
        # 记录一个被访问的node 顺序， tail指向上一次被访问的节点，新节点就插入在这里
        self.tail = self.root
        # hash<key, node> 记录所有node
        self.entryFinder = {}
        
    def get(self, key):
        """
        :rtype: int
        """
        entry = self.entryFinder.get(key)
        if entry == None:
            return -1
        else:
            self.renew(entry)
            return entry.val


    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        entry = self.entryFinder.get(key)
        # 新node
        if entry == None:
            entry = Node(key,value)
            self.entryFinder[key] = entry
            # entry插入tail
            self.tail.next = entry
            entry.prev = self.tail
            self.tail = entry

            # Cache 没有满
            if self.size<self.capacity:
                self.size += 1
            else:
                # cache 已经慢 拿掉LRU
                head = self.root.next
                if head != None:
                    self.root.next = head.next
                    head.next.prev = self.root
                del self.entryFinder[head.key]
        else:
            # 更新val和
            entry.val = value
            self.renew(entry)

    def renew(self,entry):
        # 把entry 重新插入
        if self.tail != entry:
            # remove entry
            prevNode = entry.prev
            nextNode = entry.next
            prevNode.next = nextNode
            nextNode.prev = prevNode
            
            # 把entry插入到tail后面并更新tail
            entry.next = None
            self.tail.next = entry
            entry.prev = self.tail
            self.tail = entry
