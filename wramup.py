#%%

from copy import deepcopy


def inplace_add_vectors(vec1: list, vec2: list)-> None:
    for i in range(len(vec1)):
        vec1[i] = vec1[i] + vec2[i]
v1 = [1, 2, 3]
v2 = [4, 5, 6]

def add_vectors(vec1: list, vec2: list)-> list:

    vec3 = deepcopy(vec1)
                       
    for i in range(len(vec1)):
        vec3[i] = vec1[i] + vec2[i]
        return vec3
    

vec3 = add_vectors(v1, v2)



print(v1)
print(vec3)




#%%
