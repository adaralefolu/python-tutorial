import math

def number_of_can_needed (wall_height, wall_width, coverage_per_pan):
  area_of_wall = wall_height * wall_width
  number_of_can_needed = math.ceil (area_of_wall / coverage_per_pan)
  print (f"Number of can needed: {number_of_can_needed}")

wall_height = int(input("Enter height of wall: "))
wall_width = int(input("Enter width of wall: "))

number_of_can_needed (wall_height, wall_width, 4)
