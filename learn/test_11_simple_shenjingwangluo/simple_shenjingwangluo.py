from numpy import exp,array,random,dot
training_set_inputs = array([[0,0,1],[1,1,1],[1,0,1],[0,1,1]]) #learn data
training_set_outputs = array([[0,1,1,0]]).T
random.seed(1)
synaptic_weight = 2 * random.random((3,1)) -1
for iteration in xrange(10000):
	output = 1/(1+exp(-(dot(training_set_inputs,synaptic_weight))))
	synaptic_weight += dot(training_set_inputs.T,(training_set_outputs - output) * output *(1-output))
print 1/(1+exp(-(dot(array([1,0,0]),synaptic_weight))))
# 1			0.53002734
# 10		0.84820304
# 100		0.99025576
# 1000		0.99929937
# 10000 	0.99993704
# 1000000	0.9999994