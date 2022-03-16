class Automaton():

    def __init__(self, config_file):
        self.config_file = config_file
        print("Hi, I'm an automaton!")

        automaton = {"sigma": [], "states": [], "transitions": []}
        with open(self.config_file) as input:
            while len(automaton["sigma"]) == 0 or len(automaton["stari"]) == 0 or len(automaton["tranzitii"]) == 0:
                line = input.readline().strip()  # eliminarea spatiilor inutile
                section = line.split(":", maxsplit=1)[0]
                if line[0] == "#":
                    continue
                elif section in automaton.keys():
                    while line != "end":
                        line = input.readline().strip()
                        if "end" not in line:
                            automaton[section].append(line)  # adaugarea value in dict automaton la cheia section

        automaton["states"] = [tuple([x for x in state.split(",")]) for state in automaton["states"]]

        self.automaton = automaton
        print(automaton)

    def validate():
        states = [state[1] if len(state) > 1 else "" for state in self.automaton["states"]]
        if states.count("S") > 1:
            print("Only one state")
            return False

        for transition in self.automaton["transitions"]:
            state1, word, state2 = [y for y in transition.split(",")]
            valid_states = [state[0] for state in self.automaton["states"]]
            if state1 not in valid_states or state2 not in valid_states or word not in self.automaton["sigma"]:
                print("Invalid words or states")
                return False
        return True


if __name__ == "__main__":
    automaton = Automaton("your_config_file")
    print(automaton.validate())

