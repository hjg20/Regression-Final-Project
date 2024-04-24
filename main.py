import numpy as np

names = ['Kevin', 'Hunter', 'Reese', 'Guililililililio']

roles = ['ModelDiag', 'VariableSelection', 'Colinearity/GLS/WLS', 'Categorical']


for i in range(4):
    name = np.random.randint(0,4-i)
    role = np.random.randint(0,4-i)

    print(f'{names[name]} has the role of {roles[role]}')

    names.remove(names[name])
    roles.remove(roles[role])