tree = {'tree_type':'Pepper-bark tree','age':15,
        'family':'Canellaceae'}
print(f"associated with age:{tree['age']}")

kingdom = {'kingdom': 'plantae'}

tree.update(kingdom)
print(tree)

del tree['family']
print(tree)

african_trees = {
    "Baobab": {
        "common_name": "Baobab",
        "scientific_name": "Adansonia",
    },
    "Acacia": {
        "common_name": "Acacia",
        "scientific_name": "Acacia",
    }
}
print(african_trees)

new_baobab = {'country':'Zimbabwe',
'average_height': 25}
african_trees['Baobab'].update(new_baobab)

new_acacia = {'country':'South Africa',
'average_height': 15}
african_trees['Acacia'].update(new_acacia)

print(african_trees)