# The function will take a list of 25 strings. The function will output a large string emulating a grid. The function
# will check if the list has 25 strings. If it doesn't, the function will return "Invalid input".
def print_grid(list):
    if len(list) != 25:
        return "Invalid input"
    else:
        print('+', '-', '-', '-', '-', '-', '++', '-', '-', '-', '-', '-', '+')
        print('|', list[0], '|', list[1], '|', list[2], '|', list[3], '|', list[4], '|')
        print('+', '-', '-', '-', '-', '-', '++', '-', '-', '-', '-', '-', '+')
        print('|', list[5], '|', list[6], '|', list[7], '|', list[8], '|', list[9], '|')
        print('+', '-', '-', '-', '-', '-', '++', '-', '-', '-', '-', '-', '+')
        print('|', list[10], '|', list[11], '|', list[12], '|', list[13], '|', list[14], '|')
        print('+', '-', '-', '-', '-', '-', '++', '-', '-', '-', '-', '-', '+')
        print('|', list[15], '|', list[16], '|', list[17], '|', list[18], '|', list[19], '|')
        print('+', '-', '-', '-', '-', '-', '++', '-', '-', '-', '-', '-', '+')
        print('|', list[20], '|', list[21], '|', list[22], '|', list[23], '|', list[24], '|')
        print('+', '-', '-', '-', '-', '-', '++', '-', '-', '-', '-', '-', '+')





# The function will take number_counter (a list with only two values, the values being integers) and x (a string with
# either "GG" or "XX" written). The function will update number counter and will return a new string based on that.
# More specifically, the function will return a string that says "Numbers already selected: " with the first value of
# number_counter, and "Numbers needed:" with the second value of number_counter. The function will update the first value of
# number_counter depending on what x is. If x is "GG", the function will increase the first value of number_counter by 1.
# If x is "XX", the function will not change the first value of number_counter. The function won't update the second value
# of number_counter.
number_counter = [0, 3]
def number_changer(number_counter, x):
    if x == "GG":
        number_counter[0] += 1
        return print("Numbers already selected: " + str(number_counter[0]) ,  "Numbers needed: " + str(number_counter[1]))
    elif x == "XX":
        return print("Numbers already selected: " + str(number_counter[0]) , "Numbers needed: " + str(number_counter[1]))
    else:
        return print("Numbers already selected: " + str(number_counter[0]) , "Numbers needed: " + str(number_counter[1]))




#The function will take heart_counter (a list with only one value, the value being an integer) and x
#(a string with either "GG" or "XX" written). The function will return a string and will update heart_counter.
#More specifically, the function will return a string that says "lives: " with hearts written. The number of hearts
#written will depend on the value of heart_counter (valid from 1 to 7). The function will also update the number for
#heart_counter. Now, the purpose of the function is
#to see if x is "XX" or "GG". Depending on what x is, the function will reduce the number of hearts displayed and the
#value on list heart_counter or the function won't do anything.
def heart_counter_display(heart_counter, x):
    dict = {1: "♥", 2: "♥ ♥", 3: "♥ ♥ ♥", 4: "♥ ♥ ♥ ♥", 5: "❤ x 5", 6: "❤ x 6", 7: "❤ x 7", 8: "❤ x 8", 9: "❤ x 9", 10: "❤ x 10"
            , 11: "❤ x 11", 12: "❤ x 12", 13: "❤ x 13", 14: "❤ x 14", 15: "❤ x 15", 16: "❤ x 16", 17: "❤ x 17", 18: "❤ x 18", 19: "❤ x 19"}
    string = ''
    if x == "GG":
        string = "lives: " + dict[heart_counter[0]]
    elif x == "XX":
        heart_counter[0] -= 1
        if heart_counter[0] == 0:
            return "No lives left"
        else:
            string = "lives: " + dict[heart_counter[0]]
    else:
        string = "lives: " + dict[heart_counter[0]]
    return string

# This function will list the instructions for the game. You will press enter to get each subsequent instruction.
def instructions():
    input("Press enter to continue for each subsequent instruction until you start the game!:")
    print("You have 3 lives.")
    input()
    print("You need to select 3 numbers between 1 to 25 from a grid.")
    input()
    print("The computer will have a hidden grid with 3 numbers selected from 1 to 25.")
    input()
    print("Those selected numbers will contain XX instead of the number in the grid.")
    input()
    print("You will have to select numbers that don't contain XX.")
    input()
    print("However, you won't know which numbers have XX, so you will have to guess.")
    input()
    print("If you end up choosing a number with XX, you lose a life")
    input()
    print("If you lose all your lives, you lose the game")
    input()
    print("However, if you don't lose all your lives and manage to select all numbers without XX, you win the level.")
    input()
    print("Each subsequent level will have more XX and more numbers to select.")
    input()
    print("Good luck!")

# This function takes a list of strings and an integer called number_of_XX as parameters. The function outputs a
# list with the same values as the parameter but with a number of XX values determined by number_of_xx placed randomly
# in the list
def XX_list_placer(list, number_of_XX):
    import random
    selected_numbers = []
    if number_of_XX < len(list):
        for y in range(number_of_XX):
            y = random.randint(1, len(list))
            while y in selected_numbers:
                y = random.randint(1, len(list))
            selected_numbers.append(y)
            for value in range(len(list)):
                if list[value] == "XX":
                    continue
                elif y == int(list[value]):
                    list[value] = "XX"
    return list
XX_list_placer(["01", "02", "03", "04", "05", "06", "07", "08", "09", "10"], 3)

