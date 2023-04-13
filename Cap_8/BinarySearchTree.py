class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def __str__(self):
        if self.root is None:
            return '<empty>'
        return str(self.root)
    
    def __find(self, k, node, deepest):
        if node is None:
            return deepest
        if k < node.key:
            return self.__find(k, node.left, deepest)
        elif k > node.key:
            return self.__find(k, node.right, deepest)
        else:
            if deepest is None or node.depth > deepest.depth:
                deepest = node
            return self.__find(k, node.right, deepest)
        
    def search(self, k, shallowest=False):
        node = self.__find(k, self.root, None)
        if shallowest:
            while node is not None and node.left is not None and node.left.key == k:
                node = node.left
        return node
    
    def insert(self, k, v):
        node = self.search(k, shallowest=True)
        if node is not None and node.key == k:
            while node.left is not None:
                node = node.left
            node.left = BinarySearchTree.Node(k, v, node.depth+1)
        else:
            self.root = self.__insert(k, v, self.root, 0)
    
    def __insert(self, k, v, node, depth):
        if node is None:
            return BinarySearchTree.Node(k, v, depth)
        if k < node.key:
            node.left = self.__insert(k, v, node.left, depth+1)
        elif k > node.key:
            node.right = self.__insert(k, v, node.right, depth+1)
        return node
    
    def delete(self, k):
        node = self.search(k)
        if node is None:
            return
        if node.left is not None:
            node.left = self.__delete(node.left)
        else:
            self.root = self.__delete(self.root)
        
    def __delete(self, node):
        if node.right is not None:
            node.right = self.__delete(node.right)
            return node
        else:
            return node.left
    
    class Node:
        def __init__(self, k, v, d):
            self.key = k
            self.value = v
            self.depth = d
            self.left = None
            self.right = None
        
        def __str__(self):
            return (f'{self.left}' if self.left is not None else '') + \
                f'{self.key}:{self.value}:{self.depth}' + \
                (f',{self.right}' if self.right is not None else '')
