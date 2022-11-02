from Labs.Lab3Lab4.pythonProject.SymbolTable.SymbolTable import SymbolTable


class Scanner:
    def __init__(self):
        self.symbol_table = SymbolTable()
        self.output_file = "Scanner/St.out"
        self.token_file = "Tokens/Token.txt"
        self.pif_file = "Pif.txt"
        self.messages = []

    def load_tokens(self):
        self.empty_pif_file()
        file = open(self.token_file, "r")
        lines = file.readlines()
        for line in lines:
            self.symbol_table.constants.add_element(self.symbol_table.constants, line.strip("\n"))

    def scan_file(self, file_name):
        self.messages = []
        pif_file = open(self.pif_file, "a")
        file = open(file_name, "r")
        lines = file.readlines()
        index = 0

        for line in lines:
            line = line.strip("\n")
            line = line.strip("\t")
            identifiers = line.split(" ")
            for identifier in identifiers:
                if not identifier.isupper() and len(identifier) > 2 and self.symbol_table.identifiers.search(self.symbol_table.identifiers, identifier) is False:
                    self.symbol_table.identifiers.add_element(self.symbol_table.identifiers, identifier)

        for line in lines:
            index += 1
            index2 = 0
            line = line.strip("\n")
            line = line.strip("\t")

            for character in line:
                if character != " ":
                    if self.symbol_table.constants.search(self.symbol_table.constants, character) is False:
                        self.add_error_message(character, index, index2)
                    elif not character.isalpha() and not character.isdigit():
                        pif_file.write(self.get_pif_message(character, self.symbol_table.constants))
                index2 += 1

            index2 = 0
            constants = line.split(" ")

            for constant in constants:
                if constant.isupper():
                    if constant.isalpha():
                        if not self.symbol_table.constants.search(self.symbol_table.constants, constant):
                            self.add_error_message(constant, index, index2)
                        else:
                            pif_file.write(self.get_pif_message(constant, self.symbol_table.constants))
                else:
                    if self.symbol_table.identifiers.search(self.symbol_table.identifiers, constant) is True:
                        pif_file.write(self.get_pif_message(constant, self.symbol_table.identifiers))

                index2 += 1

        if len(self.messages) == 0:
            self.messages.append("\tLexically correct\n")

        self.write_message(file_name)

    def write_message(self, file_name):
        file = open(self.output_file, "a")
        file.write("\nFILE: " + file_name + "\n")
        for message in self.messages:
            file.write(message)
        file.close()

    def empty_output_file(self):
        file = open(self.output_file, "w")
        file.write("")

        file.close()

    def empty_pif_file(self):
        file = open(self.pif_file, "w")
        file.write("")
        file.close()

    def add_error_message(self, character, line, column):
        self.messages.append(
            "\tUnrecognized token: \"" + character + "\" on line: " + str(line) + ", on column: " + str(column) + "\n")

    def get_pif_message(self, character, table):
        return character + " -- " + str(
            table.inorder_traversal(table).index(character)) + "\n"
