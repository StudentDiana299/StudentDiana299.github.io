animals_tuple = ('Great White Shark', 'Blue Whale', 'African Elephant',  'Bald Eagle', 'Orangutan', 'Tiger', 'Tiger', 'Panda', 'Koala')
animals_set= set(animals_tuple)
animal_string = "Great White Shark"
print("Tuple:")
for animal in animals_tuple:
    print(animal)
print("Set:")
for animal in animals_set:
    print(animal)
print("String:")
for letter in animal_string:
    print(letter)

my_name = ('Daina')
for letter in my_name:
    if letter =='i':
        continue
    print(letter)

