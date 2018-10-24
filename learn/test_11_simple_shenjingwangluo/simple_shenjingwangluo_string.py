from numpy import exp,array,random,dot
training_set_inputs = array([[0,0,0],[0,0,1],[0,1,0],[0,1,1],[1,0,0],[1,0,1],[1,1,0],[1,1,1]]) #learn data
training_set_outputs = array([[0,1,1,0,1,0,0,1]]).T
random.seed(1)
synaptic_weight = 2 * random.random((3,1)) -1
for iteration in xrange(1000000):
	output = 1/(1+exp(-(dot(training_set_inputs,synaptic_weight))))
	synaptic_weight += dot(training_set_inputs.T,(training_set_outputs - output) * output *(1-output))
print 1/(1+exp(-(dot(array([1,0,0]),synaptic_weight))))
# learning time rate
# 1				0.53002734
# 1dzb			0.58918637
# 10			0.84820304
# 10dzb			0.90595845
# 100			0.99025576
# 100dzb		0.99539785
# 1000			0.99929937
# 1000dzb		0.99989226
# 10000 		0.99993704
# 10000dzb		0.99999725
# 100000dzb		0.99999992
# 1000000		0.9999994
# 1000000dzb	1.0