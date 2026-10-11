# A farmer has a field which is half in circle share and rest rectangle. He needs to do fencing
# for entire field using barbed wire 5 times. Circular section has radius 20m and rectangle
# length is 50 m and breadth is 40m. If cost of barbed wire is 35Rs/m then calculate the total
# cost of fencing the field.

import math
radius = 20      
length = 50     
breadth = 40     
cost_per_meter = 35 
times = 5
pi = 3.14
single_perimeter = (2 * length) + breadth + (pi * radius)
total_wire_needed = single_perimeter * times
total_cost = total_wire_needed * cost_per_meter
print(f"Single perimeter: {single_perimeter} m")
print(f"Total wire needed (5 times): {total_wire_needed} m")
print(f"Total cost of fencing: Rs {total_cost}")
single_perimeter_exact = (2*length) + breadth + (math.pi * radius)
total_cost_exact = single_perimeter_exact * times * cost_per_meter
print(f"\nWith exact pi value:")
print(f"Total cost: Rs {total_cost_exact:.2f}")