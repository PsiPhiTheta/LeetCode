class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.oDic = collections.OrderedDict()
        self.cap = capacity

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.oDic:
            self.oDic.move_to_end(key) # update position in cache (since used)
            return self.oDic[key]
        else:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.oDic:
            del self.oDic[key]
            self.oDic[key] = value # update value
        else:
            if len(self.oDic) == self.cap:
                self.oDic.popitem(False) # remove least recently used (furthest from end)
            self.oDic[key] = value # write new

        
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
