# Conditional Statements in Python
print()
print('##############################################################################')
print('# if')
print('##############################################################################')
print()

string = 'codefinity'
# Calculating the length of the string
len_of_string = len(string)
# Creating if statement
if len_of_string > 7:
    print('Codefinity is the best platform to start your career in IT.')

print()
print('##############################################################################')
print('# if 01 w/ f-string & ==')
print('##############################################################################')
print()

in_mind = 9
guess = 9
# Creating if statement
if in_mind == guess:
    # Displaying the result
    print(f'Right, You guessed my number! I have in my mind number {in_mind}')

print()
print('##############################################################################')
print('# if 02 / if not')
print('##############################################################################')
print()

mario = 'Mario'
has_super_mushroom = True
# check the condition with super mushroom
if has_super_mushroom: # if True:
	print(f'{mario} turning into a Super {mario} and overcome the obstacle.')
# check if Mario doesn`t have a super mushroom
if not has_super_mushroom: # if not True:
	print('Find a Super Mushroom to overcome this block.')

print()
print('##############################################################################')
print('# if 03')
print('##############################################################################')
print()

month = 5
# Creating the first if statement
if 3 <= month < 6:
    print('It is spring.')
# Creating the second if statement
if 6<=month<9:
    print('It is summer.')
# Creating the third if statement
if 9 <= month < 12:
    print('It is autumn.')
#Creating the fourth if statement
if  month == 1 or month == 2 or month == 12:
    print('It is winter.')

print()
print('##############################################################################')
print('# if 04 - operator precedence')
print('##############################################################################')
print()

def leap_year(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return 'Leap year'
    else:
        return 'Not a leap year'

print(leap_year(2024))
print(leap_year(2014))

print()
print('##############################################################################')
print('# if 05 - if else')
print('##############################################################################')
print()

