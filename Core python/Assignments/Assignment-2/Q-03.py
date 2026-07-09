# Convert distant given in feet and inches into meter and centimeter
# Input feet and inches
feet = float(input("Enter feet: "))
inches = float(input("Enter inches: "))
# calculations
meters = (feet * 0.3048) + (inches * 0.0254)
m=int(meters)
cm = (meters - m) * 100
# Display result
print(f' meters:{m} ,centimeter:{cm}')

