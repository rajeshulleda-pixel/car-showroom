
from fastapi import FastAPI
app = Fastapi()

@app.get("/cars")
def view_all_cars():
    return database.view_all_cars()
    
@app.post("/cars")
def insert_car(car_name,model,price,quantity):
    return database.insert_car(car_name,model,price,quantity)


@app.put("/cars/{car_name}")
def update_car(car_name,new_price,new_quantity):
    return database.update_car(car_name,new_price,new_quantity)

@app.get("/cars/{car_name}")
def search_car(car_name):
    return database.search_car(car_name)

@app.delete("/cars/{car_name}")
def delete_car(car_name):
    return database.delete_car(car_name)