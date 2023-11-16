class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def lowest_common_ancestor_iterative(root, p, q):
    if not root:
        return None
    left_itr = root
    right_itr = root
    lca = root
    while left_itr.key == right_itr.key:
        lca = left_itr
        if p > left_itr.key:
            left_itr = left_itr.right
        elif p < left_itr.key:
            left_itr = left_itr.left
        if q > right_itr.key:
            right_itr = right_itr.right
        elif q < right_itr.key:
            right_itr = right_itr.left
    return lca


vertices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
edges = [[1, 2], [1, 3], [2, 4], [2, 5], [4, 5], [2, 6], [3, 6], [3, 7], [7, 8], [7, 9], [8, 9], [10, 11]]
visited = []


def breadth_first_search(source, destination):
    queue = [source]

    while queue:
        current_node = queue.pop(0)  # Dequeue the first element (FIFO)
        visited.append(current_node)

        if current_node == destination:
            print("Destination found!")
            return True  # Return True if destination is found

        for edge in edges:
            if edge[0] == current_node and edge[1] not in visited and edge[1] not in queue:
                queue.append(edge[1])

    print("Destination not reachable from source!")
    return False  # Return False if destination is not reachable from the source


#binary search tree
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert_recursive(self.root, key)

    def _insert_recursive(self, root, key):
        if root is None:
            return Node(key)

        if key < root.key:
            root.left = self._insert_recursive(root.left, key)
        elif key > root.key:
            root.right = self._insert_recursive(root.right, key)

        return root

    def search(self, key):
        return self._search_recursive(self.root, key)

    def _search_recursive(self, root, key):
        if root is None or root.key == key:
            return root

        if key < root.key:
            return self._search_recursive(root.left, key)
        else:
            return self._search_recursive(root.right, key)

    def delete(self, key):
        self.root = self._delete_recursive(self.root, key)

    def _delete_recursive(self, root, key):
        if root is None:
            return root

        if key < root.key:
            root.left = self._delete_recursive(root.left, key)
        elif key > root.key:
            root.right = self._delete_recursive(root.right, key)
        else:
            # Node with only one child or no child
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp

            # Node with two children: Get the inorder successor (smallest in the right subtree)
            temp = self._min_value_node(root.right)

            # Copy the inorder successor's content to this node
            root.key = temp.key

            # Delete the inorder successor
            root.right = self._delete_recursive(root.right, temp.key)

        return root

    def _min_value_node(self, root):
        current = root
        while current.left is not None:
            current = current.left
        return current


# Constructing a sample binary tree
if __name__ == "__main__":
    root = TreeNode(45)
    root.left = TreeNode(15)
    root.right = TreeNode(79)
    root.left.left = TreeNode(10)
    root.left.right = TreeNode(20)
    root.right.left = TreeNode(55)
    root.right.right = TreeNode(90)
    root.left.left.right = TreeNode(12)
    root.right.left.left = TreeNode(50)

    # test iterative
    print("testing iterative method")
    result = lowest_common_ancestor_iterative(root, 12, 20)
    print("Lowest Common Ancestor:", result.key)
    result = lowest_common_ancestor_iterative(root, 12, 50)
    print("Lowest Common Ancestor:", result.key)
    result = lowest_common_ancestor_iterative(root, 55, 90)
    print("Lowest Common Ancestor:", result.key)

    source_node = 1
    destination_node = 9
    result = breadth_first_search(source_node, destination_node)
    print(result)
    print("Visited nodes during BFS:", visited)

    visited = []
    source_node = 9
    destination_node = 11
    result = breadth_first_search(source_node, destination_node)
    print(result)
    print("Visited nodes during BFS:", visited)

    visited = []
    source_node = 10
    destination_node = 11
    result = breadth_first_search(source_node, destination_node)
    print(result)
    print("Visited nodes during BFS:", visited)

#tests for  the binary search tree:
    # Example usage:

    bst = BinarySearchTree()
    bst.insert(5)
    bst.insert(3)
    bst.insert(7)
    bst.insert(2)
    bst.insert(4)
    bst.insert(6)
    bst.insert(8)

    print(bst.search(4).key)  # Should print the node with key=4
    bst.delete(4)
    print(bst.search(4))  # Should print None as 4 is deleted