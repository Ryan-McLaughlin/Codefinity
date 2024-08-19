print()
print('##############################################################################')
print('# functions - using f"string: {string}"')
print('##############################################################################')
print()


def greet_dog(dog_name, dog_breed):
    return f"Hello, {dog_name}! You're a {dog_breed}."


# Function call
greeting = greet_dog("Buddy", "Labrador")

# Display the result
print(greeting)

print()
print('##############################################################################')
print('# functions - positional arguments vs dictionary')
print('##############################################################################')
print()

user_list = []


def register_user(name, email):
    # Dictionary with user data
    user_data = {'name': name, 'email': email}
    # Add the dictionary to the user list
    user_list.append(user_data)


# First function call
register_user("Alice", "alice@example.com")
# Second function call
register_user(email="bob@example.com", name="Bob")

# Check the result
print(user_list)

print()
print('##############################################################################')
print('# functions - optional argument')
print('##############################################################################')
print()


# Function that generates a greeting
def greet(name, greeting="Hello"):
    message = f"{greeting}, {name}!"
    return message


# Function calls
print(greet("Slim"))  # Uses default values for greeting
print(greet("Bob", "Hi"))  # All arguments are provided

print()
print('##############################################################################')
print('# functions - arbitrary argument')
print('##############################################################################')
print()


# Function to calculate the average of numbers
def calculate_average(*args):
    # Determine the number of arguments
    len_args = len(args)
    # Check if the number of arguments is zero
    if len_args == 0:
        # If there are no arguments, return 0
        return 0
    # Calculate the sum of all arguments
    total = sum(args)
    # Calculate the average value
    average = total / len_args
    # Return the average value
    return average


# Test the function using different number of arguments
print(calculate_average(10, 20, 30, 40, 50))
print(calculate_average(5))
print(calculate_average())

print()
print('##############################################################################')
print('# functions - arbitrary keyword argument')
print('##############################################################################')
print()


# Function to calculate the total cost of candies and sweets
def calculate_total_cost(**kwargs):
    total_cost = 0
    # Iterate through the keyword arguments and calculate the total cost
    for item, cost in kwargs.items():
        total_cost += cost

    return total_cost


# Test the function using different number of arguments
total = calculate_total_cost(candy=2.5, chocolate=3.0, lollipop=1.5, gummy_bears=4.0)
print(f"The total cost of candies and sweets is: ${total}")

total = calculate_total_cost(candy=1.0, cookie=2.5, marshmallow=3.5)
print(f"The total cost of candies and sweets is: ${total}")

print()
print('##############################################################################')
print('# functions - .join on args')
print('##############################################################################')
print()


# Define a function with arbitrary arguments
def merge_string_lists(*args):
    merged_string = ''

    # Iterate all strings in args
    for string_list in args:
        merged_string += ' '.join(string_list) + ' '

    # Return resulting string
    return merged_string


# Example usage
list1 = ['Hello,', 'world!']
list2 = ['I', 'am', 'Python!']
list3 = ['Nice', 'to', 'meet', 'you!']
result = merge_string_lists(list1, list2, list3)
print(result)

print()
print('##############################################################################')
print('# functions - multiple return values')
print('##############################################################################')
print()


def calculate_statistics(numbers):
    if len(numbers) == 0:
        return 0, 0, 0, 0
    total = sum(numbers)
    average = total / len(numbers)
    minimum = min(numbers)
    maximum = max(numbers)
    return total, average, minimum, maximum


# Example usage
data = [12, 7, 15, 9, 22, 13, 18]
total, average, minimum, maximum = calculate_statistics(data)

print(f'Total Sum: {total}')
print(f'Average: {average}')
print(f'Minimum Value: {minimum}')
print(f'Maximum Value: {maximum}')

print()
print('##############################################################################')
print('# functions - yield more efficient than return')
print('##############################################################################')
print()


def id_generator():
    count = 1
    while True:
        yield f"ID_{count}"
        count += 1


# Using the generator to obtain unique identifiers
id_gen = id_generator()

# Getting the first five identifiers
for i in range(5):
    unique_id = next(id_gen)
    print(unique_id)

print()
print('##############################################################################')
print('# functions - more yield')
print('##############################################################################')
print()


def traffic_light_generator():
    while True:
        yield "Red"
        yield "Yellow"
        yield "Green"


# Using the generator to simulate the operation of a traffic light
traffic_light = traffic_light_generator()

# Printing the state of the traffic light for several cycles
for i in range(9):
    print(next(traffic_light))

print()
print('##############################################################################')
print('# functions - recursion')
print('##############################################################################')
print()


def sum_of_digits(n):
    if n < 10:
        return n
    else:
        # use modulus to get last number, use integer division to get rest of digits
        return n % 10 + sum_of_digits(n // 10)


print(sum_of_digits(123456))

print()
print('##############################################################################')
print('# functions - recursion 01')
print('##############################################################################')
print()


def draw_pyramid(height, current_height=1):
    if current_height > height:
        return  # Base case: exit when the pyramid height is reached

    # Recursive case: print a row for the current height
    spaces = ' ' * (height - current_height)  # Spaces for alignment
    stars = '*' * (2 * current_height - 1)  # Asterisks for the current row
    print(spaces + stars)

    # Recursive call for the next row
    draw_pyramid(height, current_height + 1)


# Example usage
draw_pyramid(4)

print()
print('##############################################################################')
print('# lambda functions - anonymous (dont have name)')
print('##############################################################################')
print()

# Creating a lambda function that adds two numbers
add = lambda x, y: x + y

# Calling the lambda function
result = add(3, 5)
print(result)  # Outputs 8

print()
print('##############################################################################')
print('# immediately invoked lambda functions')
print('##############################################################################')
print()

celsius_temperature = 23

# Lambda function for converting temperature
# from celsius_temperature variable to fahrenheit temperature
fahrenheit_temperature = (lambda celsius: (9/5) * celsius + 32)(celsius_temperature)

# Output the result
print(f"{celsius_temperature} degrees Celsius is equal to {fahrenheit_temperature} degrees Fahrenheit")

