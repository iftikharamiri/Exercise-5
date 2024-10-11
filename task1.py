"""""
taks nr 1

"""""
#%%
import numpy as np 
import random
matrix = np.random.randint(0, 101, size=(5000, 5000))
a= np.sum(matrix)

#Sum matrix
def sum_function(matrix):
    totall_sum_nr = 0

    for row in matrix:
        for element in row:
            totall_sum_nr += element
    return totall_sum_nr
print('Task 1'.center(30))
print('-'*30)
print(f"Sum: {sum_function(matrix)}")

#Mean
def mean_function(matrix):
    totall_element = matrix.shape[0]*matrix.shape[1]
    totall_sum = sum_function(matrix)
    mean_value = totall_sum/totall_element
    return mean_value
print(f"MEan:{mean_function(matrix)}")

#varinace
def varinace_function(matrix):
    totall_squared = 0
    totall_element = matrix.shape[0]*matrix.shape[1]
    for row in matrix:
        for element in row:
            totall_squared += (element - mean_function(matrix))**2
        
    variance = totall_squared/totall_element
    return variance
print(f"Variance: {varinace_function(matrix)}")


#new matrix
import copy

def multiply_function(matrix, nr:int):

    multipal_matrix = copy.deepcopy(matrix)

    for row in matrix:
        for element in row:
            multipal_matrix *=nr

        return multipal_matrix
print(f"New_matrix: {multiply_function(matrix, 0)}")

"""""
task nr 2
"""""

A = np.zeros((50, 50))

np.fill_diagonal(A, -2)
n = A.shape[0]
for i in range(n-1):
    A[i, i+1] = 1
for i in range(1, n):
    A[i, i-1] = 1


def iteration(A, num_iteration=100):
    v = np.random.rand(A.shape[1])
  
    for _ in range(100):
        v_new = np.dot(A, v)
        norm_v_new = np.linalg.norm(v_new)
        if norm_v_new == 0:
            return None
        
        v = v_new/norm_v_new
                
        dominant_eigenvalue= np.abs(np.dot(v.T, np.dot(A, v)))/(np.dot(v.T, v))
        return dominant_eigenvalue
print('Task 2'.center(23))
print('-'*30)    
print(f"Eigenvalue after 100 iterations: {iteration(A, 100)}")
      
eigenvalue, _ = np.linalg.eig(A)
dominant_eigenvalue_np = np.max(np.abs(eigenvalue))

print(f"Eigenvalue fra np: {dominant_eigenvalue_np}")

