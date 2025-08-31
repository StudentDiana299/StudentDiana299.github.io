weekly_collection = [340, 220, 455, 300, 385, 520, 410]
total_waste_collected = 0
for daily_collection in weekly_collection:
        total_waste_collected += daily_collection
print(f"Total waste collected over the week: {total_waste_collected} kg")


endangered_species = ['Tiger', 'Blue Whale', 'Mountain Gorilla']
sightings = ['Deer', 'Tiger', 'Blue Whale', 'Mountain Gorilla', 'Elephant']
for species in sightings:
    if species in endangered_species:
       break
print(f"Endangered species spotted: {species}")


forest_area = 1000 # Initial forest area in square kilometres
growth_rate = 1.05 # 5% annual growth
year = 0
while forest_area < 1500:
    year += 1
    forest_area *= growth_rate
    print(f"Forest area after {year} years: {forest_area:.2f} sq km")