class Node:
    def __init__(self, val: int) -> None:
        self.val = val
        self.npx = 0

class XORLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.size = 0
        self._address_map = {}

    def add(self, val: int) -> None:
        new_node = Node(val)
        self._address_map[id(new_node)] = new_node
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.npx = id(self.tail)
            self.tail.npx ^= id(new_node)
            self.tail = new_node
        self.size += 1

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        current = self.head
        prev_id = 0
        for _ in range(index):
            next_id = prev_id ^ current.npx
            prev_id = id(current)
            current = self._get_node_by_id(next_id)
        return current.val

    def _get_node_by_id(self, node_id: int) -> Node:
        if node_id == 0:
            return None
        return self._address_map.get(node_id, None)

    def _iter_nodes(self):
        current = self.head
        prev_id = 0
        while current:
            yield current
            next_id = prev_id ^ current.npx
            prev_id = id(current)
            current = self._get_node_by_id(next_id)
