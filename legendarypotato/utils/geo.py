from random import *
import random
import sys
import math
'''
degrees to radians, vice versa
area/surface area/volume
find missing angle

equations of lines/circles

basic trig w/ triangles
proportions w/ similar triangles

pythagorean theorem
'''

def make_geo(diff):
    #beg
    if(diff == 0):
        i = randint(0,3)
        if(i == 0):
            return make_area()
        if(i == 1):
            return make_volume()
        if(i == 2):
            return make_deg_to_rad()
        if(i == 3):
            return make_rad_to_deg()

    #intimm
    if(diff == 1):
        i = randint(0,2)
        if(i == 0):
            return make_surf_area()
        if(i == 1):
            return make_sim()
        if(i == 2):
            return make_pyth_thm()
        
    #exp
    if(diff == 2):
        i = randint(0,2)
        if(i == 0):
            return make_eq_line()
        if(i == 1):
            return make_eq_circle()
        if(i == 2):
            return make_trig_q()
    
spec_angles = [0,30,45,60,90]

def make_deg_to_rad():
    deg = spec_angles[randint(0,4)]*randint(0,4)
    rad = math.radians(deg)/math.pi

    rad = round(rad,2)
    deg = round(deg, 2)

    question = "Convert from degrees to radians: " + str(deg)
    answer = deg
    return [question,answer]

    
def make_rad_to_deg():
    deg = spec_angles[randint(0,4)]*randint(0,4)
    rad = math.radians(deg)/math.pi
    deg = rad*math.pi

    rad = round(rad,2)
    deg = round(deg, 2)
    question = "Convert from radians to degrees: " + str(rad)
    answer = deg

    return [question,answer]

def make_area():

    shape_type = randint(0,2)

    question = ""
    answer = ""
    
    #circle
    if(shape_type == 0):
        radius = randint(0,25)
        question = "Find the area of a circle with radius " + str(radius)
        answer = str(radius*radius)+"pi"
        
    #triangle
    if(shape_type == 1):
        base = randint(1,25)
        height = randint(1,25)
        question = "Find the area of a triangle with base " + str(base) + " and height " + str(height)
        answer = base*height/2

    #quadrilateral
    if(shape_type == 2):
        #parallelogram (rectangle)
        if(randint(0,1) == 0):
            height = randint(1,25)
            width = randint(1,25)
            question = "Find the area of a rectangle with height " + str(height) + " and width " + str(width)
            answer = height*width
        #trapezoid
        else:
            base1 = randint(1,25)
            base2 = randint(1,25)
            height = randint(1,25)
            question = "Find the area of a trapezoid with base lengths " + str(base1) + " and " + str(base2) + ", and height " + str(height)
            answer = 0.5*height*(base1+base2)
    return [question,answer]

def make_volume():
    shape_type = randint(0,5)
    #sphere
    if(shape_type == 0):
        radius = randint(1,10)
        question = "Find the volume of a sphere with radius " + str(radius)
        answer = str((radius**3)*4/3)+"pi"
    #cone
    if(shape_type == 1):
        radius = randint(1,10)
        height = randint(1,10)
        question = "Find the volume of a cone with radius " + str(radius) + " and height " + str(height)
        answer = str(radius*radius*height/3)+"pi"
    #cube
    if(shape_type == 2):
        side = randint(1,10)
        question = "Find the volume of a cube with side length " + str(side)
        answer = side**3
    #cylinder
    if(shape_type == 3):
        radius = randint(1,10)
        height = randint(1,10)
        question = "Find the volume of a cylinder with radius " + str(radius) + " and height " + str(height)
        answer = str(radius*radius*height)+"pi"
    #triangular prisms
    if(shape_type == 4):
        base = randint(1,10)
        height1 = randint(1,10)
        height2 = randint(1,10)
        question = "Find the volume of a triangular prism with height " + str(height2) + " and a base with base " + str(base) + " and height " + str(height1)
        answer = base*height1*height2/2
    #rectangular prisms
    if(shape_type == 5):
        height = randint(1,10)
        width = randint(1,10)
        depth = randint(1,10)
        question = "Find the volume of a rectangular prism with height %d, width %d, and depth %d" %(height, width, depth)
        answer = height*width*depth

    return [question, answer]

