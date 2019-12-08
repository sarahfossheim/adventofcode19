from input import codes
from itertools import permutations

class Amplifier:
    def __init__(self, codes):
        self.codes = list(codes)
        self.program_input = 0
        self.program_output = 0
        self.phase = 0
        self.input_processes = 0
        self.stopped = False
        self.index = 0

    def set_phase(self, value):
        self.phase = value

    def set_input(self, value):
        self.program_input = value

    def set_output(self, value):
        self.program_output = value

    def is_stopped(self):
        return self.stopped

    def get_input(self):
        input_ = self.phase
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
        while True:
            opcode = self.breakdown_codes(self.codes[self.index])
            operation = opcode[3]
            mode_1 = opcode[2]
            mode_2 = opcode[1]
            mode_3 = opcode[0]

            # GET NUMBER INDECES
            index_1 = self.codes[self.index + 1] if mode_1 == 0 and self.index + 1 < len(self.codes) else self.index + 1
            index_2 = self.codes[self.index + 2] if mode_2 == 0 and self.index + 2 < len(self.codes) else self.index + 2
            index_3 = self.codes[self.index + 3] if mode_3 == 0 and self.index + 3 < len(self.codes) else self.index + 3

            # STOP
            if operation == 99:
                self.stopped = True
                break
                
            # ADDITION
            elif operation == 1:
                number_1 = self.codes[index_1]
                number_2 = self.codes[index_2]
                self.codes[index_3] = number_1 + number_2
                self.index += 4

            # MULTIPLICATION
            elif operation == 2:
                number_1 = self.codes[index_1]
                number_2 = self.codes[index_2]
                self.codes[index_3] = number_1 * number_2
                self.index += 4

            # INPUT
            elif operation == 3: 
                input_ = self.get_input()
                self.codes[self.codes[self.index + 1]] = input_
                self.index += 2

            # OUTPUT
            elif operation == 4: 
                output = self.codes[index_1]
                self.program_output = output
                self.index += 2

            # JUMP
            elif operation == 5:
                number_1 = self.codes[index_1]
                if number_1 != 0:
                    self.index = self.codes[index_2]
                else:
                    self.index += 3

            elif operation == 6:
                number_1 = self.codes[index_1]
                if number_1 == 0:
                    self.index = self.codes[index_2]
                else:
                    self.index += 3

            elif operation == 7:
                if self.codes[index_1] < self.codes[index_2]:
                    self.codes[index_3] = 1
                else:
                    self.codes[index_3] = 0
                self.index += 4

            elif operation == 8:            
                if self.codes[index_1] == self.codes[index_2]:
                    self.codes[index_3] = 1
                else:
                    self.codes[index_3] = 0
                self.index += 4


class AmplifierSequence:
    def __init__(self, codes, sequence):
        self.codes = codes
        self.sequence = sequence
        # self.amplifiers = [Amplifier(codes) for _ in range(0,5)]
        # for i in range(0,5):
        #     self.amplifiers[i].set_phase(sequence[i])

        #
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

        self.amplifiers = [self.amplifier_A, self.amplifier_B, self.amplifier_C, self.amplifier_D, self.amplifier_E]

    def run(self):
        last_amp = self.amplifiers[-1]
        last_amp.set_output(0)
        index = 0

        while True:
            if index > 4:
                index = 0

            current = self.amplifiers[index]
            previous = self.amplifiers[index - 1]

            current.set_input(previous.get_output())
            current.run()

            if current.is_stopped():
                break
            index += 1
            

    def get_output(self):
        return self.amplifiers[-1].get_output()


outcomes = {}
gen_permutations = permutations(range(5,10))
for permutation in gen_permutations:
    amplifiers = AmplifierSequence(codes, permutation)
    amplifiers.run()
    result = amplifiers.get_output()
    outcomes[permutation] = result
#
maximum = max(outcomes.items(), key=lambda t: t[1])
print(maximum)
