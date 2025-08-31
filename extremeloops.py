endangered_marine_species = ['Hawksbill Turtle', 'Vaquita', 'Blue Whale', 'Staghorn Coral', 'Green Turtle']
endangered_count = 0

# Your task: Use a for loop to count the number of species in the list
for species in endangered_marine_species:
    endangered_count += 1

print(f"Number of endangered marine species: {endangered_count}")

initial_forested_area = 1000  # in square kilometres
deforestation_rate = 20       # square kilometres per year

# Your task: Use a while loop to determine how many years it takes for the forested area to fall below 500 square kilometres
years = 0
while initial_forested_area > 500:
   initial_forested_area -= deforestation_rate
   years += 1

print(f"Years until critical deforestation level: {years}")

animals = ['Tiger', 'Blue Whale', 'African Elephant', 'Koala', 'Panda']
endangered_animals = ['Tiger', 'Blue Whale', 'African Elephant']

# Your task: Use a for loop to print out each animal's name and its endangered status
for animal in animals:
    if animal in endangered_animals:
        print(f"{animal} is endangered")
    else:
        print(f"{animal} not endangered")

ocean_pollution_data = {
    'Pacific Ocean': [3, 5, 2],  # pollution levels
    'Atlantic Ocean': [7, 2, 4],
    'Indian Ocean': [5, 1, 3]
}



# Your task: Use loops to calculate the average pollution level for each ocean and print it
for ocean, pollution_levels in ocean_pollution_data.items():
    sum_pollution_level = 0
    for levels in pollution_levels:
        sum_pollution_level += levels
        print (f"sum_pollution_level is {sum_pollution_level} for {ocean}")
    avg_pollution_level = sum_pollution_level/len(pollution_levels)
    print(f"avg_pollution_level is {avg_pollution_level} for {ocean}")


current_population = 150  # of a particular endangered species
target_population = 500
years = 0
growth_rate = 1.07  # 7% annual growth due to conservation efforts

# Your task: Use a while loop to calculate how many years it takes to reach the target population
while current_population < target_population:
    current_population *= growth_rate
    years += 1
print(f"Years to reach target population: {years}")


numbers = range(1, 11)

squares = {x:x**2 for x in numbers}# Fill in the list comprehension
print(list(squares.values()))


numberss = range(1, 21)
even_numbers = [x for x in numberss if x % 2 == 0 ] # Fill in the list comprehension
print(even_numbers)


marine_animals = ['Dolphin', 'Shark', 'Turtle']
# Desired Output: {'Dolphin': 'Aquatic', 'Shark': 'Aquatic', 'Turtle': 'Aquatic'}

animal_categories = {animali: 'Aquatic' for animali in marine_animals }
print(animal_categories)


species = ['Dolphins', 'Whales', 'Sea Turtles', 'Seals']
status = ['Endangered', 'Vulnerable', 'Endangered', 'Least Concern']
# Desired Output: {'Dolphins': 'Endangered', 'Sea Turtles': 'Endangered'}
number_of_species = range(len(species))

endangered_species = {species[i]: status[i] for i in number_of_species if status[i] == 'Endangered'} 