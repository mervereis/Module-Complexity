
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LruCache:
    def __init__(self, limit):
        if limit <= 0:
            raise ValueError("Limit must be greater than 0")

        self.limit = limit
        self.cache = {}

        self.head = Node(None, None)
        self.tail = Node(None, None)

        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def _add_to_head(self, node):
        node.next = self.head.next
        node.prev = self.head

        self.head.next.prev = node
        self.head.next = node

    def get(self, key):
        if key not in self.cache:
            return None

        node = self.cache[key]

        self._remove(node)
        self._add_to_head(node)

        return node.value

    def set(self, key, value):
        if key in self.cache:
            node = self.cache[key]
            node.value = value

            self._remove(node)
            self._add_to_head(node)
        else:
            node = Node(key, value)
            self.cache[key] = node
            self._add_to_head(node)

            if len(self.cache) > self.limit:
                lru_node = self.tail.prev
                self._remove(lru_node)
                del self.cache[lru_node.key]
