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

def make_trig():
    make_deg_to_rad()
    make_rad_to_deg()

    make_area()
    make_volume()
    make_surf_area()

    make_eq_line()
    make_eq_circle()

    make_trig_q()
    make_sim()

    make_pyth_thm()

spec_angles = [0,30,45,60,90]

def make_deg_to_rad():
    deg = spec_angles[randint(0,4)]*randint(0,4)
    rad = math.radians(deg)/math.pi

    print("\nConvert from degrees to radians: ")
    print(deg)
    print("Answer:")
    print(rad)

def make_rad_to_deg():
    deg = spec_angles[randint(0,4)]*randint(0,4)
    rad = math.radians(deg)/math.pi

    print("\nConvert from radians to degrees: ")
    print(rad)
    print("Answer:")
    print(deg)

def make_area():
    shape_type = randint(0,2)
    
    #circle
    if(shape_type == 0):
        radius = randint(0,25)
        print("\nFind the area of a circle with radius " + str(radius))
        print("Answer:")
        print(str(radius*radius)+"pi")
        
    #triangle
    if(shape_type == 1):
        base = randint(1,25)
        height = randint(1,25)
        print("\nFind the area of a triangle with base " + str(base) + " and height " + str(height))
        print("Answer:")
        print(base*height/2)

    #quadrilateral
    if(shape_type == 2):
        #parallelogram (rectangle)
        if(randint(0,1) == 0):
            height = randint(1,25)
            width = randint(1,25)
            print("\nFind the area of a rectangle with height " + str(height) + " and width " + str(width))
            print("Answer:")
            print(height*width)
        #trapezoid
        else:
            base1 = randint(1,25)
            base2 = randint(1,25)
            height = randint(1,25)
            print("\nFind the area of a trapezoid with base lengths " + str(base1) + " and " + str(base2) + ", and height " + str(height))
            print("Answer:")
            print(0.5*height*(base1+base2))

def make_volume():
    shape_type = randint(0,5)
    #sphere
    if(shape_type == 0):
        radius = randint(1,10)
        print("\nFind the volume of a sphere with radius " + str(radius))
        print("Answer:")
        print(str((radius**3)*4/3)+"pi")
    #cone
    if(shape_type == 1):
        radius = randint(1,10)
        height = randint(1,10)
        print("\nFind the volume of a cone with radius " + str(radius) + " and height " + str(height))
        print("Answer:")
        print(str(radius*radius*height/3)+"pi")
    #cube
    if(shape_type == 2):
        side = randint(1,10)
        print("\nFind the volume of a cube with side length " + str(side))
        print("Answer:")
        print(side**3)
    #cylinder
    if(shape_type == 3):
        radius = randint(1,10)
        height = randint(1,10)
        print("\nFind the volume of a cylinder with radius " + str(radius) + " and height " + str(height))
        print("Answer:")
        print(str(radius*radius*height)+"pi")
    #triangular prisms
    if(shape_type == 4):
        base = randint(1,10)
        height1 = randint(1,10)
        height2 = randint(1,10)
        print("\nFind the volume of a triangular prism with height " + str(height2) + " and a base with base " + str(base) + " and height " + str(height1))
        print("Answer:")
        print(base*height1*height2/2)
    #rectangular prisms
    if(shape_type == 5):
        height = randint(1,10)
        width = randint(1,10)
        depth = randint(1,10)
        print("\nFind the volume of a rectangular prism with height %d, width %d, and depth %d" %(height, width, depth))
        print("Answer:")
        print(height*width*depth)
        
