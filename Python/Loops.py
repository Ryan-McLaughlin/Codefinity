print()
print('##############################################################################')
print('# Python Loops Tutorial')
print('##############################################################################')
print()
print('##############################################################################')
print('# for')
print('##############################################################################')
print()

numbers = [2, 12, 4, 15, 6, 7, 8, 11]
counter = 0

# Set for loop for given list
for i in numbers:
    # Sum elements using counter
    counter += i

# Print the counter
print(counter)

print()
print('##############################################################################')
print('# for loop 01')
print('##############################################################################')
print()

numbers = [2, 17, 20, 5, 56, 7, 8, 11]

# Set for loop to work with numbers
for i in numbers:
    # Set condition *an element is lower than 10*
    if i < 10:
        # Set message 'is lower than 10'
        print(i, 'is lower than 10')
    else:
        # Set message 'is greater or equal to 10'
        print(i, 'is greater or equal to 10')

print()
print('##############################################################################')
print('# for loop 02')
print('##############################################################################')
print()

numbers = [12, 1, 6, 5, 3, 2, 8, 11]
counter = 1

# Set for loop to work with numbers
for i in numbers:
    # Set condition and break the loop if the counter is going to be greater than 100
    if counter * i > 100:
        break
    # Multiply the counter variable by the next element
    else:
        counter *= i

# Print the counter
print(counter)

print()
print('##############################################################################')
print('# for loop 03 - pass')
print('##############################################################################')
print()

numbers = [17, 7, 8, 11, 8, 5]

# Set for loop to work with numbers
for i in numbers:
    if i > 5:
        print(i, 'is greater than 5')
    else:
        # Fill the gap
        pass

#else:
# Filling the else block
print('Done')

print()
print('##############################################################################')
print('# for loop 04 - continue')
print('##############################################################################')
print()

numbers = [2, 3, 8, 5, 6, 7, 8, 11, 8]
counter = 0

# Set for loop with enumerate() to work with numbers
for i, v in enumerate(numbers):
    # Set condition *a number need to be multiple of three*
    if v % 3 == 0:
        # Print message
        print('Numbers[', i, '] =', v, 'is multiple of three')
        # Increase the counter
        counter += 1
    else:
        continue

# Print the counter
print(counter)

print()
print('##############################################################################')
print('# for loop 05 - challenge')
print('##############################################################################')
print()

products_list = [29.25, 48.99, 99.98, 124.65, 214.30, 543.90, 799.85]
upd_list = []

# Set for loop to work with products_list
for i in products_list:
    # Set the condition *if the price is greater than 30*
    if i > 30:
        # Add the element in an updated list with the 25% discount
        upd_list.append(round(i * 0.75, 2))
    else:
        # Add the element in an updated list without the discount
        upd_list.append(i)

# Print the upd_list
print(upd_list)

print()
print('##############################################################################')
print('# while loop')
print('##############################################################################')
print()

i = 10

# Set while loop
while i > -1:
    # Print i
    print(i)
    # Decrease i
    i -= 1

print()
print('##############################################################################')
print('# while loop')
print('##############################################################################')
print()

numbers = [1, -12, 4, -6, -10, 5, -1, -5, 4]
i = 0
counter = 1

# Set while to work with numbers
while i < len(numbers):
    # Set condition
    if numbers[i] < 1:
        # Multiply elements
        counter *= numbers[i]
    # Increase i
    i += 1

# Print counter
print(counter)

print()
print('##############################################################################')
print('# while loop...')
print('##############################################################################')
print()

numbers = [2, 3, 4, -11, 5]
i = -1

# Set while loop to work with numbers
while i < len(numbers) - 1:
    # Increase 'i'
    i += 1
    if numbers[i] < 0:
        # Print a negative element
        print('Negative number was found!: ', numbers[i])
        # Finish the loop
        break
    else:
        # Continue searching
        continue

print()
print('##############################################################################')
print('# another shitty while loop...')
print('##############################################################################')
print()

counter = 0

# Fill the gap
while counter < 10:
    counter += 1
    # Fill the gap
    pass

# Fill the gap
else:
    print('Done!')

print()
print('##############################################################################')
print('# nested for loop')
print('##############################################################################')
print()

