import random

def generate_random_strings(n, m, chars):
    generated_strings = []

    for i in range(n):
        string = ''
        for j in range(m):
            string += random.choice(chars)
        
        generated_strings.append(string)

    return generated_strings
