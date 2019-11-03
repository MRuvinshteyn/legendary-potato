from random import *
import sys

ops = ['+', '-', '*', '/']

def make_alg1(max_vars):
    num_vars = randint(2, max_vars)

    expr = ""
    
    while(num_vars!=0):
        n = randint(0, 100)
        i = randint(0,3)
        expr += str(n) + ops[i]
        num_vars-=1

    expr = expr[0:len(expr)-1]
    print_expr(expr)

def make_alg2(max_vars):
    num_vars = randint(2, max_vars)

    open_parenths = 0
    
    n = randint(0, 100)
    num_vars-=1
    expr = str(n)
    
    while(num_vars!=0):
        n = randint(0, 100)
        i = randint(0,5)
        
        
        #0-3 is basic operations
        if(i < 4):
            expr += ops[i] + str(n)
        #4 is ^
        elif(i == 4):
            expr += '^' + '(' + str(n)
            open_parenths+=1
        #5 is opening a parenthesis
        elif(i == 5):
            expr += '(' + str(n)
            open_parenths+=1

        #0 means closing parenths
        if(randint(0,1) == 0 and open_parenths != 0):
            expr += ')'
            open_parenths-=1
        num_vars-=1

    while(open_parenths != 0):
        expr += ')'
        open_parenths-=1
    print("\nSolve:")
    print(expr)
    #print_expr(expr)
    
def print_expr(expr):
    print("\nSolve:")
    for op in ops:
        expr = expr.replace(op, " "+op+" ")
    print(expr)
    

make_alg1(int(sys.argv[1]))
make_alg2(int(sys.argv[1]))