def make_surf_area():
    shape_type = randint(0,4)
    #sphere
    if(shape_type == 0):
        radius = randint(1,10)
        question = "Find the surface area of a sphere with radius " + str(radius)
        answer = str(4*radius*radius)+"pi"
    #cone
    if(shape_type == 1):
        radius = randint(1,10)
        height = randint(1,10)
        question = "Find the surface area of a cone with radius " + str(radius) + " and height " + str(height)
        answer = str(radius*(radius+math.sqrt(height*height+radius*radius)))+"pi"
    #cube
    if(shape_type == 2):
        side = randint(1,10)
        question = "Find the surface area of a cube with side length " + str(side)
        answer = 6*side*side
    #cylinder
    if(shape_type == 3):
        radius = randint(1,10)
        height = randint(1,10)
        question = "Find the surface area of a cylinder with radius " + str(radius) + " and height " + str(height)
        answer = str(2*radius*(radius+height))+"pi"
    #rectangular prisms
    if(shape_type == 4):
        height = randint(1,10)
        width = randint(1,10)
        depth = randint(1,10)
        question = "Find the surface area of a rectangular prism with height %d, width %d, and depth %d" %(height, width, depth)
        answer = 2*(height*width + height*depth + width*depth)
    return [question,answer]

def mk_str(i):
    if(i > 0):
        return "+ " + str(i) + " " 
    elif(i < 0):
        return "- " + str(i*-1) + " "
    else:
        return ""
        
def make_eq_line():
    #given 2 points
    if(randint(0,1) == 0):
        pt1 = [randint(-10,10), randint(-10,10)]
        pt2 = [randint(-10,10), randint(-10,10)]
        m = (pt2[1]-pt1[1])/(pt2[0]-pt1[0])
        while(pt2[0] - pt1[0] == 0 and isinstance(m,int)):
            pt2 = [randint(-10,10),randint(-10,10)]
            m = (pt2[1]-pt1[1])/(pt2[0]-pt1[0])
        question = "Find the equation of a line containing the points (%d,%d) and (%d,%d). Leave it in point-slope form." %(pt1[0],pt1[1], pt2[0],pt2[1])
        answer1 = "y %s= %f (x %s)" %(mk_str(pt1[0]), m, mk_str(pt1[1]))
        answer2 = "y %s= %f (x %s)" %(mk_str(pt2[0]), m, mk_str(pt2[1]))
        return [question, answer1, answer2]
    #given m,b
    else:
        m = randint(-25,25)
        b = randint(-25,25)
        question = "Find the equation of a line with slope " + str(m) + " and a y-intercept of " + str(b)
        answer = "y = (%d)x %s" %(m,mk_str(b))
        return [question, answer]
        
def make_eq_circle():
    cx = randint(-25,25)
    cy = randint(-25,25)
    radius = randint(1,25)
    question = "Find the equation of a circle with center (%d,%d) and radius %d" %(cx,cy,radius)
    answer = "(x %s)^2 + (y %s)^2 = %d" %(mk_str(-cx),mk_str(-cy), radius*radius)
    return [question,answer]

