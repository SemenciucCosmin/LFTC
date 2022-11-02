from Labs.Lab3Lab4.pythonProject.SymbolTable.DataStructure import BST


def test_add():
    symbol_table = BST("b")
    assert symbol_table.name == "b"
    symbol_table.add_element(symbol_table, "b")
    assert symbol_table.right.name == "b"
    symbol_table.add_element(symbol_table, "a")
    assert symbol_table.left.name == "a"
    symbol_table.add_element(symbol_table.right, "a")
    assert symbol_table.right.left.name == "a"


def test_remove():
    symbol_table = BST("b")
    symbol_table.remove_element(symbol_table, "b")
    assert symbol_table.name == "b"
    symbol_table.add_element(symbol_table, "b")
    symbol_table.add_element(symbol_table, "c")
    symbol_table.add_element(symbol_table, "a")
    symbol_table.add_element(symbol_table, "d")
    assert symbol_table.right.right.right.name == "d"
    symbol_table.remove_element(symbol_table, "d")
    assert symbol_table.right.right.right is None


def test_search():
    symbol_table = BST("b")
    assert symbol_table.search(symbol_table, "b").name == "b"
    symbol_table.add_element(symbol_table, "b")
    assert symbol_table.search(symbol_table, "b").name == "b"
    symbol_table.add_element(symbol_table, "a")
    assert symbol_table.search(symbol_table, "a").name == "a"
    symbol_table.add_element(symbol_table.right, "c")
    assert symbol_table.search(symbol_table, "c").name == "c"


def test_all():
    test_add()
    test_remove()
    test_search()
