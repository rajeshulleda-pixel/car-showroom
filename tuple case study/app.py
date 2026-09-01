import database
user_choice="""
1.Add car
2.View all cars
3.Search car
4.Update car
5.Delete car
6.Exit

"""
def insert():
    car_name = input("Enter car name: ")
    model = input("Enter model: ")
    price = int(input("Enter price: "))
    quantity = int(input("Enter quantity: "))
    database.insert_car(car_name,model,price,quantity)

def view():
    print(database.view_all_cars())

def search():
    car_name = input("Enter car name: ")
    print(database.search_car(car_name))

def update():
    car_name = input("Enter car name: ")
    new_price = int(input("Enter new price: "))
    new_quantity = int(input("Enter new quantity: "))
    database.update_car(car_name,new_price,new_quantity)

def delete():
    car_name = input("Enter car name: ")
    database.delete_car(car_name)

if __name__ == "__main__":
    while True:
        print(user_choice)
        choice = input("Enter your choice: ")
        if choice == "1":
            insert()
        elif choice == "2":
            view()
        elif choice == "3":
            search()
        elif choice == "4":
            update()
        elif choice == "5":
            delete()
        elif choice == "6":
            break
        else:
            print("Invalid choice")

main()