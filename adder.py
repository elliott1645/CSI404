class circuit(object):
    def __init__(self, in1, in2):
        self.in1_ = in1
        self.in2_ = in2

class andgate(circuit):
    def cir_func(self):
        return self.in1_ and self.in2_

class orgate(circuit):
    def cir_func(self):
        return self.in1_ or self.in2_

class notgate(circuit):
    def __init__(self, in1):
        self.in1_ = in1

    def cir_func(self):
        return not self.in1_

