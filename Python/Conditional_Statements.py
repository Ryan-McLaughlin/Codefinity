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
if has_super_mushroom:  # if True:
    print(f'{mario} turning into a Super {mario} and overcome the obstacle.')
# check if Mario doesn`t have a super mushroom
if not has_super_mushroom:  # if not True:
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
if 6 <= month < 9:
    print('It is summer.')
# Creating the third if statement
if 9 <= month < 12:
    print('It is autumn.')
#Creating the fourth if statement
if month == 1 or month == 2 or month == 12:
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

x = 5
y = 7
z = 14
# Creating if part
if (x + y > z) and (x + z > y) and (y + z > x):
    print('These three sides satisfy the condition of the triangle.')
# Creating else part
else:
    print('These three sides do not satisfy the condition of the triangle.')

print()
print('##############################################################################')
print('# if 06 - if else syntax')
print('##############################################################################')
print()

number_1 = -5
number_2 = 18
number_3 = 9
# Creating if part
if number_1 >= number_2:
    max_number = number_1
# Creating else part
else:
    max_number = number_2
# Creating another if statement
if number_3 > max_number:
    max_number = number_3
print(f'Maximum number of three numbers: {number_1}, {number_2}, {number_3} is {max_number}.')

print()
print('##############################################################################')
print('# if 07')
print('##############################################################################')
print()

angles = 6
# Creating condition for circle and elipse, if part
if angles == 0:
    print('Circle or elipse.')
# Creating condition for triangle, if part
if angles == 3:
    print('Triangle.')
# Creating condition for square, if part
if angles == 4:
    print('Square, rectangle or rhombus.')
#Creating condition for polygon, if part
if angles > 4:
    print('Polygon.')
# Creating else part
else:
    print('It is not a geometric figure.')

print()
print('##############################################################################')
print('# if 08')
print('##############################################################################')
print()

player_01 = 'scissors'
player_02 = 'rock'


def game(player_1, player_2):
    # Determine the winner
    if player_1 == player_2:
        return "It's a tie!"
    if (player_1 == 'rock' and player_2 == 'scissors') or (player_1 == 'scissors' and player_2 == 'paper') or (
            player_1 == 'paper' and player_2 == 'rock'):
        print("Player 1 wins!")
    else:
        return "Player 2 wins!"


print(game(player_01, player_02))

print()
print('##############################################################################')
print('# if elif else')
print('##############################################################################')
print()

angles = 6
# Creating condition for circle and elipse, if part
if angles == 0:
    print('Circle or elipse.')
# Creating condition for triangle, elif part
if angles == 3:
    print('Triangle.')
# Creating condition for square, elif part
if angles == 4:
    print('Square, rectangle or rhombus.')
# Creating condition for polygon elif part
elif angles > 4:
    print('Polygon.')
# Creating else part
else:
    print('It is not geometric figure.')

print()
print('##############################################################################')
print('# if elif else - challenge')
print('##############################################################################')
print()

cars = ['mazda', 'lexus', 'bmw', 'tesla', 'kia']
new_list = []
# Creating for loop
for car in cars:
    # Creating if part to check if car == 'bmw'
    if car == 'bmw':
        # Adding element to the list
        new_list.append(car.upper())
    # Creating elif part to check elif car == 'kia'
    elif car == 'kia':
        # Adding element to the list
        new_list.append(car.upper())
   # Creating else part
    else:
        # Adding elements to the list
        new_list.append(car.title())
print(cars)
print(new_list)

print()
print('##############################################################################')
print('# if elif else - challenge')
print('##############################################################################')
print()

list_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Creating for loop
for i in list_of_numbers:
    # Creating if part
    if i == 1:
        print(f'number{i} - {i}st')
    # Creating the first elif part
    elif i == 2:
        print(f'number{i} - {i}nd')
    # Creating the second elif part
    elif i == 3:
        print(f'number{i} - {i}rd')
    # Creating else part
    else:
        print(f'number{i} - {i}th')

print()
print('##############################################################################')
print('# if elif else - challenge')
print('##############################################################################')
print()

def music_for_you(mood_rank: int):
	moods = {1: "Exhausted", 2: "Sad", 3: "Relaxed", 4: "Happy", 5: "Excited"}

	if mood_rank == 1:
		print("The Beatles - Let It Be")
	elif mood_rank == 2:
		print("Avriel & The Sequoias - Quarter Past Four")
	elif mood_rank == 3:
		print("The Cinematic Orchestra, Patrick Watson - To Build A Home")
	elif mood_rank == 4:
		print("Sia - Santa's Coming For Us")
	elif mood_rank == 5:
		print("Mark Ronson & Bruno Mars - Uptown Funk")
	else:
		print("Rick Astley - Never Gona Give You Up")

music_for_you(6)