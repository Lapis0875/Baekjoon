from sys import stdin
from typing import Final, Generic, Optional, TypeVar

T = TypeVar("T")

class Node(Generic[T]):
    """이진 트리의 노드 클래스. """
    
    __slots__ = ("data", "left", "right")
    
    data: T
    left: Optional["Node[T]"]
    right: Optional["Node[T]"]
    
    def __init__(self, data: T, left: Optional["Node[T]"] = None, right: Optional["Node[T]"] = None):
        self.data = data
        self.left = left
        self.right = right
    
    def isLeaf(self) -> bool:
        return self.left is None and self.right is None

    def __str__(self) -> str:
        return str(self.data)

class BinaryTree(Generic[T]):
    """이진 트리"""
    
    __slots__ = ("root", )
    
    root: Node[T]
    
    def __init__(self, root: Node[T]):
        self.root = root
    
    def preorder(self, node: Node[T]):
        print(node, end="")
        if node.left is not None:
            self.preorder(node.left)
        if node.right is not None:
            self.preorder(node.right)
    
    def inorder(self, node: Node[T]):
        if node.left is not None:
            self.inorder(node.left)
        print(node, end="")
        if node.right is not None:
            self.inorder(node.right)
    
    def postorder(self, node: Node[T]):
        if node.left is not None:
            self.postorder(node.left)
        if node.right is not None:
            self.postorder(node.right)
        print(node, end="")


N: Final[int] = int(stdin.readline().strip())
A = Node[str]("A")
nodes: dict[str, Node[str]] = {"A": A}
for _ in range(N):
    parent, left, right = stdin.readline().split()
    if left != ".":
        nodes[parent].left = nodes[left] = Node[str](left)
    if right != ".":
        nodes[parent].right = nodes[right] = Node[str](right)

tree = BinaryTree[str](A)
tree.preorder(A)
print()
tree.inorder(A)
print()
tree.postorder(A)
print()