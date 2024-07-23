# create an empty tuple
empty_tpl = ()
# Create a tuple containing names of your siblings 
sisters = ('Dana', 'Margot', 'Lisa')
brothers = ('Derek', 'Ross', 'Chad')
siblings = brothers + sisters
print(len(siblings))
parents = ('Mom', 'Dad')
family_members = parents + siblings
siblings_upacked = family_members[2:]
parents_upacked = family_members[:2]
print(siblings_upacked, parents_upacked)

fruits = ('Apples', 'Banana', 'Blueberries','Blackberries')
veggies = ('Broccoli','Cauliflower', 'Peppers')
animal_products = ('Milk', 'Eggs', 'Meats')
food_stuff_tp = fruits + veggies + animal_products
food_stuff_lt = list(food_stuff_tp)
food_stuff_lt[:3]
food_stuff_lt[-3:]
del food_stuff_lt

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)