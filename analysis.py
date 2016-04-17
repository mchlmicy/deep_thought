def observe(line):
    ''' Read a given string and derive numeric observations.
        Parameters: str(line)
        Returns: list(int(observations))
    '''
    observations = [ \
        len(line), # number of characters
        len(line) % 2, # odd/eveness number of characters
        ',' in line, # , in string
        ':' in line, # : in string
        ';' in line, # ; in string
        '.' in line, # . in string
        '!' in line, # ! in string
        '?' in line, # ? in string
    ]
    observations.extend(utility_cap_analysis(line)) # cap / lower counts
    return observations

def utility_cap_analysis(line):
    ''' Count the number of capital and lowercase letters.
        Parameters: str(line)
        Returns: list(int(num_lower), int(num_caps))
    '''
    lower, caps = 0, 0
    for char in line:
        if 65 >= ord(char) <= 90:
            caps += 1
        elif 97 >= ord(char) <= 122:
            lower += 1
    return lower, caps
