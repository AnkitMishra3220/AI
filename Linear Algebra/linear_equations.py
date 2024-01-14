import numpy as np
import plot_lines as pl

# −𝑥1+3𝑥2=7
#
# 3𝑥1+2𝑥2=1

matrix_a = np.array([
    [-1, 3],
    [3, 2]], dtype=np.dtype(float))

matrix_b = np.array(
    [7, 1], dtype=np.dtype(float))

print('shape_of_matrix_a', matrix_a.shape)
print('shape_of_matrix_b', matrix_b.shape)

result = np.linalg.solve(matrix_a, matrix_b)

print('result 2*2 ', result)

# Evaluating Determinant of a Matrix
determinant = np.linalg.det(matrix_a)
print('determinant', determinant)

# Solving 3 variables
#  a+b+c = 10
# a+2b+c = 15
# a+b+2c = 12

matrix_x = np.array([[1, 1, 1],
                     [1, 2, 1],
                     [1, 1, 2]], dtype=np.dtype(float))

matrix_y = np.array([10, 15, 12], dtype=np.dtype(float))

result = np.linalg.solve(matrix_x, matrix_y)

print('Result 3*3: ', result)

determinant_3_3 = np.linalg.det(matrix_x)
print('determinant 3*3', determinant_3_3)

# 3*3 Infinite Solution
# a+b+c=10
# a+b+2c=15
# a+b+3c=20

matrix_q = np.array([[1, 1, 1],
                     [1, 1, 2],
                     [1, 1, 3]], dtype=np.dtype(float))

matrix_w = np.array([10, 15, 20], dtype=np.dtype(float))

try:
    result = np.linalg.solve(matrix_q, matrix_w)
except np.linalg.LinAlgError as err:
    print('result_3*3_Infinite_Sol :', err)

determinant_3_3_i_s = np.linalg.det(matrix_q)
print('determinant_3_3_i_s :', determinant_3_3_i_s)  # 0 Hence singular Matrix

# Check the dimensions of  𝐴 and  𝑏
#   using the shape attribute (you can also use np.shape() as an alternative):
print(f'Shape of A {matrix_a.shape}')
print(f'Shape of B {matrix_b.shape}')

# Unify matrix  𝐴 and array  𝑏 into one matrix using np.hstack()
# function. Note that the shape of the originally defined array  𝑏 was  (2,)
#  , to stack it with the  (2,2) matrix you need to use .reshape((2, 1)) function:

one_matrix = np.hstack((matrix_a, matrix_b.reshape((2, 1))))

print('one_matrix:', one_matrix)

pl.plot_lines(one_matrix)

# Solve No Solution with Graph

# −𝑥1 + 3𝑥2 = 7
#  3𝑥1 − 9𝑥2 = 1
#
matrix_ns = np.array([[-1, 3, 7],
                      [3, -9, 1]], dtype=np.dtype(float))

pl.plot_lines(matrix_ns)

matrix_ns = np.array([[-1, 3, 7],
                      [3, -9, 1]], dtype=np.dtype(float))

pl.plot_lines(matrix_ns)

# Solve infinite no. of  solutions with Graph
#
# −𝑥1 + 3𝑥2 = 7
#  3𝑥1 − 9𝑥2 = −21
#

matrix_ins = np.array([[-1, 3, 7],
                      [3, -9, -21]], dtype=np.dtype(float))
pl.plot_lines(matrix_ins)





