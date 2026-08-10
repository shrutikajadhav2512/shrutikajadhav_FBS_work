# Calculate the cost of painting the following building’s walls (both interior and
# exterior). You need to accept area (one wall) and cost of both interior and
# exterior wall.
def paint(area_one_wall,no_of_walls,cost_interior,cost_exterior):
    
    total_area = area_one_wall * no_of_walls
    interior_cost = total_area * cost_interior
    exterior_cost = total_area * cost_exterior
    total_cost = interior_cost + exterior_cost
    print('total cost is',total_cost)
area_one_wall = float(input("area of one wall:"))
no_of_walls = int(input("Total walls: "))
cost_interior = float(input("Interior paint cost:"))
cost_exterior = float(input("Exterior paint cost:"))
paint(area_one_wall,no_of_walls,cost_interior,cost_exterior)

