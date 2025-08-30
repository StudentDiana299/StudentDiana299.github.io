first_trees = [1,2,3,4,5]
print(first_trees)

tree_list = list(range(20,144,4))
print(f"wihout 400: {tree_list}")

tree_list.append(400)
print(f"with 400: {tree_list}")

old_trees = [500, 600, 700]
combined_trees = tree_list + old_trees
print(combined_trees)
combined_trees_count = len(combined_trees)
print(combined_trees_count)


conifers = ["Pine", "Fir", "Juniper"]
cycads = ["Cycas", "Sago palm", "Zamia"]
gymnosperms = conifers + cycads
print(gymnosperms)

new_lists = gymnosperms[3:5]
print(new_lists)

ordered_plants = conifers + cycads
ordered_plants.sort()
print(ordered_plants)