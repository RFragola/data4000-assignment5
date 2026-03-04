


def get_student_key():
    student_key = input("Student key: ")
    seed = sum(ord(ch) for ch in student_key.strip())
    return seed


def get_item_name():
    while True:
        name = input("Item name: ").strip()
        if name == "":
            print("Error: Item name cannot be empty. Please try again.")
        else:
            return name


def get_unit_price():
    while True:
        try:
            price = float(input("Unit price: $"))
            if price <= 0:
                print("Error: Unit price must be greater than 0. Please try again.")
            else:
                return price
        except ValueError:
            print("Error: Invalid price. Please enter a numeric value (e.g. 4.99).")


def get_quantity():
    while True:
        try:
            qty = int(input("Quantity: "))
            if qty < 1:
                print("Error: Quantity must be at least 1. Please try again.")
            else:
                return qty
        except ValueError:
            print("Error: Invalid quantity. Please enter a whole number (e.g. 2).")


def run_checkout():
    # Step 1: Student Key
    seed = get_student_key()

    # Step 2 & 4: Item Entry Loop with Running Totals 
    subtotal = 0.0
    total_units = 0

    print("Enter items one at a time. Type DONE as the item name when finished.\n")

    while True:
        print("--- New Item ---")
        name = get_item_name()

        if name.upper() == "DONE":
            break

        price = get_unit_price()
        qty = get_quantity()

        line_total = price * qty
        subtotal += line_total
        total_units += qty

        print(f"\nRunning Subtotal: ${subtotal:.2f}\nTotal Units: {total_units}\n")

    # Step 5: Discount Logic
    if total_units >= 10 or subtotal >= 100:
        discount_percent = 10
    else:
        discount_percent = 0

    discount_amount = subtotal * (discount_percent / 100)
    total = subtotal - discount_amount

    # Step 6: Seed-Based Member Perk
    if seed % 2 != 0:          # odd seed → $3.00 perk
        perk_applied = True
        total -= 3.00
    else:                      # even seed → no perk
        perk_applied = False

    # Total may never fall below $0.00
    if total < 0:
        total = 0.00

    # Step 7: Output
    print(f"\nSeed: {seed}")
    print(f"Units: {total_units}")
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Discount: {discount_percent}%")
    print(f"Perk applied: {'YES' if perk_applied else 'NO'}")
    print(f"Total: ${total:.2f}")



run_checkout()