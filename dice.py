import random 


#these are the diagrams which will be printed to the screen, stored in a dictionary with their integer value
DICE_ART = {
     1: (
        "┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘",
    ),
    2: (
        "┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘",
    ),
    3: (
        "┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘",
    ),
    4: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    5: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    6: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘",
    ),}

DIE_HEIGHT = len(DICE_ART[1])
DIE_WIDTH = len(DICE_ART[1][0])
DIE_FACE_SEPARATOR = " "


#this function's pupose is to generate the dice diagram when the user views the result

def generate_dice_diagram(dice_values):

    dice=[]
    for value in dice_values:
        dice.append(DICE_ART[value])
    

    dice_rows=[]
    for row_index in range(DIE_HEIGHT):

        row_components=[]
        for die in dice:
            row_components.append(die[row_index])
        
        row_string = DIE_FACE_SEPARATOR.join(row_components)
        dice_rows.append(row_string)
    

    width = len(dice_rows[0])
    diagram_header = "RESULT".center(width, "*")
    dice_diagram = "/n".join([diagram_header] + dice_rows)
    return dice_diagram


#this function checks if the input is between 1-6 and stores it, else asks the user to enter a valid number

def parse_input (input_string):

    if input_string.strip() in {"1", "2", "3", "4", "5", "6"}:
        return int(input_string)
    else:
        print("Enter another valid number from 1 to 6!")
        raise SystemExit(1)



#This function asks how many numbers to generate and stores it then iterates the rolls and returns it

def roll_dice(num_dice):
    roll_results = []

    for x in range (num_dice):
        roll = random.randint(1,6)
    
        roll_results.append(roll)

    return roll_results


# ---------------- T  H I S   I S   T H E   M A I N   C O D E   B L O C K -------------------------------

#1. user input and storing
num_dice_input = input("How many dices do you want to roll? (max is 6) ")
num_dice = parse_input(num_dice_input)


#2. rolls the dice
roll_results = roll_dice(num_dice)
print(roll_results)

#3. generate the diagrams and display
dice_diagram = generate_dice_diagram(roll_results)
print(f"\n{dice_diagram}")








