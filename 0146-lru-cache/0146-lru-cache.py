class Cache:
    def __init__(self, val: int, key: int):
        self.val = val
        self.key = key
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache_head = Cache(key=-1, val=-1)
        self.caches_map = defaultdict(Cache)
        self.recent_cache = None
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.caches_map:
            return -1
        
        cache = self.caches_map[key]
        
        self._remove(cache)
        self._add(cache)

        return cache.val

    def put(self, key: int, value: int) -> None:
        if key in self.caches_map:
            self._remove(self.caches_map[key])
            
        self._add(Cache(value, key))
        
        if len(self.caches_map) > self.capacity:
            self._remove(self.cache_head.next)

    def _remove(self, cache):
        if cache == self.recent_cache:
            cache.prev.next = None
            if cache.prev == self.cache_head:
                self.recent_cache = None
            else:
                self.recent_cache = cache.prev
        else:
            cache.prev.next = cache.next
            cache.next.prev = cache.prev

        del self.caches_map[cache.key]

    def _add(self, cache):
        if self.recent_cache:
            self.recent_cache.next = cache
            cache.prev = self.recent_cache
            self.recent_cache = cache
        else:
            self.recent_cache = cache
            self.cache_head.next = cache
            cache.prev = self.cache_head
        
        self.caches_map[cache.key] = cache


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)