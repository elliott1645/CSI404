
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
		
#---------------------------------------------------------------
# homework 6 due Tu 11/17/15 5:45pm

'''
use the mux_2to1, implement a 4 to 1 multiplexer class mux_4to1
'''
		
def main():

	input1_b = [None]*32
	input2_b = [None]*32
	input3_b = [None]*32
	input4_b = [None]*32
	
	ctr_b = [None]*32
	
	input1 = raw_input("Please Enter the first input: ")
	input2 = raw_input("Please Enter the second input: ")
	input3 = raw_input("Please Enter the third input: ")
	input4 = raw_input("Please Enter the fouth input: ")
	ctr = raw_input("Please Enter the ctr signal input: ")
	
	
	for i in range(0, len(input1)):
		one_or_zero = input1[i]
		if (one_or_zero == '1'):
			input1_b[i] = True
		else: 
			input1_b[i] = False

	for i in range(0, len(input2)):
		one_or_zero = input2[i]
		if (one_or_zero == '1'):
			input2_b[i] = True
		else:
			input2_b[i] = False	
	
	for i in range(0, len(input3)):
		one_or_zero = input3[i]
		if (one_or_zero == '1'):
			input3_b[i] = True
		else:
			input3_b[i] = False	
	
	for i in range(0, len(ctr)):
		one_or_zero = ctr[i]
		if (one_or_zero == '1'):
			ctr_b[i] = True
		else:
			ctr_b[i] = False	
	
	for i in range(0, len(input4)):
		one_or_zero = input4[i]
		if (one_or_zero == '1'):
			input4_b[i] = True
		else:
			input4_b[i] = False
	
	o_mux = mux_2to1(input1_b[0], input2_b[0], ctr_b[0]) 
	
	output = o_mux.cir_func()
	
	#---------------------------------------------------------------
	# homework 6 due Tu 11/17/15 5:45pm

	'''
	give 4 inputs to your mux_4to1, and 2-bit control signal also
	
	e.g  inputs
	Please Enter the first input: 1
	Please Enter the second input: 1
	Please Enter the third input: 0
	Please Enter the fouth input: 1
	Please Enter the ctr signal input: 01
	
	your output should be:
	the output for mux_4to1:  False
		
	Please note in the ctr signal 01, 0 is going to be used as the control signal of two 2to1mux, 1 is going to be used as the control signal for only 1 2to1mux
	
	'''
		
	print "the output for mux_4to1: ", output
	
if __name__ == '__main__':
	main()
