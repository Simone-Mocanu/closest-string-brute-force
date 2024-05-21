from itertools import product
import sys

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
    for key, value in hamming_dist_dict.items():
        if value == global_smallest_hamming_dist:
            print(key, value)

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
            # print(filtered_string, hamming_dist_arr, count)
        
    
    print(final_arr)
    return final_arr
    #return the string with the lowest hamming_distances (median)
    

strings = ["cata", "cota", "sstb", "bnas", "bgat"]
#strings = ["asdb", "axty", "asza"]

closest_strings = closest_string_brute_force(strings)
# print(closest_strings)



