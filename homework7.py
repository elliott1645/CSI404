class circuit(object):
    def __init__(self, in1, in2):
        self.in1_ = in1
        self.in2_ = in2

class andgate(circuit):
    def cir_func(self):
        return self.in1_ and self.in2_

class andgate_3in(circuit):

    def __init__(self, in1, in2, in3):
        self.in1_ = in1
        self.in2_ = in2
        self.in3_ = in3

    def cir_func(self):
        return self.in1_ and self.in2_ and self.in3_

class orgate(circuit):
    def cir_func(self):
        return self.in1_ or self.in2_

class orgate_3in(circuit):
    def __init__(self, in1, in2, in3):
        self.in1_ = in1
        self.in2_ = in2
        self.in3_ = in3

    def cir_func(self):
        return self.in1_ or self.in2_ or self.in3_

class orgate_4in(circuit):
    def __init__(self, in1, in2, in3, in4):
        self.in1_ = in1
        self.in2_ = in2
        self.in3_ = in3
        self.in4_ = in4

    def cir_func(self):
        return self.in1_ or self.in2_ or self.in3_ or self.in4_

class notgate(circuit):

    def __init__(self, in1):
        self.in1_ = in1

    def cir_func(self):
        return not self.in1_

class mux_2to1(circuit):
    def __init__(self, in1, in2, ctr1):
        self.in1_ = in1
        self.in2_ = in2
        self.ctr1_ = ctr1

    def cir_func(self):

        inv_ctr = notgate(self.ctr1_).cir_func()
        a0 = andgate(self.in1_, inv_ctr).cir_func()
        a1 = andgate(self.in2_, self.ctr1_).cir_func()
        o0 = orgate(a0, a1)

        return o0.cir_func()

class mux_4to1(circuit):
    def __init__(self, in1, in2, in3, in4, ctr0, ctr1):
        self.in1_ = in1
        self.in2_ = in2
        self.in3_ = in3
        self.in4_ = in4
        self.ctr1_ = ctr0
        self.ctr0_ = ctr1

    def cir_func(self):

        m0_output = mux_2to1(self.in1_, self.in2_, self.ctr0_).cir_func()
        m1_output = mux_2to1(self.in3_, self.in4_, self.ctr0_).cir_func()
        m3_output = mux_2to1(m0_output, m1_output, self.ctr1_).cir_func()

        return m3_output

class fulladder(circuit):
    def __init__(self, in1, in2, carryIn):
        self.in1_ = in1
        self.in2_ = in2
        self.carryIn_ = carryIn

    def cir_func(self):

        o_2andg_1_co = andgate(self.in1_, self.carryIn_).cir_func()
        o_2andg_2_co = andgate(self.in2_, self.carryIn_).cir_func()
        o_2andg_3_co = andgate(self.in1_, self.in2_).cir_func()

        carryOut = orgate_3in(o_2andg_1_co, o_2andg_2_co, o_2andg_3_co).cir_func()

        in1_inv = notgate(self.in1_).cir_func()
        in2_inv = notgate(self.in2_).cir_func()
        cin_inv = notgate(self.carryIn_).cir_func()

        o_3andg_1_sum = andgate_3in(in1_inv, in2_inv, self.carryIn_).cir_func()
        o_3andg_2_sum = andgate_3in(in1_inv, self.in2_, cin_inv).cir_func()
        o_3andg_3_sum = andgate_3in(self.in1_, self.in2_, self.carryIn_).cir_func()
        o_3andg_4_sum = andgate_3in(self.in1_, in2_inv, cin_inv).cir_func()

        sum = orgate_4in(o_3andg_1_sum, o_3andg_2_sum,o_3andg_3_sum, o_3andg_4_sum).cir_func()

        return sum, carryOut

'''
homework 7  Due Dec 1th 5:45pm
Implement the alu control circuit class aluControl below based on the FIGURE D.2.3. The figure is from textbook and is also in lecture slides 13_ALU_Control_Continue.pdf.

NOTE: There is an error in the texbook FIGURE D.2.3, please correct that error as we did in class before you write the code.

The inputs are ALUOps and function code field.
The outputs are ALU control signals.

e.g: (1 is for Ture, 0 is for False)
inputs: 11100010
outputs: 0110(subtract)

inputs: 10110101
outputs: 0001(or)
'''

