
def take_order():
    items_ordered = []
    total_amount = 0

    while True:
        show_menu()
        try:
            choice = int(input("Enter your choice (1-8): "))
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue
        if choice == 9:
            break
        elif choice in [1, 2, 3, 4, 5,6,7,8]:
            quantity = int(input("Enter quantity: "))
            price = get_item_price(choice)
            amount = price * quantity
            item_name = [][choice - 1]
            items_ordered.append((item_name, quantity, amount))
            total_amount += amount
            print(f"Added to cart! Item total: ₹{amount}")
        else:
            print("Invalid choice. Try again!")

    return items_ordered, total_amount
def save_invoice(name, phone, address, items_ordered, total_amount):
    now = datetime.datetime.now()
    filename = f"invoice_{name}_{now.strftime('%Y%m%d_%H%M%S')}.txt"

    with open(filename, "w") as file:
        file.write("======= McDonald's Delivery Invoice =======\n")
        file.write(f"Date: {now.strftime('%d-%m-%Y %H:%M:%S')}\n")
        file.write(f"Customer Name: {name}\n")
        file.write(f"Phone: {phone}\n")
        file.write(f"Address: {address}\n")
        file.write("-------------------------------------------\n")
        file.write("Items Ordered:\n")

        for item_name, qty, amount in items_ordered:
            file.write(f"{item_name} x{qty} = ₹{amount}\n")

        file.write("-------------------------------------------\n")
        file.write(f"Total Bill: ₹{total_amount}\n")
        file.write("Thank you for ordering from McDonald's!\n")
        file.write("Your food will be delivered shortly 🍟🍔\n")

    print(f"\nInvoice generated and saved as '{filename}'")
    print("Thank you! Your order will be delivered soon 🚴‍♂️")
def main():
    name, phone, address = get_customer_details()
    items_ordered, total_amount = take_order()
    save_invoice(name, phone, address, items_ordered, total_amount)


if __name__ == "__main__":
    main()
