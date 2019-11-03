from random import *
import random
import arith
import sys

ops = ['+', '-', '*', '/']
valid_vars = "abcdfghjklmnpqrstvwxyz"

def make_alg_basic():
    i = randint(2,4)
    expr = "x=" + arith.make_arith_basic(i)[0][1:]
    return [expr,""]

def make_alg_exp():
    i = randint(2,4)    
    expr = "x=" + arith.make_arith_exp(i)[0]
    return [expr,""]

def make_alg_vars(max_vars):
    num_vars = randint(2, max_vars)

    n = randint(0, 10)
    num_vars-=1
    expr = " " + str(n)
    
    while(num_vars!=0):
        n = randint(0,10)
        i = randint(0,3)
        temp_exp = expr + ops[i] + str(n)
        if(not (ops[i] == '/' and n == 0)):
            ev = eval(temp_exp)
            if(isinstance(ev, int)):
                expr = temp_exp
                num_vars-=1
    
    return [expr,""]
    
    
def make_alg(diff):
    make_alg_basic()
    #make_alg_vars()
    #make_alg_mult_lines()
    
def print_ret(ret):
    print("\nSolve:")
    print(ret[0])

    ret[0].replace("^", "**")
    print("Answer:")
    print(eval(ret[0]))

make_alg_basic()
