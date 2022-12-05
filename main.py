'''
Disclosure of the characteristic determinant by the Danilevsky method
and calculation of eigenvalues and vectors by the Jacobi rotation method
'''

import numpy as np
from jacobi_eigen_method import find_eigen
from method_danilevskogo import DanilevskyMethod
from staff import print_array
import task
import test


E = task.E
A = test.A_5


eig_val, eig_vec, steps = find_eigen(A, E, 1)

print_array(A, 'Default Matrix:')
print_array(eig_val, '\nMatrix of Eigenvalues:')
print_array(eig_val @ np.ones(shape=(eig_val.shape[0], )), 'Eigenvalues:')
print_array(eig_vec, 'Eigenvectors:')


print("\nVerification:")
print("\nVerification:")

w, v = np.linalg.eig(A)
print_array(w, 'Eigenvalues (numpy):')
print_array(v, 'Eigenvectors (numpy):')


print("\nMethod Danilevskogo:")
eig_val, eig_vec = DanilevskyMethod(A, E, 1)
print_array(eig_val, '\nEigenvalues:')
print_array(eig_vec, 'Eigenvectors:')