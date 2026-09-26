class ListNode:
    def __init__(self, key: int, val: int = 0, prev = None, next = None):
        self.prev = prev
        self.val = val
        self.key = key
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.head = None
        self.lastHead = None

    def get(self, key: int) -> int:

        if key in self.cache:
            
            current = self.cache[key]

            if current == self.head and len(self.cache) == 1:
                return current.val

            elif current == self.head and len(self.cache)>1:
                current.next.prev = None
                current = current.next
                self.head = current
                self.lastHead.next = self.cache[key]
                self.lastHead.next.prev = self.lastHead
                self.lastHead = self.lastHead.next
                self.lastHead.next = None
                return self.cache[key].val
            
            elif current == self.lastHead:
                return current.val
            
            else:
                current.prev.next = current.next
                current.next.prev = current.prev
                self.lastHead.next = self.cache[key]
                self.lastHead.next.prev = self.lastHead
                self.lastHead = self.lastHead.next
                self.lastHead.next = None
                return self.cache[key].val
        
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:

        if key in self.cache:
                self.cache[key].val = value
                self.get(key)
                return
        
        if len(self.cache) < self.capacity:

            self.cache[key] = ListNode(key=key, val=value)

            if self.head == None and self.lastHead == None:

                self.head = self.cache[key]
                self.lastHead = self.cache[key]
                return

            self.lastHead.next = self.cache[key]
            self.lastHead.next.prev = self.lastHead
            self.lastHead = self.lastHead.next

        else:

            if self.capacity == 1:
                del self.cache[self.head.key]
                
                self.cache[key] = ListNode(key=key, val=value)

                self.head = self.cache[key]
                self.lastHead = self.cache[key]
            
            else:

                current = self.head
                self.head = self.head.next
                self.head.prev = None

                del self.cache[current.key]

                self.cache[key] = ListNode(key=key, val=value)

                self.lastHead.next = self.cache[key]
                self.lastHead.next.prev = self.lastHead
                self.lastHead = self.lastHead.next 