class Automaton():

    def __init__(self, config_file):
        self.config_file = config_file
        print("Hi, I'm an automaton!")

        self.sigma = []
        self.states = []
        self.transitions = dict()
        Automaton = dict()

        with open(self.config_file) as f:
            # Sigma:
            # word1
            # word2
            # ...
            # End
            line = f.readline().strip()  # citim prima linie din fisier pana ajungem la "end"
            while line.lower() != "end":
                # daca avem randuri comentate, "...", citim urmatoarea linie si iesim din while
                if line[0] == '#' or ("..." in line) or (":" in line):
                    line = f.readline().strip()
                    continue
                else:
                    # altfel, adaugam noua sigma si citim urmatorul rand
                    self.sigma.append(line)
                    line = f.readline().strip()

            # States:
            # state1
            # state2
            # state3, F
            # ...
            # stateK, S
            # ...
            # End
            line = f.readline().strip()
            while line.lower() != "end":
                if line[0] == '#' or ("..." in line) or (":" in line):
                    line = f.readline().strip()
                    continue
                else:
                    tuplu = line.split(",")
                    tuplu[0] = tuplu[0].strip()
                    if len(tuplu) > 1:
                        tuplu[1] = tuplu[1].strip()
                    self.states.append(tuplu)
                    line = f.readline().strip()

            # Transitions:
            # stateX, wordY, stateZ
            # stateX, wordY, stateZ
            # ...
            # End
            line = f.readline().strip()
            while line.lower() != "end":
                if line[0] == "#" or ("..." in line) or (":" in line):
                    line = f.readline().strip()
                    continue
                else:
                    aux = line.split(",")
                    aux[0], aux[1], aux[2] = aux[0].strip(), aux[1].strip(), aux[2].strip()
                    # self.transitions.append(aux)
                    self.transitions[(aux[0], aux[1])] = aux[2]
                    line = f.readline().strip()

        # print("Sigma:", self.sigma)
        # print("Tranziții:", self.transitions)
        # print("Stari:", self.states)
        Automaton = {"Sigma": self.sigma, "Stari": self.states, "Tranzitii": self.transitions}
        for key in Automaton.keys():
            print(key, "->", Automaton[key])

    def validate(self):
        init_fin = [s[1] if len(s) > 1 else "" for s in self.states]

        #”S” symbol can succeed only one state.
        if init_fin.count("S") > 1:
            print("Only one starting state allowed!")

        for tr in self.transitions.keys():
            accept_states = [state[0] for state in self.states]
            # if transition[0] not in accept_states or transition[2] not in accept_states or transition[1] not in self.sigma:
            aux1, aux2 = tr
            if self.transitions[tr] not in accept_states or aux1 not in accept_states or aux2 not in self.sigma:
                raise Exception("Transition contains invalid words or states!")
        return True, init_fin

    # def retsigma(self):
    #     return self.sigma
    #
    # def retstates(self):
    #     return self.states
    #
    # def rettransitions(self):
    #     return self.transitions

    def create_function(self):
        aux = {tuple([t[0].strip(), t[1].strip()]): t[2].strip() for t in self.transitions}
        return aux


if __name__ == "__main__":
    automaton = Automaton('input.txt')

    print(automaton.validate())