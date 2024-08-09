# Import Packages
import numpy as np
import random
random.seed(42)
import pandas as pd

class PermutationTest():
    def __init__(self, data1, data2, nb_permutation, p_value):
        self.data1 = data1
        self.data2 = data2
        self.nb_permutation = nb_permutation
        self.p_value = p_value
        self.concat_arrays = np.concatenate((data1, data2))
        self.mean_diff = []
    
    @staticmethod 
    def calculate_mean_diff(data_1, data_2):
        return np.mean(data_1) - np.mean(data_2)
    
    def get_mean(self):
        return calculate_mean_diff(self.data1, self.data2)
    
    def do_permutation(self):
        # Shuffle self.concat_arrays
        np.random.shuffle(self.concat_arrays)
        
        # New distribution
        new_data1 = self.concat_arrays[:len(self.data1)]
        new_data2 = self.concat_arrays[len(self.data1):]
        return new_data1, new_data2
    
    def check_p_value(self, probability):
        if probability < self.p_value:
            print("Withdraw null hypothesis")
        else:
            print("Stay with null hpothesis")
            
    def calculate_probability(self):
        return np.sum(np.abs(np.array(self.mean_diff) >= np.abs(self.get_mean()))) / self.nb_permutation
    
    def run_permutation_test(self):
        for _ in range(self.nb_permutation):
            new_data1, new_data2 = self.do_permutation()
            self.mean_diff.append(self.calculate_mean_diff(new_data1, new_data2))
            
        # Check p_value
        self.check_p_value(self.calculate_probability())
        
        print(self.mean_diff)