# This function takes 2 lists of strings and one integer called number_selected. The function will return list1 with
# the index specified by number_selected - 1 changed. This value in list1 might be changed to GG or XX. This change will
# depend on what list2 at the index number-selected - 1 has. If it has XX, list1 will now have XX at the index, if it
# has GG, list1 will now have GG at the index.

def list_comparator(list1, list2, number_selected):
    if list2[number_selected - 1] == "XX":
        list1[number_selected - 1] = "XX"
        return list1, "XX"
    else:
        list1[number_selected - 1] = "GG"
        return list1, "GG"


# This function will display the grid, the number of numbers you have selected, and the number of lives you have.
def display(Front_grid, number_counter, heart_counter, outcome):
    print_grid(Front_grid)
    number_changer(number_counter, outcome) 
    print(heart_counter_display(heart_counter, outcome)) 
    
# This function will run an entire level. It will take 3 integers as parameters. The first integer will be the number
# of XX in the hidden grid. The second integer will be the number of numbers you need to select. The third integer will
# be the number of lives you have. The function will return True if you win the level and False if you lose the level.
# In the middle, the function will be calling other functions to let you play the game.
def level_runner(num_of_XX, nums_needed, num_of_hearts):
    list = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10",
         "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25"]
    Front_grid = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10",
         "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25"]
    Hidden_grid = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10",
         "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25"]
    number_counter = [0, nums_needed]
    heart_counter = [num_of_hearts]
    outcome = "00"
    list_of_nums_picked = []
    XX_list_placer(Hidden_grid, num_of_XX)
    display(Front_grid, number_counter, heart_counter, outcome)
    while number_counter[0] < number_counter[1] and heart_counter[0] > 0:
        y = input("Enter the number you want to pick on the grid: ")
        while y not in list:
            print("Invalid input!")
            y = input("Enter the number you want to pick on the grid: ")
        while y in list_of_nums_picked:
            print("You already picked that number!")
            y = input("Pick another number: ")
        Front_grid, outcome = list_comparator(Front_grid, Hidden_grid, int(y))
        display(Front_grid, number_counter, heart_counter, outcome)
        list_of_nums_picked.append(y)
    if number_counter[0] == number_counter[1]:
        print("You won the level!")
        return True
    else:
        print("You lost the level!?")
        return False

# This function will run the whole game. The main purpose of this function is to tell the instructions
# and run all the levels of the game as long as you haven't lost.
def game_runner():
    import random
    print("Welcome to the game!")
    x = input("Do you want to read the instructions? (Press 'Yes' if you want to or 'No' if you don't):")
    if x == "Yes":
        instructions()
    num_of_XX = 3
    nums_needed = 3 
    num_of_hearts = 3
    level = 1
    print("Level 1")
    check = level_runner(num_of_XX, nums_needed, num_of_hearts)
    if check == True:
        Answer = input("Do you want to go to the next sublevel? (Press 'Yes' if you want to or 'No' if you don't): ")
        if Answer == "Yes":
            level += 1
            while level < 6:
                y = input("Enter a random number between 1 to 3: ")
                while y not in "123":
                    y = input("Enter a random number between 1 to 3: ")
                x = random.randint(1, 3)
                if int(y) == x:
                    print("You got the right number, the hidden grid will only have " + str(num_of_XX + 1 + (level - 2)) + 
                          "XX you will need to select " + str(nums_needed + 1) + " numbers and you will have "
                        + str(num_of_hearts + 1), " ♥!")
                    input("Press enter to continue")
                    num_of_XX += 1 + (level - 2)
                    nums_needed += 1
                    num_of_hearts += 1
                    if nums_needed + num_of_XX >= 25:
                        nums_needed = 25 - num_of_XX
                        print("Wait a second, you got an impossible task!!! You will now need to select " + str(nums_needed)
                               + " numbers")
                        input("Press enter to continue")
                    print("Level " + str(level))
                    input("Press enter to continue")
                    check = level_runner(num_of_XX, nums_needed, num_of_hearts)
                    if check == False:
                        break
                else:
                    print("You got the wrong number, the hidden grid will now have " + str(num_of_XX + 2 + (level - 2)) + 
                          "XX, you will need to select " + str(nums_needed + 2) + " numbers and you will have "
                        + str(num_of_hearts) + " ♥")
                    input("Press enter to continue")
                    num_of_XX += 2 + (level - 2)
                    nums_needed += 2
                    if nums_needed + num_of_XX >= 25:
                        nums_needed = 25 - num_of_XX
                        print("Wait a second, you got an impossible task!!! You will now need to select "
                              + str(nums_needed) + " numbers")
                        input("Press enter to continue")
                    print("Level " + str(level))
                    input("Press enter to continue")
                    check = level_runner(num_of_XX, nums_needed, num_of_hearts)
                    if check == False:
                        break
                if level == 5:
                    break
                Answer = input("Do you want to go to the next sublevel? (Press 'Yes' if you want to or 'No' if you don't): ")
                if Answer == "Yes":
                    level += 1
                else:
                    break
            if check == False:
                print("You lost the game")
                input("Press enter to get out of the game")
                return False
            elif level < 5:
                print("You won the game!")
                input("Press enter to continue")
                print("Next try, try to win level 5!")
                input("Press enter to get out of the game")
            else:
                print("You won the entire game!")
                input("Press enter to continue")
                print("You got such a great luck, you should go to a casino!")
                input("Press enter to get out of the game")
        else:
            print("You won the game!")
            input("Press enter to continue")
            print("Next try, try to win level 5!")
            input("Press enter to get out of the game")
            return True
    else:
        print("You lost the game!?")
        print("You got such bad luck that it's impressive!")
        input("Press enter to get out of the game")
            

game_runner()