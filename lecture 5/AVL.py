from BST import BST


def height(node):
    if node is None:
        return -1
    else:
        return node.height


def update_height(node):
    node.height = max(height(node.left), height(node.right)) + 1


class AVl(BST):
    def left_rotate(self, x):
        y = x.right
        y.parent = x.parent
        if y.parent is None:
            self.root = y
        else:
            if y.parent.left is x:
                y.parent.left = y
            elif y.parent.right is x:
                y.parent.right = y
        x.right = y.left
        if x.right is not None:
            x.right.parent = x
        y.left = x
        x.parent = y
        update_height(x)
        update_height(y)

    def right_rotate(self, x):
        y = x.left
        y.parent = x.parent
        if y.parent is None:
            self.root = y
        else:
            if y.parent.left is x:
                y.parent.left = y
            elif y.parent.right is x:
                y.parent.right = x
        x.left = y.right
        if x.left is not None:
            x.left.parent = x
        y.right = x
        x.parent = y
        update_height(x)
        update_height(y)

    def rebalance(self, node):
        while node is not None:
            update_height(node)
            if height(node.left) > height(node.right) + 1:
                if height(node.left.right) > height(node.left.left) + 1:
                    self.left_rotate(node.left)
                    self.right_rotate(node)
                else:
                    self.right_rotate(node)
            elif height(node.right) > height(node.left) + 1:
                if height(node.right.left) > height(node.right.right) + 1:
                    self.right_rotate(node.right)
                    self.left_rotate(node)
                else:
                    self.left_rotate(node)
            node = node.parent

    def insert(self, k):
        node = super(AVl, self).insert(k)
        self.rebalance(node)

    def delete(self, k):
        node = super(AVl, self).delete(k)
        self.rebalance(node)
