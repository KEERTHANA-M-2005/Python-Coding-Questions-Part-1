#  Refer to Fresher Profiles – Student agreement and write a program to
# calculate the placement assistance fee a student would pay based on the CTC
# and placement drive type. 

print("Placement Drive Types: Normal / Premium")
drive_type = input("Enter placement drive type: ").strip().lower()
ctc = float(input("Enter CTC (in LPA): "))

fee_percentage = 0

# Sample fee structure
if drive_type == "normal":
    if ctc <= 5:
        fee_percentage = 5
    elif ctc <= 10:
        fee_percentage = 7
    else:
        fee_percentage = 8

elif drive_type == "premium":
    if ctc <= 5:
        fee_percentage = 8
    elif ctc <= 10:
        fee_percentage = 10
    else:
        fee_percentage = 12
else:
    print("Invalid drive type entered.")
    exit()


fee_amount = (ctc * 100000 * fee_percentage) / 100  # converting LPA to actual ₹

print(f"\n--- Placement Assistance Fee Details ---")
print(f"CTC: ₹{ctc:.2f} LPA")
print(f"Drive Type: {drive_type.capitalize()}")
print(f"Fee Percentage: {fee_percentage}%")
print(f"Fee Amount: ₹{fee_amount:,.2f}")
