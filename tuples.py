# Assign each element in animal_tuple to individual variables
import sys
animal_tuple = ("Yellow anaconda", "Reptile", 30.5, 20)

name, group, av_weight, av_lifespan = animal_tuple
print(f"Name: {name}")
print(f"Group: {group}")

tree_tuple = 8, 'apple', 'Granny Smith'
type(tree_tuple)
print(tree_tuple)
tree_tuple_length = len(tree_tuple)
print(tree_tuple_length)

fruit = tree_tuple[1]
print(fruit)

text_only = tree_tuple[1:3]
print(text_only)

fruit_summer = 'peach', 'apricot', 'plum'
fruit_winter = 'lemon', 'orange', 'grapefruit'
print (fruit_summer + fruit_winter)
all_fruit = fruit_winter + fruit_summer
print(all_fruit)

combined_info = ('yellow', 5, 'lemon')
colour, age, tree_type = combined_info

print(f"Tree's color:{colour}")

peach_count = all_fruit.count('peach')
print(peach_count)