pythag_trips = [[3,4,5],[5,12,13],[7,24,25]]
trig = ["sin", "cos", "tan"]
def make_trig_q():
    quest_type = randint(0,2)
    trig_type = trig[randint(0,2)]
    ang = ['A','B','C']
    random.shuffle(ang)
    while(ang[1] == 'C'):
        random.shuffle(ang)
    angle = ang[0]+ang[1]+ang[2]
        
    opp = adj = hyp = 'c'
    if(ang[1] == 'A'):
        opp = 'a'
        adj = 'b'
    if(ang[1] == 'B'):
        opp = 'b'
        adj = 'a'

    frac = ""
    if(trig_type == "sin"):
        frac = opp + "/" + hyp
    if(trig_type == "cos"):
        frac = adj + "/" + hyp
    if(trig_type == "tan"):
        frac = opp + "/" + adj

    question = ""
    answer = ""
    
    #find sin/cos/tan of an angle
    if(quest_type==0):        
        question = "Given a right triangle ABC, with AB=c,AC=b,and BC=a, and the hypotenuse being c, what is the %s of angle %s?" %(trig_type,angle)
        answer = frac
    #find what operation of given angle = side1/side2
    if(quest_type==1):
        question = "Given a right triangle ABC, with AB=c,AC=b,and BC=a, and the hypotenuse being c, which of the following operations (sin,cos,tan) of angle %s gives us %s?" %(angle, frac)
        answer = trig_type        
    #find what angle st sin/cos/tan angle = side1/side2
    if(quest_type==2):
        question = "\nGiven a right triangle ABC, with AB=c,AC=b,and BC=a, and the hypotenuse being c, the %s of what angle gives us %s?" %(trig_type, frac)
        answer1 = angle
        answer2 = angle[::-1]
        return [question,answer1,answer2]
    return [question,answer]

def make_sim():
    #given 3 sides
    ang1 = ['A','B','C']
    random.shuffle(ang1)
    side1 = ang1[0]+ang1[1]
    random.shuffle(ang1)
    side2 = ang1[0]+ang1[1]
    while(side1==side2):
        random.shuffle(ang1)
        side2 = ang1[0]+ang1[1]
            
    side1_size = randint(1,10)
    side2_size = randint(1,10)
    scale = round(random.uniform(0.0,10.0), 1)
            
    sim_side1 = chr(ord(side1[0])+3) + chr(ord(side1[1])+3)
    sim_side2 = chr(ord(side2[0])+3) + chr(ord(side2[1])+3)
    sim_side1_size = round(side1_size*scale,2)
    sim_side2_size = round(side1_size*scale,2)

    question = ""
    if(randint(0,1) == 0):
        question = "Given two similar right triangles, ABC and DEF, and %s=%d, %s=%d, %s=%d, what is %s?" %(side1,side1_size, side2,side2_size, sim_side1,sim_side1_size, sim_side2)
    #given the scaling proportion
    else:
        if(randint(0,1) == 0):
            prop = side1 + "/" + sim_side1
        else:
            prop = side2 + "/" + sim_side2
        question = "Given two similar right triangles, ABC and DEF, and %s=%d, %s=%d, and %s=%.1f, what is %s?" %(side1,side1_size, side2,side2_size, prop, scale, sim_side2)
    answer = sim_side2_size
    return [question,answer]
    
def make_pyth_thm():
    i = randint(0,2)
    trips = pythag_trips[i]
    if(i == 0):
        mult = randint(1,10)
        trips[0] *= mult
        trips[1] *= mult
        trips[2] *= mult
    if(i == 1):
        mult = randint(1,5)
        trips[0] *= mult
        trips[1] *= mult
        trips[2] *= mult
        
    question = "Find the hypotenuse of a triangle with base " + str(trips[0]) + " and height " + str(trips[1])
    answer = trips[2]
    return [question,answer]

if(len(sys.argv) == 1):
    for diff in range(3):
        i = 10
        while( i != 0):
            ret = make_geo(diff)
            print()
            print(ret[0] + "\nANSWER: " + str(ret[1]))
            i-=1
        print()
        print("=============================================================")
        print()
    
else:
    i = 10
    while( i != 0):
        ret = make_geo(int(sys.argv[1]))
        print()
        print(ret[0] + "\nANSWER: " + str(ret[1]))
        i-=1

