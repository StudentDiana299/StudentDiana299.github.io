

### START FUNCTION
def add_vehicle(vehicles, new_vehicle_params):
    # Insert your code here
    model , colour, horsepower, fuel_capacity = new_vehicle_params
    new_vehicle = {'model' : model, 'colour' : colour, 'horsepower' : horsepower,'fuel_capacity' : fuel_capacity }
    vehicles.append(new_vehicle)
    return vehicles
### END FUNCTION

input1 = existing_vehicles = [
    {'model': 'TX-130', 'colour': 'Green', 'horsepower': 150, 'fuel_capacity': 60},
    {'model': 'RX-850', 'colour': 'Red', 'horsepower': 120, 'fuel_capacity': 45}
]

new_vehicle =  ('SX-750', 'White', 180, 80)
add_vehicle(existing_vehicles, new_vehicle)

print(input1)
