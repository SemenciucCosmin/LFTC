class Transition:
    def __init__(self, initial_state, symbol, final_state):
        self.initial_state = initial_state
        self.symbol = symbol
        self.final_state = final_state

    def __str__(self):
        return "(" + self.initial_state + ", " + self.symbol + ")->" + self.final_state
