class Node:
    def __init__(self, key: int):
        self.left: 'Node | None' = None
        self.right: 'Node | None' = None
        self.val: int = key

    def __str__(self, level=0, prefix="Root: ") -> str:
        ret = "\t" * level + prefix + str(self.val) + "\n"
        if self.left:
            ret += self.left.__str__(level + 1, "L--- ")
        if self.right:
            ret += self.right.__str__(level + 1, "R--- ")
        return ret

def insert(node: 'Node | None', key: int) -> Node:
    if node is None:
        return Node(key)
    else:
        if key < node.val:
            node.left = insert(node.left, key)
        else:
            node.right = insert(node.right, key)
    return node

def search(node: 'Node | None', key: int) -> 'Node | None':
    if node is None or node.val == key:
        return node
    if key < node.val:
        return search(node.left, key)
    return search(node.right, key)

def min_value_node(node: Node) -> Node:
    current = node
    while current.left:
        current = current.left
    return current

def max_value_node(node: Node) -> Node:
    current = node
    while current.right:
        current = current.right
    return current

def delete(node: 'Node | None', key: int) -> 'Node | None':
    if not node:
        return node

    if key < node.val:
        node.left = delete(node.left, key)
    elif key > node.val:
        node.right = delete(node.right, key)
    else:
        # Node with only one child or no child
        if not node.left:
            temp = node.right
            node = None
            return temp
        elif not node.right:
            temp = node.left
            node = None
            return temp
        # Node with two children: Get the inorder successor
        temp = min_value_node(node.right)
        node.val = temp.val
        node.right = delete(node.right, temp.val)
    return node

def sum_tree(node: 'Node | None') -> int:
    if node is None:
        return 0
    return node.val + sum_tree(node.left) + sum_tree(node.right)

if __name__ == "__main__":
    # Create BST
    root = Node(5)
    root = insert(root, 3)
    root = insert(root, 2)
    root = insert(root, 4)
    root = insert(root, 7)
    root = insert(root, 6)
    root = insert(root, 8)

    print("BST structure:")
    print(root)

    # Search for a value
    val = 4
    result = search(root, val)
    if result:
        print(f"Value {val} found in the tree.")
    else:
        print(f"Value {val} not found in the tree.")

    # Delete a value
    root = delete(root, 7)
    print("\nBST after deleting 7:")
    print(root)

    # Task 1: find the maximum value in the tree
    max_node = max_value_node(root)
    print(f"Maximum value in the tree: {max_node.val}")

    # Task 2: Find the minimum value in the tree
    min_node = min_value_node(root)
    print(f"Minimum value in the tree: {min_node.val}")

    # Task 3: Find the sum of all values in the tree
    total_sum = sum_tree(root)
    print(f"Sum of all values in the tree: {total_sum}")