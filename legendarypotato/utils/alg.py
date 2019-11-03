from random import *
import random
import arith
import sys

ops = ['+', '-', '*', '/']
valid_vars = "abcdfghjklmnpqrstvwyz"

def make_alg_basic():
    i = randint(2,4)
    expr = "x=" + arith.make_arith_basic(i)[0][1:]
    return [expr,""]

def make_alg_exp():
    i = randint(2,4)    
    expr = "x=" + arith.make_arith_exp(i)[0]
    return [expr,""]

def make_alg_vars(max_vars,v):
    num_vars = randint(2, max_vars)

    n = randint(0, 10)
    num_vars-=1
    expr = v + "=" + str(n)

    vvars = [char for char in valid_vars]
    random.shuffle(vvars)
    num_vvars = 0

    guaranteed_var = randint(1,num_vars)
    while(num_vars!=0):
        n = randint(0,10)
        i = randint(0,3)
        expr += ops[i] + str(n)
        rand = randint(-1,num_vvars)
        if(rand==num_vvars):
            num_vvars+=1
        if(rand != -1):
            if(n == 1):
                expr = expr[:-1] + vvars[rand]
            else:
                expr += vvars[rand]
        elif(num_vars==guaranteed_var and v == "x" and num_vvars == 0):
            print("guaranteed")
            rand = randint(0,num_vvars)
            num_vvars+=1
            if(n == 1):
                expr = expr[:-1] + vvars[rand]
            else:
                expr += vvars[rand]
        num_vars-=1
    return [expr,"",vvars[:num_vvars]]

def make_alg_mult_lines(line_nums):
    ret = make_alg_vars(5, "x")
    expr = ret[0] + "\n"
    vvars = ret[2]
    for i in range(line_nums):
        v = random.choice(vvars)
        expr += make_alg_vars(2, v)[0] + "\n"
        vvars.remove(v)
        if(len(vvars) == 0):
            break
    return [expr,""]
    
def make_alg(diff):
    #beginner
    if(diff == 0):
        if(randint(0,1) == 0):
            return make_alg_basic()
        else:
            return make_alg_exp()
    if(diff == 1):
        return make_alg_vars(4,"x")
    if(diff == 2):
        return make_alg_mult_lines(3)

print(make_alg(2)[0])
