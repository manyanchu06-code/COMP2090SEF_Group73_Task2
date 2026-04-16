from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self, root_val=None):
        if root_val is not None:
            self.root = TreeNode(root_val)
        else:
            self.root = None

    def build_example(self):
        self.root = TreeNode(1)
        self.root.left = TreeNode(2)
        self.root.right = TreeNode(3)
        self.root.left.left = TreeNode(4)
        self.root.left.right = TreeNode(5)
        self.root.right.right = TreeNode(6)

    def preorder(self):
        return list(self._preorder(self.root))

    def inorder(self):
        return list(self._inorder(self.root))

    def postorder(self):
        return list(self._postorder(self.root))

    def level_order(self):
        if not self.root:
            return []
        queue = deque([self.root])
        result = []
        while queue:
            node = queue.popleft()
            result.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return result

    def _preorder(self, node):
        if node:
            yield node.val
            yield from self._preorder(node.left)
            yield from self._preorder(node.right)

    def _inorder(self, node):
        if node:
            yield from self._inorder(node.left)
            yield node.val
            yield from self._inorder(node.right)

    def _postorder(self, node):
        if node:
            yield from self._postorder(node.left)
            yield from self._postorder(node.right)
            yield node.val

if __name__ == "__main__":
    bt = BinaryTree()
    bt.build_example()
    print("Pre-order :", bt.preorder())
    print("In-order  :", bt.inorder())
    print("Post-order:", bt.postorder())
    print("Level-order:", bt.level_order())
