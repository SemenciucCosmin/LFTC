from DataStructure import BST


class SymbolTable:
    def __init__(self):
        self.identifiers = BST(None)
        self.constants = BST(None)
