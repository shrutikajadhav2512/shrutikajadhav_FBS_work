# Write a program to calculate the total cost of painting. The interior of building with four
# equal sized walls.
wall_length = float(input("Enter length of wall (m): "))
wall_height = float(input("Enter height of wall (m): "))
cost_per_sqm = float(input("Enter painting cost per sq.m (Rs): "))
one_wall_area = wall_length * wall_height
total_area = 4 * one_wall_area
total_cost = total_area * cost_per_sqm
print(f"\nArea of 1 wall: {one_wall_area} sq.m")
print(f"Total paintable area (4 walls): {total_area} sq.m")
print(f"Total cost of painting: Rs {total_cost}")