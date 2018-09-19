# !/usr/bin/env python
# python test.py
import colin
def func(*a):
	res = 1
	for i in range(len(a)):
		res *= sum(a[i])
	return res
a = [1,2,3]
b = [4,5,6]
c = [7,8]
d = [9]
e = [10,11,12,13,14]
f = colin.func2(99) # call c languare
g = colin.func3(a,b,c,d,e) # call c languare
h = func(a,b,c,d,e)
print "f = ",f
print "g = ",g
print "h = ",h
