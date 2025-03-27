def get_item():
    order = {}
    print("1) Cheese Burger")
    print("2) Fries")
    print("3) Soda")
    print("4) Ice Cream")
    print("5) Cookie")

    while True:
        input_get_item = int(input("Enter your choice: "))
        if input_get_item == 1:
            item = "Cheese Burger"
        elif input_get_item == 2:
            item = "Fries"
        elif input_get_item == 3:
            item = "Soda"
        elif input_get_item == 4:
            item = "Ice Cream"
        elif input_get_item == 5:
            item = "Cookie"
        else:
            print("Invalid input")
            continue

        if item in order:
            order[item] += 1
        else:
            order[item] = 1


        choice = input("Do you want anything else?(y/n): ").lower()
        if choice == "n":
            print("Your order:")
            for i, (item,quantity) in enumerate(order.items(), start=1):
                print(f"{i}. {quantity}x {item}")
            exit()
        else:
            continue



def welcome():
    print("======================")
    print("Welcome to McDonald's")
    print("======================")

if __name__ == "__main__":
    welcome()
    get_item()


