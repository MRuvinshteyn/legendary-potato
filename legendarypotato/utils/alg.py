from random import *
import random
import arith
import sys

ops = ['+', '-', '*', '/']
valid_vars = "abcdfghjklmnpqrstvwxyz"

def make_alg_basic():
    i = randint(2,4)
    if(randint(0,1) == 0):
        expr = "x=" + arith.make_arith_basic(i)[0][1:]
    else:
        expr = "x=" + arith.make_arith_exp(i)[0]
    print(expr)
    return [expr,""]

def make_alg(diff):
    make_alg_basic()
    #make_alg_mult_vars()
    #make_alg_mult_lines()
    
def print_ret(ret):
    print("\nSolve:")
    print(ret[0])

    ret[0].replace("^", "**")
    print("Answer:")
    print(eval(ret[0]))

make_alg_basic()
