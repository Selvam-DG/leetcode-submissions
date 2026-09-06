class Node:
    def __init__(self, key, val, next= None, prev= None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = Node(-1,-1)
        self.tail = Node(-1,-1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.hmap = dict()
        

    def get(self, key: int) -> int:
        if key not in self.hmap:
            return -1
        node = self.hmap[key]
        self.remove(node)
        self.move2Front(node)
        return node.val
        

    def put(self, key: int, value: int) -> None:
        
        if key in self.hmap:
            node = self.hmap[key]
            node.val = value
            self.remove(node)
            self.move2Front(node)
            return
        new_node = Node(key,value)
        self.hmap[key] = new_node
        self.move2Front(new_node)
        
        if len(self.hmap)>self.capacity:
            least_recent_node = self.tail.prev
            self.remove(least_recent_node)
            del self.hmap[least_recent_node.key]
        
        return
        
    def move2Front(self, node):
        temp = self.head.next
        self.head.next = node
        node.next = temp
        node.prev = self.head
        temp.prev = node

    
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)