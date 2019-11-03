from random import *
import sys

ops = ['+', '-', '*', '/']

#basic operations
def make_arith_basic(max_vars):

    num_vars = randint(2, max_vars)

    n = randint(0, 10)
    num_vars-=1
    expr = str(n)
    
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
    

#exponents + parenthe+sis
def make_arith_exp(max_vars):
    num_vars = randint(2, max_vars)

    open_parenths = 0
    
    n = randint(0, 10)
    num_vars-=1
    expr = str(n)
    
    while(num_vars!=0):
        n = randint(0, 10)
        i = randint(0,4)
        i2 = randint(0,1)
        
        tmp_expr = expr
        add_parenths = 0
                
        #0-3 is basic operations
        if(i < 4):
            if(ops[i] == '/' and n == 0):
                continue
            tmp_expr += ops[i] + '('*i2 + str(n)
            add_parenths = i2
        #4 is ^
        elif(i == 4):
            n = randint(-3, 3)
            tmp_expr += '**' + '(' + str(n)
            add_parenths=1

        #gives parenthesis
        if(eval(expr+(')'*open_parenths)) == 0 and i == 4):
            continue

        clos_paren = ')' * (open_parenths+add_parenths)
        ev = eval(tmp_expr+clos_paren)
        if(isinstance(ev, int)):
            expr = tmp_expr
            num_vars-=1
            open_parenths += add_parenths
            
                
        #0 means closing parenths
        if(randint(0,1) == 0 and open_parenths != 0):
            expr += ')'
            open_parenths-=1

    while(open_parenths != 0):
        expr += ')'
        open_parenths-=1

    expr.replace("**",'^')
    return [expr,""]

#fractional operations
def make_arith_frac(max_vars, same_dem):

    num_vars = randint(2, max_vars)

    n1 = randint(0, 10)
    n2 = randint(0, 10)
    while(n2 == 0):
        n2 = randint(0, 10)
    num_vars-=1
    expr = '(' + str(n1) + '/' + str(n2) + ')'

    last_div = False
    while(num_vars!=0):
        n1 = randint(0,10)
        if(last_div):
            while(n1 == 0):
                n1 = randint(0, 10)
        if(not same_dem):
            n2 = randint(0,10)
            while(n2 == 0):
                n2 = randint(0, 10)
        
        i = randint(0,3)
        if(same_dem):
            i = randint(0,1)
        expr += ops[i] + '(' + str(n1) + '/' + str(n2) + ')'
        if(ops[i] == '/'):
            last_div = True
        else:
            last_div = False
        num_vars-=1
            
    return [expr, ""]

def print_ret(ret):
    print("\nSolve:")
    print(ret[0])

    ret[0].replace("^", "**")
    print("Answer:")
    print(eval(ret[0]))

def make_arith():
    i = randint(0,3)
    n_vars = randint(2,5)
    if(i == 0):
        return make_arith_basic(n_vars)
    if(i == 1):
        return make_arith_exp(n_vars)
    if(i == 2):
        return make_arith_frac(n_vars, True)
    if(i == 3):
        return make_arith_frac(n_vars, False)
    
#print_ret(make_arith_basic(int(sys.argv[1])))
#print_ret(make_arith_exp(int(sys.argv[1])))
#print_ret(make_arith_frac(int(sys.argv[1]), True))
#print_ret(make_arith_frac(int(sys.argv[1]), False))
#print_ret(make_arith())
