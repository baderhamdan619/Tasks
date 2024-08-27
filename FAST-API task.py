# main.py

from typing import Optional, List
from pydantic import BaseModel
from fastapi import FastAPI, HTTPException

app = FastAPI()

# Define the data model for a Car
class Car(BaseModel):
    name: str
    model: str
    year: int
    price: float

# In-memory storage for cars
cars_db = []

@app.post("/cars/", response_model=Car)
def create_car(car: Car):
    car_id = len(cars_db) + 1
    car_data = car.dict()
    car_data["id"] = car_id
    cars_db.append(car_data)
    return car_data

@app.get("/cars/", response_model=List[Car])
def read_cars():
    return cars_db

@app.get("/cars/{car_id}", response_model=Car)
def read_car(car_id: int):
    for car in cars_db:
        if car["id"] == car_id:
            return car
    raise HTTPException(status_code=404, detail="Car not found")

@app.put("/cars/{car_id}", response_model=Car)
def update_car(car_id: int, updated_car: Car):
    for car in cars_db:
        if car["id"] == car_id:
            car.update(updated_car.dict())
            return car
    raise HTTPException(status_code=404, detail="Car not found")

@app.delete("/cars/{car_id}", response_model=Car)
def delete_car(car_id: int):
    for index, car in enumerate(cars_db):
        if car["id"] == car_id:
            deleted_car = cars_db.pop(index)
            return deleted_car
    raise HTTPException(status_code=404, detail="Car not found")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)