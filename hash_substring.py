# python3

def read_input():

    # this function needs to aquire input both from keyboard and file
    # as before, use capital i (input from keyboard) and capital f (input from file) to choose which input type will follow
    # after input type choice
    # read two lines 
    # first line is pattern 
    # second line is text in which to look for pattern 

    FI = input().rstrip()
    if "I" in FI:
        pattern = input().rstrip()
        text = input().rstrip()
    if "F" in FI:
        test_file = "tests/06"
        with open(test_file) as file:
            pattern = file.readline().rstrip()
            text = file.readline().rstrip()
    
    # return both lines in one return
    # this is the sample return, notice the rstrip function
    return (pattern, text)

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    # this function should find the occurances using Rabin Karp alghoritm 
    # and return an iterable variable
    pattern_len = len(pattern)
    text_len = len(text)
    hash_p = hash_t = 0
    Q = 256
    B = 13
    muliplier = 1
    occurrences = []

    for i in range(pattern_len):
        hash_p = (hash_p * B + ord(pattern[i])) % Q
        hash_t = (hash_t * B + ord(text[i])) % Q

    for i in range(pattern_len-1):
        muliplier = (muliplier * B) % Q
    
    for i in range(text_len - pattern_len + 1):
        if hash_p == hash_t:
            for j in range(pattern_len):
                if pattern[j] != text[i + j]:
                    break
            else:
                occurrences.append(i)
        if i < text_len - pattern_len:
            hash_t = (B * (hash_t - ord(text[i]) * muliplier) + ord(text[i + pattern_len])) % Q
            
    return occurrences

# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
