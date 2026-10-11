# A man goes for shopping. He buys 5 products. Accept the price of all products and display
# the total bill after adding 18% GST


total = 0

for i in range(1, 6):
    price = float(input(f"Enter price of product {i}: Rs "))
    total += price

gst_rate = 18
gst_amount = total * gst_rate / 100
final_bill = total + gst_amount

print(f"\nTotal without GST: Rs {total:.2f}")
print(f"GST (18%): Rs {gst_amount:.2f}")
print(f"Final Bill: Rs {final_bill:.2f}")