# Write a program to generate a receipt based on the items sold in a pizza
# shop. The format of the receipt is as below
# ----------------------------------------------------------------
# Sr. No. Item Name Qty UoM Rate Sub-Total
# -------+------------------+------+------+-----------+-----------
# 1. + Cheesecake + 1.45 + Kg + 100.00 + 145.00
# 2. + Farmhouse Pizza + 3 + M + 1243.20 + 3729.80
# 3.
# ..
# n. + Garlic Bread + 2 + Num + 149.99 + 299.98
# -------+------------------+------+------+-----------+-----------
# TOTAL NNNNNN.NN 


# Pizza Shop Receipt Generator

items = []
n = int(input("Enter number of items sold: "))

for i in range(n):
    print(f"\nEnter details for item {i+1}:")
    name = input("Item Name: ")
    qty = float(input("Quantity: "))
    uom = input("Unit of Measure (Kg/M/Num): ")
    rate = float(input("Rate: "))
    sub_total = qty * rate
    items.append((i+1, name, qty, uom, rate, sub_total))

# Print receipt
print("-" * 64)
print(f"{'Sr. No.':<7} {'Item Name':<18} {'Qty':>5} {'UoM':>6} {'Rate':>11} {'Sub-Total':>11}")
print("-" * 64)

total = 0
for sr, name, qty, uom, rate, sub_total in items:
    print(f"{sr:<7} {name:<18} {qty:>5.2f} {uom:>6} {rate:>11.2f} {sub_total:>11.2f}")
    total += sub_total

print("-" * 64)
print(f"{'TOTAL':>53} {total:>11.2f}")
print("-" * 64)
