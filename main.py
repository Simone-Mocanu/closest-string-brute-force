from itertools import product
from utils import *
import string
import sys
import time
import matplotlib.pyplot as plt
import numpy as np

hamming_dist_dict = {}

def hamming_dist(string1, string2):
    count = 0
    for i in range(len(string1)):
        if string1[i] != string2[i]:
            count += 1
    return count

letters = []

def closest_string_brute_force(strings):
    count = 0
    for i in range(len(strings[0])):
        for string in strings:
            if string[i] not in letters:
                letters.append(string[i])

    m = len(strings[0])
    # Generate the Cartesian product
    permutations = product(letters, repeat=m)
    
    hamming_dist_arr = []
    # Print the permutations

    global_smallest_hamming_dist = sys.maxsize
    for p in permutations:
        highest_hamming_dist = 0
        hamming_dist_arr.clear() #!!!!!!!!!!!!!!!
        bf_string = ''.join(p)

        for string in strings:
            hamming_dist_arr.append(hamming_dist(string, bf_string))

        #get the highest_hamming_dist in the array
        for i in hamming_dist_arr:
            if highest_hamming_dist < i:
                highest_hamming_dist = i
        
        # print("highest hamming dist: " + str(highest_hamming_dist))
        #update global
        if highest_hamming_dist < global_smallest_hamming_dist:
            global_smallest_hamming_dist = highest_hamming_dist

        # populate the dict
        hamming_dist_dict[bf_string] = highest_hamming_dist
    
    # print("global shd:" + str(global_smallest_hamming_dist))
    closest_string = {i for i in hamming_dist_dict if hamming_dist_dict[i]==global_smallest_hamming_dist}
    filtered_array = []
    closest_strings = list(closest_string)
    # print("closest strings: " + str(closest_string))

    hamming_dist_arr = []
    for closest_string in closest_strings:
        hamming_dist_arr.clear()
        for string in strings:
            hamming_dist_arr.append(hamming_dist(closest_string, string))
        
        not_a_good_string = False
        for value in hamming_dist_arr:
            if value > global_smallest_hamming_dist or value == 0:
                not_a_good_string = True
            
        if not not_a_good_string:
            filtered_array.append(closest_string)

    global_smallest_count = sys.maxsize
    for filtered_string in filtered_array:
        count = 0
        hamming_dist_arr.clear()
        for string in strings:
            hamming_dist_arr.append(hamming_dist(filtered_string, string))
        
        for value in hamming_dist_arr:
            if value == global_smallest_hamming_dist:
                count += 1

        if count < global_smallest_count:
            global_smallest_count = count
        
        # print(filtered_string, hamming_dist_arr, count)

    final_arr = []

    for filtered_string in filtered_array:
        count = 0
        hamming_dist_arr.clear()
        for string in strings:
            hamming_dist_arr.append(hamming_dist(filtered_string, string))
        for value in hamming_dist_arr:
            if value == global_smallest_hamming_dist:
                count += 1
        
        if count == global_smallest_count:
            final_arr.append(filtered_string)
            #print(filtered_string, hamming_dist_arr)
        
    
    return final_arr
    

#strings = ["cata", "cota", "sstb", "bnas", "bgat"]
#strings = ["asdb", "axty", "asza"]



alphabet = string.ascii_lowercase

number_of_strings = 1
number_of_strings_arr = []
strings_arr = []
closest_string_final_arr = []
closest_string_arr = []
time_arr = []
print("wait...")
for i in range(10):
    start = time.time()
    closest_string_arr.clear()
    number_of_strings_arr.append(number_of_strings)
    strings = generate_random_strings(number_of_strings, 5, alphabet)
    strings_arr.append(strings)
    closest_strings = closest_string_brute_force(strings)
    closest_string_arr.append(closest_strings)
    closest_string_final_arr.append(closest_string_arr)
    #print(closest_strings)

    end = time.time()
    length = end - start
    time_arr.append(length)
    number_of_strings += 1

print("number_of_strings_arr: " + str(number_of_strings_arr))
print("time_arr: " + str(time_arr))
print("strings_arr: " + str(strings_arr))
print("closest_strings: " + str(closest_string_final_arr))
xpoints = number_of_strings_arr
ypoints = time_arr

plt.figure(num=0, dpi=120)
plt.title("Time / strings")
plt.xlabel("Number of strings")
plt.ylabel("Time in seconds")
plt.plot(xpoints, ypoints)
plt.show()
