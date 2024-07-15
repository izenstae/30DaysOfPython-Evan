
# Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
'''
str = ['Thirty', 'Days', 'Of', 'Python']
full_str = ' '.join(str)
print(full_str)
'''
# Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
'''
str = ['Coding', 'For', 'All']
full_str = ' '.join(str)
print(full_str)
'''
# Declare a variable named company and assign it to an initial value "Coding For All".
company = 'Coding For All'
# Print the variable company using print().
print(company)
# Print the length of the company string using len() method and print().
print(len(company))
# Change all the characters to uppercase letters using upper() method.
print(company.upper())
# Change all the characters to lowercase letters using lower() method.
print(company.lower())
# Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
print(company.capitalize())
print(company.title())
print(company.swapcase())
# Cut(slice) out the first word of Coding For All string.
print(company[:6])
# Check if Coding For All string contains a word Coding using the method index, find or other methods.
print(company.index('Coding'))
print(company.find('Coding'))
print(company.count('Coding'))
# Replace the word coding in the string 'Coding For All' to Python.
print(company.replace('Coding', 'Python'))
# Change Python for Everyone to Python for All using the replace method or other methods.
phrase = 'Python for Everyone'
print(phrase.replace('Everyone', 'All'))
# Split the string 'Coding For All' using space as the separator (split()) .
print(company.split())
# "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
tech_companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(tech_companies.split(','))
# What is the character at index 0 in the string Coding For All.
# C
# What is the last index of the string Coding For All.
# 13
# What character is at index 10 in "Coding For All" string.
# ' ' (Space Character)
# Create an acronym or an abbreviation for the name 'Python For Everyone'.
print(phrase[0],phrase[7].upper() ,phrase[11])
# Create an acronym or an abbreviation for the name 'Coding For All'.
print(company[0], company[7], company[-3])
# Use index to determine the position of the first occurrence of C in Coding For All.
print(company.index('C'))
# Use index to determine the position of the first occurrence of F in Coding For All.
print(company.index('F'))
# Use rfind to determine the position of the last occurrence of l in Coding For All People.
print(company.rfind('l'))
# Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print('You cannot end a sentence with because because because is a conjunction'.index('because'))
# Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print('You cannot end a sentence with because because because is a conjunction'.rindex('because'))
# Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
because = 'You cannot end a sentence with because because because is a conjunction'
print(because[31:54])
# Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print(because.find('because'))
# Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print(because[31:54])
# Does ''Coding For All' start with a substring Coding?
# Yes
# Does 'Coding For All' end with a substring coding?
# No
# '   Coding For All      '  , remove the left and right trailing spaces in the given string.
print('   Coding For All      '.strip('  '))
# Which one of the following variables return True when we use the method isidentifier():
# 30DaysOfPython False
# thirty_days_of_python True

# The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
joined_libraries = '- '.join(libraries)
print(joined_libraries)
# Use the new line escape sequence to separate the following sentences.
# I am enjoying this challenge.
# I just wonder what is next.
print('I am enjoying this challenge.\nI just wonder what is next.')
# Use a tab escape sequence to write the following lines.
# Name      Age     Country   City
# Asabeneh  250     Finland   Helsinki
print('Name\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki')
# Use the string formatting method to display the following:
# radius = 10
# area = 3.14 * radius ** 2
# The area of a circle with radius 10 is 314 meters square.
radius = 10
area = 3.14 * radius ** 2
print('The area of a circle with radius {} is {} meters square'.format(radius, area))
# Make the following using string formatting methods:
'''
8 + 6 = 14
8 - 6 = 2
8 * 6 = 48
8 / 6 = 1.33
8 % 6 = 2
8 // 6 = 1
8 ** 6 = 262144
'''
a = 8
b = 6
print('{} + {} = {}'.format(a, b, a + b))
print('{} - {} = {}'.format(a, b, a - b))
print('{} * {} = {}'.format(a, b, a * b))
print('{} / {} = {:.2f}'.format(a, b, a / b))
print('{} % {} = {}'.format(a, b, a % b))
print('{} // {} = {}'.format(a, b, a // b))
print('{} ** {} = {}'.format(a, b, a ** b))