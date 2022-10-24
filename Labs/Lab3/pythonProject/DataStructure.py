class BST:
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None

    def add_element(self, root, name):
        if root is None:
            return BST(name)

        if root.name is not None:
            if name < root.name:
                root.left = self.add_element(root.left, name)
            else:
                root.right = self.add_element(root.right, name)
        else:
            root.name = name

        return root

    @staticmethod
    def min_value_element(element):
        current = element

        while current.left is not None:
            current = current.left

        return current

    def remove_element(self, root, name):

        if root is None:
            return root

        if name < root.name:
            root.left = self.remove_element(root.left, name)

        elif name > root.name:
            root.right = self.remove_element(root.right, name)

        else:

            if root.left is None:
                return root.right

            elif root.right is None:
                return root.left

            root.name = self.min_value_element(root.right).name
            root.right = self.remove_element(root.right, root.name)

        return root

    def print_elements(self):
        if self.left:
            self.left.print_elements()
        print(self.name),
        if self.right:
            self.right.print_elements()

    def inorder_traversal(self, root):
        elements = []
        if root:
            elements = self.inorder_traversal(root.left)
            elements.append(root.name)
            elements = elements + self.inorder_traversal(root.right)
        return elements

    def search(self, root, name):
        if root is None:
            return False

        if name < root.name:
            return self.search(root.left, name)
        elif name > root.name:
            return self.search(root.right, name)
        else:
            return True
