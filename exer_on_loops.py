animals = ['Great White Shark', 'Blue Whale', 'African Elephant', 'Bald Eagle',
            'Orangutan', 'Tiger', 'Panda', 'Koala']
for animal in animals:
    print(animal)

i=0
while i<5 :
    print(i)
    i = i+1

for animal in animals:
    print(animal)
    if animal == 'Orangutan':
        print("Found the Orangutan")
        break
print(f"last animal was : {animal}")

for animal in animals:
       if animal == 'Bald Eagle':
        continue
       print(animal)
deforestation_rates = [150, 145, 140, 135, 130]
deforestation_years = [2010, 2011, 2012, 2013, 2014]
for i, rate in enumerate(deforestation_rates):
    year = deforestation_years[i]
    print(f"i = {i} - Yearly deforestation rate in {year} is:{rate}k hectares")


marine_species_count = {
    'Dolphins': 12,
    'Whales': 3,
    'Sea Turtles': 7
}

for species in marine_species_count:
    print(f"{species}: {marine_species_count[species]} sightings")