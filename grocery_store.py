# Sample initial products
products = [
    {"id": 101, "name": "Milk", "category": "Dairy", "price": 250, "stock": 20},
    {"id": 102, "name": "Bread", "category": "Bakery", "price": 120, "stock": 15},
    {"id": 103, "name": "Eggs", "category": "Dairy", "price": 300, "stock": 4},
    {"id": 104, "name": "Rice", "category": "Grains", "price": 350, "stock": 25},
    {"id": 105, "name": "Cooking Oil", "category": "Oils", "price": 1800, "stock": 8}
]

# List to store completed sales
sales_records = []


def find_product_by_id(product_id):
    for product in products:
        if product["id"] == product_id:
            return product
    return None


def add_new_product():
    print("\n--- Add New Product ---")
    try:
        product_id = int(input("Enter Product ID: ").strip())
    except ValueError:
        print("Invalid ID. Must be a number.")
        return

    # Check for duplicate ID
    if find_product_by_id(product_id) is not None:
        print("A product with this ID already exists.")
        return

    name = input("Enter Product Name: ").strip()
    if not name:
        print("Product name cannot be empty.")
        return

    category = input("Enter Category: ").strip()
    if not category:
        print("Category cannot be empty.")
        return

    try:
        price = float(input("Enter Price: ").strip())
        stock = int(input("Enter Available Stock: ").strip())
        if price <= 0 or stock < 0:
            print("Price must be greater than 0 and stock cannot be negative.")
            return
    except ValueError:
        print("Invalid price or stock value.")
        return

    # Add product to list as a dictionary
    new_product = {
        "id": product_id,
        "name": name,
        "category": category,
        "price": price,
        "stock": stock
    }
    products.append(new_product)
    print(f"Product '{name}' added successfully.")


def view_all_products():
    print("\n--- Available Products ---")
    if not products:
        print("No products available.")
        return

    print(f"{'ID':<6} {'Name':<18} {'Category':<15} {'Price':<10} {'Stock':<6}")
    print("-" * 55)
    for p in products:
        print(f"{p['id']:<6} {p['name']:<18} {p['category']:<15} {p['price']:<10.2f} {p['stock']:<6}")


def search_product():
    print("\n--- Search Product ---")
    query = input("Enter Product ID or Name: ").strip().lower()

    found = False
    for p in products:
        if str(p["id"]) == query or query in p["name"].lower():
            if not found:
                print(f"{'ID':<6} {'Name':<18} {'Category':<15} {'Price':<10} {'Stock':<6}")
                print("-" * 55)
                found = True
            print(f"{p['id']:<6} {p['name']:<18} {p['category']:<15} {p['price']:<10.2f} {p['stock']:<6}")

    if not found:
        print("Product not found.")


def update_product_stock():
    print("\n--- Update Product Stock ---")
    try:
        product_id = int(input("Enter Product ID: ").strip())
    except ValueError:
        print("Invalid ID.")
        return

    product = find_product_by_id(product_id)
    if not product:
        print("Product not found.")
        return

    print(f"Current stock for {product['name']}: {product['stock']}")
    print("1. Add to existing stock")
    print("2. Set new stock quantity")
    choice = input("Choose an option (1/2): ").strip()

    try:
        if choice == "1":
            qty = int(input("Enter quantity to add: ").strip())
            if qty < 0:
                print("Quantity cannot be negative.")
                return
            product["stock"] += qty
        elif choice == "2":
            new_stock = int(input("Enter new stock quantity: ").strip())
            if new_stock < 0:
                print("Stock cannot be negative.")
                return
            product["stock"] = new_stock
        else:
            print("Invalid option.")
            return

        print(f"Updated stock for {product['name']}: {product['stock']}")
    except ValueError:
        print("Invalid quantity entered.")


def process_customer_sale():
    print("\n--- Process Customer Sale ---")
    try:
        product_id = int(input("Enter Product ID: ").strip())
    except ValueError:
        print("Invalid ID.")
        return

    product = find_product_by_id(product_id)
    if not product:
        print("Product not found.")
        return

    if product["stock"] <= 0:
        print(f"'{product['name']}' is out of stock.")
        return

    try:
        quantity = int(input(f"Enter quantity to buy (Available: {product['stock']}): ").strip())
        if quantity <= 0:
            print("Quantity must be greater than zero.")
            return
    except ValueError:
        print("Invalid quantity.")
        return

    # Check available stock
    if quantity > product["stock"]:
        print(f"Cannot complete sale. Only {product['stock']} units available.")
        return

    total_amount = product["price"] * quantity
    product["stock"] -= quantity

    # Record the sale
    sale = {
        "id": product["id"],
        "name": product["name"],
        "quantity": quantity,
        "total_amount": total_amount
    }
    sales_records.append(sale)

    # Display receipt
    print("\n--- Purchase Summary ---")
    print(f"Product: {product['name']}")
    print(f"Unit Price: {product['price']:.2f}")
    print(f"Quantity: {quantity}")
    print(f"Total Amount: {total_amount:.2f}")
    print(f"Remaining Stock: {product['stock']}")


def view_sales_records():
    print("\n--- Sales Records ---")
    if not sales_records:
        print("No sales recorded yet.")
        return

    print(f"{'#':<4} {'ID':<6} {'Name':<18} {'Qty':<6} {'Total Amount':<12}")
    print("-" * 48)
    for idx, sale in enumerate(sales_records, 1):
        print(f"{idx:<4} {sale['id']:<6} {sale['name']:<18} {sale['quantity']:<6} {sale['total_amount']:<12.2f}")


def generate_store_report():
    print("\n--- Store Report ---")
    total_products = len(products)
    total_stock = sum(p["stock"] for p in products)
    total_sales = len(sales_records)
    total_revenue = sum(s["total_amount"] for s in sales_records)

    print(f"Total Products: {total_products}")
    print(f"Total Available Stock: {total_stock}")
    print(f"Total Sales Transactions: {total_sales}")
    print(f"Total Revenue: {total_revenue:.2f}")

    if products:
        highest = max(products, key=lambda p: p["price"])
        lowest = min(products, key=lambda p: p["price"])
        print(f"Highest Price Product: {highest['name']} ({highest['price']:.2f})")
        print(f"Lowest Price Product: {lowest['name']} ({lowest['price']:.2f})")

    # Products with stock below 5 units
    low_stock = [p for p in products if p["stock"] < 5]
    print("\nProducts with stock below 5 units:")
    if low_stock:
        for p in low_stock:
            print(f"- {p['name']} (ID: {p['id']}, Stock: {p['stock']})")
    else:
        print("None")


def main():
    while True:
        print("\n====================================")
        print("SMART GROCERY STORE SYSTEM")
        print("====================================")
        print()
        print("1. Add New Product")
        print("2. View All Products")
        print("3. Search Product")
        print("4. Update Product Stock")
        print("5. Process Customer Sale")
        print("6. View Sales Records")
        print("7. Generate Store Report")
        print("8. Exit")
        print()

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_new_product()
        elif choice == "2":
            view_all_products()
        elif choice == "3":
            search_product()
        elif choice == "4":
            update_product_stock()
        elif choice == "5":
            process_customer_sale()
        elif choice == "6":
            view_sales_records()
        elif choice == "7":
            generate_store_report()
        elif choice == "8":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice, please select between 1 and 8.")


if __name__ == "__main__":
    main()
