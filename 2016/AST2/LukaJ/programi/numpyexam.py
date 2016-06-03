import numpy

a = numpy.arange(15).reshape(3,5)
print(a)
print(a.shape)
print(a.ndim)
print(a.dtype.name)
print(a.size)
print(type(a))

b = numpy.array( [2,3,4] )
print(b)
