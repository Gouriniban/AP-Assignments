def display_low_stock(product_list):

    print("\nProducts with Low Stock (Less than 10):")
    print("-" * 40)

    low_stock_found = False

    for product in product_list:

        if product["stock"] < 10:

            print(f"Product Name : {product['name']}")
            print(f"Stock        : {product['stock']}")
            print("-" * 40)

            low_stock_found = True

    if not low_stock_found:
        print("All products have sufficient stock.")


def edit_stock(product_list):

    choice = input("\nDo you want to edit stock? (yes/no): ")

    if choice.lower() == "yes":

        name = input("Enter product name to edit: ")

        found = False

        for product in product_list:

            if product["name"].lower() == name.lower():

                new_stock = int(input("Enter new stock value: "))

                product["stock"] = new_stock

                print("Stock updated successfully.")

                found = True
                break


        if not found:
            print("Product not found.")


def main():

    products = [

        {"name": "Laptop", "stock": 15},

        {"name": "Mouse", "stock": 19},

        {"name": "Keyboard", "stock": 12},

        {"name": "Monitor", "stock": 5},

        {"name": "Printer", "stock": 8}

    ]

    print("Product Inventory:")
    print("-" * 40)


    for product in products:

        print(f"{product['name']} : {product['stock']} units")


    edit_stock(products)

    print("\nUpdated Inventory:")
    print("-" * 40)


    for product in products:

        print(f"{product['name']} : {product['stock']} units")

    display_low_stock(products)

if __name__ == "__main__":
    main()
