class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None
        self.cnt = 1

class LinkedList:
    def __init__(self):
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def add_front(self, node):
        temp = self.head.next
        node.next = temp
        node.prev = self.head
        self.head.next = node
        temp.prev = node
        self.size += 1

    def remove_node(self, node):
        front = node.next
        back = node.prev
        front.prev = back
        back.next = front
        self.size -= 1

class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.curr_size = 0
        self.min_freq = 0
        self.key_node_map = {}
        self.freq_ll_map = {}

    def update_freq_ll_map(self, node):
        del self.key_node_map[node.key]
        self.freq_ll_map[node.cnt].remove_node(node)
        if (node.cnt == self.min_freq and self.freq_ll_map[node.cnt].size == 0):
            self.min_freq += 1
        next_higher_freq_ll = LinkedList()
        if ((node.cnt + 1) in self.freq_ll_map):
            next_higher_freq_ll = self.freq_ll_map[node.cnt + 1]
        node.cnt += 1
        next_higher_freq_ll.add_front(node)
        self.freq_ll_map[node.cnt] = next_higher_freq_ll
        self.key_node_map[node.key] = node

    def get(self, key: int) -> int:
        if (key in self.key_node_map):
            node = self.key_node_map[key]
            val = node.val
            self.update_freq_ll_map(node)
            return val
        return -1

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        if (key in self.key_node_map):
            node = self.key_node_map[key]
            node.val = value
            self.update_freq_ll_map(node)
        else:
            if (self.curr_size == self.capacity):
                LL = self.freq_ll_map[self.min_freq]
                del self.key_node_map[LL.tail.prev.key]
                self.freq_ll_map[self.min_freq].remove_node(LL.tail.prev)
                self.curr_size -= 1
            self.curr_size += 1
            self.min_freq = 1
            LL_freq = LinkedList()
            if (self.min_freq in self.freq_ll_map):
                LL_freq = self.freq_ll_map[self.min_freq]
            node = Node(key, value)
            LL_freq.add_front(node)
            self.key_node_map[key] = node
            self.freq_ll_map[self.min_freq] = LL_freq

cache = LFUCache(2)

cache.put(1, 1)
cache.put(2, 2)
print(cache.get(1), end=" ")
cache.put(3, 3)
print(cache.get(2), end=" ")
print(cache.get(3), end=" ")
cache.put(4, 4)
print(cache.get(1), end=" ")
print(cache.get(3), end=" ")
print(cache.get(4), end=" ")