# Set outer loop for the number of rows
for i in range(4, 0, -1):
    # Set inner loop for the number of elements in the row
    for j in range(1, i + 1):
        # Print '*'
        print('*', end=' ')
    print('')

print()
print('##############################################################################')
print('# nested for loop')
print('##############################################################################')
print()

matrix = [
    [1, 2, 4, 29],
    [3, 4, 6, 1]
]

# Summing all elements in the list
# Set counter
counter = 0
# Set outer loop to work with the number of rows
for i in range(len(matrix)):
    # Inner loop to work with the number of element in the row
    for j in range(len(matrix[i])):
        # Implement sum with the help of counter
        counter += matrix[i][j]

# Print counter
print(counter)

print()
print('##############################################################################')
print('# nested while loop')
print('##############################################################################')
print()

matrix = [
    [1, 2, 4, 29],
    [3, 4, 6, 1],
    [10, -5, 0]
]

# Set outer while loop to work with the number of rows
i = 0
while i < len(matrix):
    # Set inner while loop to work with the number of elements in the row
    j = 0
    while j < len(matrix[i]):  # Change an element
        matrix[i][j] += 1
        # Print an element
        print(matrix[i][j], end=' ')
        j += 1
    i += 1
    print('')

print()
print('##############################################################################')
print('# nested loop')
print('##############################################################################')
print()

matrix = [
    ['R', 'i', 'd', 'e', 'r', 's', ' ', 'o', 'n '],
    ['t', 'h', 'e', ' ', 's', 't', 'o', 'r', 'm']
]

# Set for loop to work with rows (i)
for i in range(len(matrix)):
    # Set j
    j = 0
    # Set while loop to work with elements inside the row
    while j < len(matrix[i]):
        # Print an element
        print(matrix[i][j], end=' ')
        # Update j
        j += 1
    print('')

print()
print('##############################################################################')
print('# nested loop')
print('##############################################################################')
print()

text = 'ofsddsfadfjfojnanjinjudfninvjunjee'
vowels = 'aeiou'

# Set i
i = 0
# Set while loop to work with elements of the text
while i < len(text):
    # Set for loop to work with the elements of the vowels
    for j in range(len(vowels)):
        # If an element in the text is one of the elements in vowels
        if text[i] == vowels[j]:
            # Print an element
            print(text[i])
    i += 1

print()
print('##############################################################################')
print('# nested loop w/ elif')
print('##############################################################################')
print()

matrix = [
    [' L', '#', 'o', 'o', '#', 's', 'i', 'n', 'g', ' ', '#', 'm', 'y '],
    ['r', 'e', '#', 'l', 'i', '#', 'g', 'i', 'o', '#', 'n', '!', 'apspsasd']
]

# Set for loop to work with the number of rows
for i in range(len(matrix)):
    # Set for loop to work with the number of elements of the row
    for j in range(len(matrix[i])):
        # Set condition if an element is '#'
        if matrix[i][j] == '#':
            continue
        # Set condition if an element is '!'
        elif matrix[i][j] == '!':
            break
        else:
            # Print an element
            print(matrix[i][j], end=' ')

print()
print('##############################################################################')
print('# nested loop w/ elif')
print('##############################################################################')
print()

text = 'aew$^&hg32yy8wer3$#^*@#7ds983hn'
vowels = 'aeiou'

text_vowels = ''
text_consonants = ''
text_symbols = ''

# Set i
i = 0
# Set outer while loop to work with text
while i < len(text):
    # Set u
    u = 0
    # Set condition *if an element is a letter*
    if text[i].isalpha():
        # Set inner *while* loop to work with vowels
        while u < len(vowels):
            # Set condition *if a letter from the text is in the vowels*
            if text[i] == vowels[u]:
                # Add the letter to the text_vowels
                text_vowels += text[i]
                break
            # Increase u
            u += 1
        else:
            # Add the letter to the text_consonants
            text_consonants += text[i]
    else:
        # Add the letter to the text_symbols
        text_symbols += text[i]
    i += 1

print('Vowels from the text: ', text_vowels)
print('Consonants from the text: ', text_consonants)
print('Symbols from the text: ', text_symbols)

