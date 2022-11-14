from Labs.Lab3Lab4.pythonProject.FA import FA
from Labs.Lab3Lab4.pythonProject.Scanner.Scanner import Scanner


def print_menu():
    print("MENU")
    print("\t0. Exit")
    print("\t1. Display set of states")
    print("\t2. Display alphabet")
    print("\t3. Display transitions")
    print("\t4. Display initial state")
    print("\t5. Display final states")
    print("\t6. Verify sequence")


def print_decision(decision, sequence):
    if decision:
        print("Decision: " + sequence + " is accepted.\n")
    else:
        print("Decision: " + sequence + " is not accepted.\n")


def print_all_states(finite_automata):
    print("All states: " + str(finite_automata.all_states))
    print()


def print_alphabet(finite_automata):
    print("Alphabet: " + str(finite_automata.alphabet))
    print()


def print_initial_state(finite_automata):
    print("Initial state: " + finite_automata.initial_state)
    print()


def print_final_states(finite_automata):
    print("Final states: " + str(finite_automata.final_states))
    print()


def print_transitions(finite_automata):
    print("Transitions: ")
    for transition in finite_automata.transitions:
        print("\t" + str(transition))
    print()


def run_scanner():
    scanner = Scanner()
    scanner.empty_output_file()
    scanner.load_tokens()
    scanner.scan_file("Programs/p1.txt")
    scanner.scan_file("Programs/p2.txt")
    scanner.scan_file("Programs/p3.txt")
    scanner.scan_file("Programs/p1err.txt")


def run_menu():
    while True:
        finite_automata = FA()
        print_menu()
        command = input("\nCommand: ")
        print()
        if command == "0":
            break
        elif command == "1":
            print_all_states(finite_automata)
        elif command == "2":
            print_alphabet(finite_automata)
        elif command == "3":
            print_transitions(finite_automata)
        elif command == "4":
            print_initial_state(finite_automata)
        elif command == "5":
            print_final_states(finite_automata)
        elif command == "6":
            sequence = input("Sequence: ")
            print()
            sequence = sequence.strip("\n")
            decision = finite_automata.verify(sequence)
            print_decision(decision, sequence)
        else:
            print("Invalid command!\n")


if __name__ == "__main__":
    run_menu()
