class Node:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev: Node | None = None
        self.next: Node | None = None

class LRUCache:

    def __init__(self, capacity: int):
        self.size = 0
        self.capacity = capacity
        self.cache: dict[int:Node] = {}
        #Creating dummy head and tail
        self.head = Node()
        self.tail = Node()

        #Connecting dummy head and tail
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove_node(node)
            self.addedtohead(node)
            return node.value
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            self.remove_node(node)
            node.value = value
            self.addedtohead(node)
        else:
            new_node = Node(key, value)
            self.cache[key] = new_node
            self.addedtohead(new_node)
            self.size += 1
            
            if self.size > self.capacity:
                lrunode = self.tail.prev
                self.cache.pop(lrunode.key)
                self.remove_node(lrunode)
                self.size -= 1

    def remove_node(self,node):
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def addedtohead(self,node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)