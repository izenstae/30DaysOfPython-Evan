'''
# Declare an Empty list
empty = []
# declare a list with more than 5 items
five_items = [1, 2, 3, 4, 5]
# find the length of the list ^
print(len(five_items))
# get the first item, middle item and the last item of the list
print(five_items[0],five_items[2], five_items[len(five_items)-1])
# Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ['Evan', 22, '8 Ft', 'Married', '123 forget-about-it BLVD']
# Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print(it_companies)
print((len(it_companies)))
print(it_companies[0],it_companies[3],it_companies[-1])
it_companies[4] = 'NVIDIA'
print(it_companies)
it_companies.append('TSMC')
it_companies.insert(3, 'Coinbase')
it_companies[0] = it_companies[0].upper()
print(it_companies)
print('#; '.join(it_companies))
print(it_companies.index('NVIDIA'))
it_companies.sort()
print(it_companies)
it_companies.reverse()
print(it_companies)
print(it_companies[:3])
print(it_companies[-3:])
print(it_companies[3:6])
print(it_companies.pop(0))
print(it_companies.pop(4))
print(it_companies.pop(-1))
print(it_companies.clear())
del it_companies



# join the following lists
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
full_list = front_end + back_end
full_stack = full_list.copy()
full_stack.insert(4,'Python')
full_stack.insert(5, 'SQL')
'''

# Exercises Level 2
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print('Min: ', min(ages), 'Max: ', max(ages))
ages.insert(0, min(ages))
ages.append(max(ages))
print(ages)
avg_age = sum(ages)/len(ages)
median_age = ages[int(len(ages)/2)]
range_of_ages = max(ages) - min(ages)
print(avg_age, median_age, range_of_ages)
print(abs(min(ages) - avg_age), abs(max(ages)- avg_age))