def make_surf_area():
    shape_type = randint(0,4)
    #sphere
    if(shape_type == 0):
        radius = randint(1,10)
        print("\nFind the surface area of a sphere with radius " + str(radius))
        print("Answer:")
        print(str(4*radius*radius)+"pi")
    #cone
    if(shape_type == 1):
        radius = randint(1,10)
        height = randint(1,10)
        print("\nFind the surface area of a cone with radius " + str(radius) + " and height " + str(height))
        print("Answer:")
        print(str(radius*(radius+math.sqrt(height*height+radius*radius)))+"pi")
    #cube
    if(shape_type == 2):
        side = randint(1,10)
        print("\nFind the surface area of a cube with side length " + str(side))
        print("Answer:")
        print(6*side*side)
    #cylinder
    if(shape_type == 3):
        radius = randint(1,10)
        height = randint(1,10)
        print("\nFind the surface area of a cylinder with radius " + str(radius) + " and height " + str(height))
        print("Answer:")
        print(str(2*radius*(radius+height))+"pi")
    #rectangular prisms
    if(shape_type == 4):
        height = randint(1,10)
        width = randint(1,10)
        depth = randint(1,10)
        print("\nFind the surface area of a rectangular prism with height %d, width %d, and depth %d" %(height, width, depth))
        print("Answer:")
        print(2*(height*width + height*depth + width*depth))

def make_eq_line():
    #given 2 points
    if(randint(0,1) == 0):
        pt1 = [randint(-25,25), randint(-25,25)]
        pt2 = [randint(-25,25), randint(-25,25)]
        while(pt2[0] - pt1[0] == 0):
            pt2[0] = randint(-25,25)
        m = (pt2[1]-pt1[1])/(pt2[0]-pt1[0])
        print("\nFind the equation of a line containing the points (%d,%d) and (%d,%d). Leave it in point-slope form." %(pt1[0],pt1[1], pt2[0],pt2[1]))
        print("Answer:")
        print("y - (%d) = %f (x - (%d))" %(pt1[1], m, pt1[0]))
        print("OR:")
        print("y - (%d) = %f (x - (%d))" %(pt2[1], m, pt2[0]))
    #given m,b
    else:
        m = randint(-25,25)
        b = randint(-25,25)
        print("\nFind the equation of a line with slope " + str(m) + " and a y-intercept of " + str(b))
        print("Answer:")
        if(b > 0):
            print("y = (%d)x + %d" %(m,b))
        else:
            print("y = (%d)x %d" %(m,b))
        
def make_eq_circle():
    cx = randint(-25,25)
    cy = randint(-25,25)
    radius = randint(1,25)
    print("\nFind the equation of a circle with center (%d,%d) and radius %d" %(cx,cy,radius))
    print("Answer:")
    print("(x - %d)^2 + (y - %d)^2 = %d" %(cx,cy, radius*radius))

#basic trig w/ triangles
#proportions w/ similar triangles

#pythagorean theorem
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
        
    #find sin/cos/tan of an angle
    if(quest_type==0):        
        print("\nGiven a right triangle ABC, with AB=c,AC=b,and BC=a, and the hypotenuse being c, what is the %s of angle %s?" %(trig_type,angle))
        print("Answer:")
        print(frac)
    #find what operation of given angle = side1/side2
    if(quest_type==1):
        print("\nGiven a right triangle ABC, with AB=c,AC=b,and BC=a, and the hypotenuse being c, which of the following operations (sin,cos,tan) of angle %s gives us %s?" %(angle, frac))
        print("Answer:")
        print(trig_type)        
    #find what angle st sin/cos/tan angle = side1/side2
    if(quest_type==2):
        print("\nGiven a right triangle ABC, with AB=c,AC=b,and BC=a, and the hypotenuse being c, the %s of what angle gives us %s?" %(trig_type, frac))
        print("Answer:")
        print(angle + " or " + angle[::-1])

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
    if(randint(0,1) == 0):
        print("\nGiven two similar right triangles, ABC and DEF, and %s=%d, %s=%d, %s=%d, what is %s?" %(side1,side1_size, side2,side2_size, sim_side1,sim_side1_size, sim_side2))
    #given the scaling proportion
    else:
        if(randint(0,1) == 0):
            prop = side1 + "/" + sim_side1
        else:
            prop = side2 + "/" + sim_side2
        print("\nGiven two similar right triangles, ABC and DEF, and %s=%d, %s=%d, and %s=%.1f, what is %s?" %(side1,side1_size, side2,side2_size, prop, scale, sim_side2))
    print("Answer:")
    print(sim_side2_size)
    

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
        
    print("\nFind the hypotenuse of a triangle with base " + str(trips[0]) + " and height " + str(trips[1]))
    print("Answer:")
    print(trips[2])



make_trig()
