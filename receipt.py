item1_name = "Notebook"
item1_price = "4.99"
item1_qty = "2"

item2_name = "Pen Pack"
item2_price = "7.50"
item2_qty = "1"

item3_name = "Backpack"
item3_price = "34.99"
item3_qty = "1"

tax_rate = "0.075"   # 7.5% sales tax

# Conversion of strings to appropriate data types
notebook_price = float(item1_price) # converting string to float data type
notebook_qty = int(item1_qty)       # converting sring to integer data type

penpack_price = float(item2_price)  # converting string to float data type
penpack_qty = int(item2_qty)        # converting string to integer data type

backpack_price = float(item3_price) # converting string to float data type
backpack_qty = int(item3_qty)       # converting string to integer data type

ftax_rate = float(tax_rate) #ftax = float tax rate

# Calculate each item's price * quantity for subtotal
notebook_total = notebook_price * notebook_qty

penpack_total = penpack_price * penpack_qty

backpack_total = backpack_price * backpack_qty

receipt_subtotal = notebook_total + penpack_total + backpack_total

# Calculate tax for each line item
note_tax = notebook_total * ftax_rate

pen_tax = penpack_total * ftax_rate

back_tax = backpack_total * ftax_rate

receipt_tax = note_tax + pen_tax + back_tax

# Add subtotal to tax for Grand Total
note_grand_total = notebook_total + note_tax

pen_grand_total = penpack_total + pen_tax

back_grand_total = backpack_total + back_tax

# Print a formatted receipt that looks clean and professional. Use f-strings with :.2f for all dollar amounts.
print("=" * 40)
print("          STORE RECEIPT")
print("=" * 40)
print(f"Notebook     ${notebook_price} x {notebook_qty}     ${notebook_total}")
print(f"Pen Pack     ${penpack_price:.2f}  x {penpack_qty}    ${penpack_total:.2f}")
print(f"Backpack     ${backpack_price} x {backpack_qty}    ${backpack_total}")
print("_" * 40)

print(f"Subtotal                   ${receipt_subtotal}")
print(f"Tax ({ftax_rate}):               ${receipt_tax:.2f}")
print("=" * 40)

print(f"TOTAL:                     ${receipt_subtotal + receipt_tax:.2f}")
print("=" * 40)
