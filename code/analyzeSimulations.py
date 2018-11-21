import os
import numpy as np
from complexity import normEntropy, desequilibrium
from symbol import symbolCount

input_dir = '../simulaciones'
output_dir = '../output'

word_len = 5    ## Length of the words
n_series = 10 ## Number of temporal series per data file

file_names = []
for file_name in os.listdir(input_dir):
    if '.txt' in file_name:
        version = file_name.split('v')[1].split('.')[0]
        print('Analyzing series', version)
        data = np.loadtxt(input_dir + '/' + file_name, 
                          dtype='float32', delimiter=',')
        properties = []
        for i in range(n_series):    
            Z = symbolCount(data[:,i], word_len)

            H = normEntropy(Z)
            D = desequilibrium(Z)
            C = H*D

            properties.append([H, D, C])

        output_file = output_dir + '/' + 'properties_v' + version + '.txt'
        np.savetxt(output_file, properties)