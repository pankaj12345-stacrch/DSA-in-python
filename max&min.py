# import numpy library
import numpy

# creating a two dimensional
# numpy array of integers
arr = numpy.array([[11, 2, 3],
					[4, 5, 16],
					[7, 81, 22]])

# finding the maximum and
# minimum element in the array
max_element_column = numpy.max(arr, 0)
max_element_row = numpy.max(arr, 1)

min_element_column = numpy.amin(arr, 0)
min_element_row = numpy.amin(arr, 1)

# printing the result
print('maximum elements in the columns of the array is:',
	max_element_column)

print('maximum elements in the rows of the array is:',
	max_element_row)

print('minimum elements in the columns of the array is:',
	min_element_column)

print('minimum elements in the rows of the array is:',
	min_element_row)
