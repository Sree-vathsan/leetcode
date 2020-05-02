"""
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

The cache is initialized with a positive capacity.

Follow up:
Could you do both operations in O(1) time complexity?

Example:

LRUCache cache = new LRUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4
"""
 
        
class LRUCache:        
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.curr_size = 0
        self.dl_head = self.Node(-1, None, None)
        self.dl_tail = self.Node(-1, self.dl_head, None)
        self.dl_head.right_ptr = self.dl_tail
        self.cache = {}
    
    class Node:
        def __init__(self, val: int, left_ptr, right_ptr):
            self.val = val
            self.left_ptr = left_ptr
            self.right_ptr = right_ptr 
    
    def _move_to_head(self, node, is_exist = False):
        if is_exist:
            left = node.left_ptr
            right = node.right_ptr
            left.right_ptr = right
            right.left_ptr = left
            node.right_ptr = self.dl_head.right_ptr
            node.left_ptr = self.dl_head
        self.dl_head.right_ptr.left_ptr = node
        self.dl_head.right_ptr = node
        
    
    def _remove_last(self):
        last_node = self.dl_tail.left_ptr
        self.dl_tail.left_ptr = last_node.left_ptr
        last_node.left_ptr.right_ptr = self.dl_tail
        return last_node.val
    
    def get(self, key: int) -> int:
        if key in self.cache:
            self._move_to_head(self.cache[key][1], True)
            return self.cache[key][0]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Key already present, not clear if we should check for val and move to front!
            _, old_node = self.cache[key]
            self._move_to_head(old_node, True)
            self.cache[key] = (value, old_node)
            return
        
        if self.curr_size == self.capacity:
            # Reached capacity
            key_to_remove = self._remove_last()
            if key_to_remove in self.cache:
                self.cache.pop(key_to_remove)
        else:
            self.curr_size += 1
        # Add and move to front
        new_node = self.Node(key, self.dl_head, self.dl_head.right_ptr)
        self._move_to_head(new_node)
        self.cache[key] = (value, new_node) 
            


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
