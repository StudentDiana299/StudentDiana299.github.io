tree_list = ['Tamboti', 'Baobab', 'Umbrella thorn', 'Yellowwood', 'Fever Tree', 'Moringa',
             'Marula', 'Waterpear','Baobab', 'Fountain Tree', 'Papaya Tree', 'Indian Laurel', 'Moringa']
print(tree_list)
tree_list_length = len(tree_list)
print(tree_list_length)

tree_set = set(tree_list)
type(tree_set)
print(tree_set)
tree_set_length = len(tree_set)
print(tree_set_length)

day_1_trees = {'Baobab', 'Buffalo Thorn', 'Bushwillow', 
               'Jackalberry', 'Knob Thorn', 'Lala Palm',
                 'Marula Tree', 'Umbrella Thorn', 
                 'Weeping Boer Bean', 'Sausage Tree'}
day_2_trees = {'Mopane Tree', 'Bushwillow', 'Knob Thorn', 'Jackalberry', 
               'Nara Plant', 'Wild Date Palm', 'Natal Mahogany', 
               'Tamboti','Leadwood', 'Bushwillow'}

union_result = day_1_trees.union(day_2_trees)
print(union_result)

both_days = day_1_trees.intersection(day_2_trees)
print(both_days)

uniqueness = day_2_trees.difference(day_1_trees)
print(uniqueness)

justchecking = both_days.issubset(day_1_trees)
print(justchecking)

hardwood_trees = {'Yellowwood', 'Leadwood', 
                  'Blackwood'}
confirming = hardwood_trees.issubset(day_2_trees)
print(confirming)