from Labs.Lab3Lab4.pythonProject.Transition import Transition


class FA:
    def __init__(self):
        self.all_states = []
        self.alphabet = []
        self.transitions = []
        self.initial_state = ""
        self.final_states = []
        self.load_from_file()

    def load_from_file(self):
        file = open("FA.in", "r")
        lines = file.readlines()
        all_states_line = lines[0].strip("\n").split(" ")
        alphabet_line = lines[1].strip("\n").split(" ")
        transitions_line = lines[2].strip("\n").split(" ")
        self.initial_state = lines[3].strip("\n").split(" ")[0]
        final_states_line = lines[4].strip("\n").split(" ")

        for state in all_states_line:
            self.all_states.append(state)

        for symbol in alphabet_line:
            self.alphabet.append(symbol)

        for state in final_states_line:
            self.final_states.append(state)

        for transition in transitions_line:
            attributes = transition.split("-")
            self.transitions.append(Transition(attributes[0], attributes[1], attributes[2]))

        file.close()

    def verify(self, sequence):
        current_state = self.initial_state
        for symbol in sequence:
            if symbol not in self.alphabet:
                return False
            current_state = self.get_next_state(current_state, symbol)
            if current_state is None:
                return False

        return current_state in self.final_states

    def get_next_state(self, current_state, symbol):
        for transition in self.transitions:
            if transition.initial_state == current_state and transition.symbol == symbol:
                return transition.final_state
        return None
