store = ()

def insert_car(car_name,model,price,quantity):
    global store

    new_car = (car_name,model,price,quantity)
    store = store + (new_car,)

    print("Car added successfully")


def view_all_cars():
    return store


def search_car(car_name):
    for car in store:
        if car[0] == car_name:
            return car

    return None


def update_car(car_name, new_price, new_quantity):
    global store

    for index, car in enumerate(store):
        if car[0] == car_name:

            new_car = (car_name,new_model,new_price,new_quantity)

            # Create a new tuple with the updated car
            store = store[:index] + (new_car,) + store[index + 1:]

            print("Car updated successfully")
            return

    print("Car not found")


def delete_car(car_name):
    global store

    for index, car in enumerate(store):
        if car[0] == car_name:

            # Create a new tuple without the deleted car
            store = store[:index] + store[index + 1:]

            print("Car deleted successfully")
            return

    print("Car not found")