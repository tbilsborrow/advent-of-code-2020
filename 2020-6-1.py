import sys

# fun with generators

def multilinereader(lines):
    '''concats multiple lines into one, generating new one upon blank line'''
    concat = ''
    for line in lines:
        if len(line.strip()) == 0:
            if len(concat) > 0:
                yield concat
            concat = ''
        concat += line.strip()
    if len(concat) > 0:
        yield concat

def chars(lines):
    '''generates a set of chars in each input string'''
    for line in lines:
        yield {ch for ch in line}

print(sum((len(s) for s in chars(multilinereader(sys.stdin)))))
