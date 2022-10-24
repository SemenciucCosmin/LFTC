from Labs.Lab3.pythonProject.SymbolTable import SymbolTable


class Scanner:
    def __init__(self):
        self.symbol_table = SymbolTable()
        self.output_file = "St.out"
        self.token_file = "Token.txt"
        self.messages = []

    def load_tokens(self):
        file = open(self.token_file, "r")
        lines = file.readlines()
        for line in lines:
            if len(line) > 2:
                self.symbol_table.constants.add_element(self.symbol_table.constants, line.strip("\n"))
            else:
                self.symbol_table.identifiers.add_element(self.symbol_table.identifiers, line.strip("\n"))

    def scan_file(self, file_name):
        self.messages = []
        file = open(file_name, "r")
        lines = file.readlines()
        index = 0

        for line in lines:
            index += 1
            line = line.strip("\n")
            line = line.strip("\t")
            for character in line:
                if character != " ":
                    if not self.symbol_table.identifiers.search(self.symbol_table.identifiers, character):
                        self.messages.append("\tUnrecognized token: \"" + character + "\" on line: " + str(index) + "\n")
            constants = line.split(" ")
            for constant in constants:
                if constant.isupper():
                    if not self.symbol_table.constants.search(self.symbol_table.constants, constant):
                        self.messages.append("\tUnrecognized token: \"" + constant + "\" on line: " + str(index) + "\n")

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
