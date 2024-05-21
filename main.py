from itertools import product
import string
import sys

alphabet = string.ascii_lowercase  # 'abcdefghijklmnopqrstuvwxyz'
hamming_dist_dict = {}

def hamming_dist(string1, string2):
    count = 0
    for i in range(len(string1)):
        if string1[i] != string2[i]:
            count += 1
    return count


def closest_string_brute_force(strings):
    m = len(strings[0])
    # Generate the Cartesian product
    permutations = product(alphabet, repeat=m)
    
    smallest_max_hamming_dist = sys.maxsize
    hamming_dist_arr = []
    # Print the permutations
    for p in permutations:
        hamming_dist_arr.clear() #!!!!!!!!!!!!!!!

        bf_string = ''.join(p)
        # print(bf_string)
        max_hamming_dist = 0

        for string in strings:
            hamming_dist_arr.append(hamming_dist(string, bf_string))
            if(string == bf_string):
                continue
            

        for i in hamming_dist_arr:
            if max_hamming_dist < i:
                max_hamming_dist = i
            
            if max_hamming_dist == 0:
                print("string: " + bf_string)

                print("max_hamming_dist: " + str(max_hamming_dist))

            if max_hamming_dist < smallest_max_hamming_dist:
                smallest_max_hamming_dist = max_hamming_dist

        if bf_string == "cstb":
            print(max_hamming_dist)
            print(smallest_max_hamming_dist)
            print(hamming_dist_arr)
            print("smallest_max_hamming_dist: " + str(smallest_max_hamming_dist))
            return

        hamming_dist_dict[bf_string] = max_hamming_dist
        #

    #print(hamming_dist_dict)
    # for key, value in hamming_dist_dict.items():
    #     if value == 2:
    #         print(key, value)
    closest_string = {i for i in hamming_dist_dict if hamming_dist_dict[i]==2}

    return closest_string
    #return the string with the lowest hamming_distances (median)
    
strings = ["cata", "cota", "sstb"]
#strings = ["asdb", "axty", "asza"]
#TODO: filter closest_string by the minimum 'k'


closest_string = closest_string_brute_force(strings)
#print(closest_string)




