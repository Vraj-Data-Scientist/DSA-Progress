class LRUcache:
    class Node:
        def __init__(self, key, val):
            self.key = key
            self.val = val
            self.next = None
            self.prev = None
    def __init__(self, capacity):
        self.head = self.Node(-1,-1)
        self.tail = self.Node(-1,-1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.cap = capacity
        self.dict1 = {}
    def insert_after_head(self, node):
        temp = self.head.next
        node.next = temp
        node.prev = self.head
        self.head.next = node
        temp.prev = node
    def delete_node(self, node):
        back = node.prev
        front = node.next
        front.prev = back
        back.next = front
    def get(self, key):
        if (key not in self.dict1):
            return -1
        node = self.dict1[key]
        self.delete_node(node)
        self.insert_after_head(node)
        return node.val
    def put(self, key, val):
        if (key in self.dict1):
            node = self.dict1[key]
            node.val = val
            self.delete_node(node)
            self.insert_after_head(node)
        else:
            if (len(self.dict1) == self.cap):
                node = self.tail.prev
                del self.dict1[node.key]
                self.delete_node(node)
            node = self.Node(key, val)
            self.dict1[key] = node
            self.insert_after_head(node)



cache = LRUcache(2)


cache.put(1, 1)
cache.put(2, 2)

print(cache.get(1))

cache.put(3, 3)

print(cache.get(2))

cache.put(4, 4)

print(cache.get(1))

print(cache.get(3))

print(cache.get(4))
