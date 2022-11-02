from Labs.Lab3Lab4.pythonProject.SymbolTable.DataStructure import BST


class SymbolTable:
    def __init__(self):
        self.identifiers = BST(None)
        self.constants = BST(None)
