class BSTNode:
    def __init__(self, key, left=None, right=None, parent=None):
        self.key = key
        self.left = left
        self.right = right
        self.parent = parent

    def find_min(self):
        current = self
        while self.left is not None:
            current = self.left
        return current

    def find(self, k):
        if self.key == k:
            return self
        elif self.key < k:
            if self.right is None:
                return None
            else:
                return self.right.find(k)
        elif self.key > k:
            if self.left is None:
                return None
            else:
                return self.left.find(k)

    def next_largest(self):
        if self.right is not None:
            return self.right.find_min()
        current = self
        while current.parent is not None and current is current.parent.right:
            current = current.parent
        return current.parent

    def insert(self, node):
        if node is None:
            raise None
        elif node.key < self.key:
            if self.left is None:
                self.left = node
                node.parent = self
            else:
                self.left.insert(node)
        elif node.key > self.key:
            if self.right is None:
                self.right = node
                node.parent = self
            else:
                self.right.insert(node)

    def delete(self):
        if self.left is None or self.right is None:
            if self is self.parent.left:
                self.parent.left = self.left or self.right
                self.parent.left.parent = self.parent
            else:
                self.parent.right = self.left or self.right
                self.parent.right.parent = self.parent
            return self
        current = self.next_largest()
        self.key, current.key = current.key, self.key
        return current.delete()


class BST:
    def __init__(self):
        self.root = None

    def find(self, k):
        return self.root and self.root.find(k)

    def find_min(self):
        return self.root.find_min()

    def next_larger(self, k):
        current = self.find(k)
        if current is not None:
            return current.next_larger()

    def insert(self, k):
        node = BSTNode(k)
        if self.root is None:
            self.root = node
        else:
            self.root.insert(node)
        return node

    def delete(self, k):
        current = self.find(k)
        if current is self.root:
            psuedonode = BSTNode(0)
            psuedonode.left = self.root
            self.root.parent = psuedonode
            deleted = self.root.delete()
            self.root = psuedonode.left
            if self.root is not None:
                self.root.parent = None
            return deleted
        return current.delete()