class aluControl(circuit):
    def __init__(self, o1, o0, f5, f4, f3, f2, f1, f0):
        self.o1_ = o1
        self.o0_ = o0
        self.f5_ = f5
        self.f4_ = f4
        self.f3_ = f3
        self.f2_ = f2
        self.f1_ = f1
        self.f0_ = f0

    def cir_func(self):
        f2_inv = notgate(self.f2_).cir_func()
        o0_inv = notgate(self.o0_).cir_func()
        o1_inv = notgate(self.o1_).cir_func()
        f0_and_f3 = orgate(self.f0_, self.f3_).cir_func()
        operation0 = andgate(f0_and_f3, self.o1_).cir_func()
        operation1 = orgate(f2_inv, o1_inv).cir_func()
        operation2_sub = andgate(self.f2_, self.o1_).cir_func()
        operation2 = orgate(operation2_sub, self.o0_).cir_func()
        operation3 = andgate(self.o0_, o0_inv).cir_func()
        return operation0, operation1, operation2, operation3

'''
homework 7

Implement a 1 bit ALU class ALU_1bit, which takes four inputs: in1, in2, cin and alu_ctrs, the output should be the aluresult and adder_carryout.

'''

#please write your code here

class obamaALU_1_bit(circuit):
    def __init__(self, in1, in2, cin, alu_ctrs):
        self.in1 = in1
        self.in2 = in2
        self.cin = cin
        self.alu_ctrs = alu_ctrs

    def cir_func(self):
        alu = [None]*4
        if self.alu_ctrs[0]:
            notgate(self.in1).cir_func()
        if self.alu_ctrs[1]:
            notgate(self.in2).cir_func()
        one = andgate(self.in1, self.in2).cir_func()
        two = orgate(self.in1, self.in2).cir_func()
        three,carryout = fulladder(self.in1, self.in2, self.cin).cir_func()
        four = False
        turkey = mux_4to1(one, two, three, four, self.alu_ctrs[2], self.alu_ctrs[3]).cir_func() 
        return turkey, carryout

    

def binaryToBoolean(input_binary, outputboolean):
    for i in range(0, len(input_binary)):
        one_or_zero = input_binary[i]
        if (one_or_zero == '1'):
            outputboolean[i] = True
        else:
            outputboolean[i] = False

def booleanToBinary(input_boolean, outputbinary):

    for i in range(0, len(input_boolean)):
        TureOrFalse = input_boolean[i]
        if (TureOrFalse == True):
            outputbinary[i] = 1
        else:
            outputbinary[i] = 0

def main():

    input1_b = [None]*32
    input2_b = [None]*32

    instru_b = [None]*32

    input1 = raw_input("Please Enter the first input: ")
    input2 = raw_input("Please Enter the second input: ")

    instru = raw_input("Please enter the alu ops and funct fields for controling alu: ")

    binaryToBoolean(instru, instru_b)
    binaryToBoolean(input1, input1_b)
    binaryToBoolean(input2, input2_b)

    '''
    homework7:

    use the aluControl class to take the alu ops and funct fields as the input,

    the output will be the alu control signals alu_ctrs,

    check if the alu control signals indicate subtraction, if it is, set the cin_forbit0 as True; else set cin_forbit0 as False

    use the ALU_1bit class you just implemented to take two 1 bit inputs, the cin_forbit0, and also the alu_ctrs

    print out the ALU_1bit output o_alu, o_alu_carryout

    the input and output format should as following:

    Please Enter the first input: 1
    Please Enter the second input: 1
    Please enter the alu ops and funct fields for controling alu: 10100100
    the output of the 1bitalu: True
    the carryout of the 1bitalu: True
-------------------------------------------------------------------------------
    Please Enter the first input: 0
    Please Enter the second input: 1
    Please enter the alu ops and funct fields for controling alu: 01000000
    the output of the 1bitalu: True
    the carryout of the 1bitalu: False
-------------------------------------------------------------------------------
    Please Enter the first input: 1
    Please Enter the second input: 0
    Please enter the alu ops and funct fields for controling alu: 10010101
    the output of the 1bitalu: True
    the carryout of the 1bitalu: False

    '''

    #Please write your code here

    someArray = [None]*4
    someArray[0], someArray[1], someArray[2], someArray[3] = aluControl(instru_b[0], instru_b[1], instru_b[2], instru_b[3], instru_b[4], instru_b[5]
, instru_b[6], instru_b[7]).cir_func()

    obama_output, carryout1 = obamaALU_1_bit(input1_b[0], input2_b[0], someArray[2], someArray).cir_func()
    print obama_output
    print carryout1
if __name__ == '__main__':
    main()
