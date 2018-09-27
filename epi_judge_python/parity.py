from test_framework import generic_test

# This is the basic solution, check every bit and update the parity if we run into 1
def parity_1(x):
    parity = 0
    while x:
        parity ^= (x & 1)
        x = x >> 1
    return parity

def parity_2(x):
    parity = 0
    while x:
        parity ^= 1
        x &= (x - 1)
    return parity

def parity(x):
    return parity_2(x)

if __name__ == '__main__':
    exit(generic_test.generic_test_main("parity.py", 'parity.tsv', parity))
