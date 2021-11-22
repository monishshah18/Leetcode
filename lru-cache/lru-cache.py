class LRUCache:

    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.remaining = capacity  

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        v = self.cache.pop(key)
        self.cache[key] = v
        return v
    
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.pop(key)
        else:
            if self.remaining > 0:
                self.remaining -= 1
            else:
                self.cache.popitem(last=False)
        self.cache[key] = value    


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)