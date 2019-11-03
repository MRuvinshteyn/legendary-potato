from random import *
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

spec_angles = [0,30,45,60,90]
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
    print()

def make_volume():
    print()

def make_surf_area():
    print()


def make_eq_line():
    print()

def make_eq_circle():
    print()


def make_trig_q():
    print()

def make_sim():
    print()


def make_pyth_thm():
    print()



make_trig()
