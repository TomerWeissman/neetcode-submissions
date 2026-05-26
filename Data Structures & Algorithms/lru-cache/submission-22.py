class ListNode:

    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity
        

    def get(self, key: int) -> int:

        if key not in self.cache:
            return -1
        
        val = self.cache[key].val

        self.remove(self.cache[key])
        self.add(self.cache[key])
        print('ran')
        return val

    def put(self, key: int, value: int) -> None:

        if key in self.cache:
            self.remove(self.cache[key])
        new_node = ListNode(key, value)
        self.add(new_node)
        self.cache[key] = new_node

        if len(self.cache) > self.capacity:
            node_to_remove = self.head.next
            self.remove(node_to_remove)
            del self.cache[node_to_remove.key]

    
    def add(self, node):
        prv = self.tail.prev
        prv.next = node
        node.next = self.tail
        self.tail.prev = node
        node.prev = prv

    
    def remove(self, node):
        prv = node.prev
        nxt = node.next
        prv.next = nxt
        nxt.prev = prv



        
