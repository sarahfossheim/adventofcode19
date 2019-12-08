from input import codes
from itertools import permutations

class Amplifier:
    def __init__(self, codes):
        self.codes = list(codes)
        self.program_input = 0
        self.program_output = 0
        self.phase = 0
        self.input_processes = 0

    def set_phase(self, value):
        self.phase = value

    def set_input(self, value):
        self.program_input = value

    def get_input(self):
        if self.input_processes == 0:
            input_ = self.phase
        elif self.input_processes == 1:
            input_ = self.program_input
        self.input_processes += 1
        return input_

    def get_output(self):
        return self.program_output

    def breakdown_codes(self, code):
        A = code // 10000 % 10
        B = code // 1000 % 10
        C = code // 100 % 10
        DE = code % 100

        return [A, B, C, DE]

    def run(self):
        values = self.codes[:]
        index = 0
        while True:
            opcode = self.breakdown_codes(values[index])
            operation = opcode[3]
            mode_1 = opcode[2]
            mode_2 = opcode[1]
            mode_3 = opcode[0]

            # GET NUMBER INDECES
            index_1 = values[index + 1] if mode_1 == 0 and index + 1 < len(values) else index + 1
            index_2 = values[index + 2] if mode_2 == 0 and index + 2 < len(values) else index + 2
            index_3 = values[index + 3] if mode_3 == 0 and index + 3 < len(values) else index + 3

            # STOP
            if operation == 99:
                return self.program_output
                
            # ADDITION
            elif operation == 1:
                number_1 = values[index_1]
                number_2 = values[index_2]
                values[index_3] = number_1 + number_2
                index += 4

            # MULTIPLICATION
            elif operation == 2:
                number_1 = values[index_1]
                number_2 = values[index_2]
                values[index_3] = number_1 * number_2
                index += 4

            # INPUT
            elif operation == 3: 
                input_ = self.get_input()
                values[values[index + 1]] = input_
                index += 2

            # OUTPUT
            elif operation == 4: 
                output = values[index_1]
                self.program_output = output
                index += 2

            # JUMP
            elif operation == 5:
                number_1 = values[index_1]
                if number_1 != 0:
                    index = values[index_2]
                else:
                    index += 3

            elif operation == 6:
                number_1 = values[index_1]
                if number_1 == 0:
                    index = values[index_2]
                else:
                    index += 3

            elif operation == 7:
                if values[index_1] < values[index_2]:
                    values[index_3] = 1
                else:
                    values[index_3] = 0
                index += 4

            elif operation == 8:            
                if values[index_1] == values[index_2]:
                    values[index_3] = 1
                else:
                    values[index_3] = 0
                index += 4


class AmplifierSequence:
    def __init__(self, codes, sequence):
        self.codes = codes
        self.sequence = sequence
        
        self.amplifier_A = Amplifier(codes)
        self.amplifier_B = Amplifier(codes)
        self.amplifier_C = Amplifier(codes)
        self.amplifier_D = Amplifier(codes)
        self.amplifier_E = Amplifier(codes)

        self.amplifier_A.set_phase(sequence[0])
        self.amplifier_B.set_phase(sequence[1])
        self.amplifier_C.set_phase(sequence[2])
        self.amplifier_D.set_phase(sequence[3])
        self.amplifier_E.set_phase(sequence[4])

    def run(self):
        self.amplifier_A.set_input(0)
        self.amplifier_A.run()

        self.amplifier_B.set_input(self.amplifier_A.get_output())
        self.amplifier_B.run()

        self.amplifier_C.set_input(self.amplifier_B.get_output())
        self.amplifier_C.run()

        self.amplifier_D.set_input(self.amplifier_C.get_output())
        self.amplifier_D.run()

        self.amplifier_E.set_input(self.amplifier_D.get_output())
        self.amplifier_E.run()

    def get_output(self):
        return self.amplifier_E.get_output()


outcomes = {}
gen_permutations = permutations(range(0,5))
for permutation in gen_permutations:
    amplifiers = AmplifierSequence(codes, permutation)
    amplifiers.run()
    result = amplifiers.get_output()
    outcomes[permutation] = result
#
maximum = max(outcomes.items(), key=lambda t: t[1])
print(maximum)
