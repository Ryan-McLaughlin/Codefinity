print()
print('##############################################################################')
print('# Dictionary')
print('##############################################################################')
print()
# Data
countries_dict = {
    'USA': (9629091, 331002651),
    'Canada': (9984670, 37742154),
    'Germany': (357114, 83783942),
    'Brazil': (8515767, 212559417),
    'India': (3166391, 1380004385)
}


# Defining a function
def country_information(d, name):
    print('Country:', name)
    print('Area:', d[name][0], 'sq km')
    print('Population:', round(d[name][1] / 1000000, 2), 'MM')


# Testing the function
country_information(countries_dict, 'Brazil')
print()
country_information(countries_dict, 'Germany')
print()


def country_information_mod(d, name):
    if name not in d.keys():
        print("There is no information about", name)
    else:
        print("Country:", name)
        print("Area:", d[name][0], 'sq km')
        print("Population:", round(d[name][1] / 1000000, 2), 'mln')
        print()


# Testing the function
country_information_mod(countries_dict, "USA")
country_information_mod(countries_dict, "Ukraine")

print()
print('##############################################################################')
print('# Lambda function - typically used for short, simple operations')
print('##############################################################################')
print()
sq = lambda x, y: (x + y) ** 2
# Test it
print('Sum of 2 and 3 squared is', sq(2, 3))

print()
print('##############################################################################')
print('# List for loop - temp')
print('##############################################################################')
print()
fahrenheit_temps = [32, 50, 68, 86, 104]
celsius_temps = [(temp - 32) * 5 / 9 for temp in fahrenheit_temps]
for i in range(len(fahrenheit_temps)):
    print("F: " + str(fahrenheit_temps[i]) + " C: " + str(celsius_temps[i]))

print()
print('##############################################################################')
print('# Dictionary for loop')
print('##############################################################################')
print()
city_popul = {
    'New York': 8419600,
    'Los Angeles': 3980400,
    'Chicago': 2716000,
    'Houston': 2328000,
    'Phoenix': 1690000,
    'Smalltown': 15000
}

min_popul = 5000000

filtered_cities = {
    city: population for city, population in city_popul.items() if population >= min_popul
}

print(filtered_cities)

print()
print('##############################################################################')
print('# Tuple - immutable')
print('##############################################################################')
print()
string_tuple = ('apple', 'apricot', 'banana', 'grape', 'mango', 'peach', 'pineapple')
print(string_tuple)

letters = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h')
new_tuple = (letters[0], letters[1], letters[-4], letters[-2])
print(new_tuple)

print(3.28084 * 5)

print()
print('##############################################################################')
print('# Unix Timestamp')
print('##############################################################################')
print()

import time

unix_timestamp = time.time()
print('Unix Timestamp:\n ' + str(unix_timestamp))

import datetime

now = datetime.datetime.now()

# Example format: Year-Month-Day Hour:Minute:Second
formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
print("Formatted date and time:\n", formatted_date)

print()
print('##############################################################################')
print('# Tuple modification 01')
print('##############################################################################')
print()

fruits = ('apple', 'apricot', 'banana', 'grape', 'mango', 'peach', 'pineapple')
print(fruits)
# Turn the tuple into a list
list_fruits = list(fruits)
# Delete items
list_fruits.remove('banana')
list_fruits.remove('grape')
list_fruits.remove('peach')
# Return the list to the tuple
fruits = tuple(list_fruits)
# Print the result
print(fruits)

print()
print('##############################################################################')
print('# Tuple modification 02')
print('##############################################################################')
print()

# Create a tuple
fruits = ("apple", "banana", "cherry", "orange", "kiwi")
print (fruits)
# Turn the tuple into a list
list_fruits = list(fruits)
# Change the items
list_fruits[1] = "melon"
list_fruits[2] = "mango"
# Return the list to the tuple
fruits = tuple(list_fruits)

# Print the result
print(fruits)

print()
print('##############################################################################')
print('# Tuple modification 03')
print('##############################################################################')
print()

# Create a tuple
fruits = ("apple", "banana", "cherry")
print(fruits)
# Turn the tuple into a list
list_fruits = list(fruits)
# Add elements
list_fruits.append("orange")
list_fruits.append("kiwi")
# Return the list to the tuple
fruits = tuple(list_fruits)

# Print the result
print(fruits)

print()
print('##############################################################################')
print('# Tuple modification 04')
print('##############################################################################')
print()

# Create tuples
fruits = ("apple", "banana", "cherry")
print(fruits)
another_tuple = ("orange", "kiwi")
# Concatenate tuples
fruits += another_tuple
# Print the result
print(fruits)

print()
print('##############################################################################')
print('# Set 00 - mutable w/ unique elements, order of elements not guaranteed')
print('##############################################################################')
print()

# Creating a set which contains strings
set_1 = {'pineapple', 'pear', 'cherry'}
print(set_1)

# Creating a set which contains a mixed type of values
set_2 = {'pear', 45, None, 'car', 'Joe', 12, 5}
print(set_2)

print()
print('##############################################################################')
print('# Set 01 - set_01.add()')
print('##############################################################################')
print()

# Creating a set
set_1 = {2, 4, 6, 8, 10, 12, 14, 16, 18, 20}
print(set_1)

# Adding elements
set_1.add(22)
set_1.add(24)
set_1.add(26)
set_1.add(28)
print(set_1)

print()
print('##############################################################################')
print('# Set 02 - set_02.update()')
print('##############################################################################')
print()

# Creating a set
set_1 = {1, 5, 10, 15}
print(set_1)
# Updating a set
set_1.update([20, 25, 100])
# Printing the result
print(set_1)

print()
print('##############################################################################')
print('# Set 03 - verify elements of set')
print('##############################################################################')
print()

set_1 = {"apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"}

print("pear" in set_1)
print("banana" in set_1)
print("lemon" in set_1)

print()
print('##############################################################################')
print('# Set 04 - set_04.remove()\n'
      '           set_04.discard()')
print('##############################################################################')
print()

set_1 = {1,  2, 3, 8, 13}
print(set_1)
set_1.remove(1) # throws error if element is not in set
set_1.discard(3) # does not throw error if element is not in set (leaves set as is)
print(set_1)

print()
print('##############################################################################')
print('# Set 05 - set_05.clear()')
print('##############################################################################')
print()

set_1 = {
    'India',
    'Latvia',
    'Panama',
    'Serbia',
    'Finland',
    'Germany',
    'Japan',
    'United States of America'
}
for country in set_1:
    print(country)

set_1.clear()
print("\n" + str(set_1))
