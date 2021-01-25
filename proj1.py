
0;136;0c"""
File: proj1.py
Author: Rooklyn Kline
Date: 10/25/19
Section: 15
E-mail: rkline2@umbc.edu
Description:
    This program is a baking sim where each player has to
bake baguettes, macarons, and croissants. They must go to
the grocery store to purchase ingredients. If they don't have enough
ingredients or they go over budget, they automatically loose the game.
"""

ASK_QUANTITY_QUESTION = ["How many ", " of ", " would you like to purchase? "]
BAGUETTES_QUANTITY = 100
BAGUETTES = 2
BAGUETTES_ING_QUANTITY_LIST = [112.5, 0, 0, 50, 0]
BAKE_INTRODUCTION = "We have everything we need! Ready! Set! Bake!"
BAGUETTES_NOT_FIRST = "We should really start the baguette dough first!"
BAKE_QUESTION = "What action would you like to cross off your list next? "
BAGUETTE_DOUGH_STATEMENT = "Ok, let's knead some baguette dough!"
BUTTER = 'butter'
CROISSANTS = 0
CROISSANTS_QUANTITY = 300
COLON = ":"
CROISSANTS_STATEMENT = "Let's make some flaky crescent goodness!"
CROISSANTS_ING_QUANTITY_LIST = [48, 12, 144, 39, 18]
DISHES_LIST = ["croissants", "macarons", "baguettes"]
DISHES_QUANTITY = [300, 600, 100]
DIDNT_BUY_ENOUGH = "You didn't buy enough"
DASH = '  -  '
EXCLAMATION_POINT = '!'
FAILURE = "You did not buy enough ingredients to even begin baking. You are a failure of all sorts. Good day."
FLOAT = "."
FOUR = 4
GREETING = "Welcome to the supermarket!"
INGREDIENTS = ['flour', 'eggs', 'butter', 'yeast', 'milk']
INGREDIENTS_DESCRIPTION_LIST = ["cups of flour", "eggs", "tbsp of butter", "tsp of yeast", "cups of milk"]
INDENT = ""
INTRO = "Baker! You must buy the following with $ "
ING_INTRO = "For"
INGREDIENT_DESCRIPTION = ["bags", "crates", "packs", "bags", "jugs"]
INVALID_ENTRY = "That is not a valid entry."
MACARONS = 1
MACARONS_QUANTITY = 600
MACARONS_ING_QUANTITY_LIST = [0, 60, 0, 0, 0]
MEASUREMENT = ['more cups', 'more eggs', 'more tbsp', 'more tsp', 'more cups']
MACARONS_STATEMENT = "Adorable sandwich cookies coming right up!"
NOTHING = 'NOTHING'
NUMBER_LIST = [1, 2, 3, 4]
OVERSPENT = "You ran out of money!"
ONE = 1
PURCHASE_QUESTION = 'What would you like to purchase (ENTER "NOTHING" to leave store) '
QUANTITY_QUESTION_PART_ONE = 0
QUANTITY_QUESTION_PART_TWO = 1
QUANTITY_QUESTION_PART_THREE = 2
QUESTION_LIST = ["Begin the baguette dough", "Make the macarons", "make the croissants", "bake the baguettes"]
REMAINING_TASKS_TITLE = "Here are your remaining tasks of the day "
TWO = 2
THREE = 3
WE_NEEDED = 'We needed:'
WINNER = "All done!  Let's hope we've PRUEven ourselves worthy."
WRONG_BAKING_RESPONSE = "Whoa, we should probably do everything else first!"
ZERO = 0

STARTING_FUNDS = 80.0

BUTTER_COST_PER_PACK = 1.25
BUTTER_REQUIRED = 144.0
TBSP_BUTTER_PER_PACK = 64.0

FLOUR_COST_PER_BAG = 2.5
CUPS_FLOUR_PER_BAG = 25.0
FLOUR_REQUIRED = 48.0 + 112.5

EGGS_COST_PER_CRATE = 1.9
EGGS_PER_CRATE = 24.0
EGGS_REQUIRED = 12.0 + 60.0

YEAST_COST_PER_BAG = 3.25
CUP_YEAST_PER_BAG = 6.0
YEAST_REQUIRED = 39 + 50

MILK_COST_PER_JUG = 2.75
GALLONS_MILK_PER_JUG = 1.0
MILK_REQUIRED = 18.0

CUPS_IN_GALLON = 16
TSP_IN_CUP = 48


def print_shopping_list():
    """
    Prints the ingredients that are required for the user to purchase as well as its budget.
    :return: none
    """
    starting_funds = str(STARTING_FUNDS)
    print(INTRO + starting_funds + COLON)
    print()
    # for-loop that will print out each ingredient as well as the quantity
    for list_value in range(len(DISHES_LIST)):
        print(ING_INTRO, DISHES_QUANTITY[list_value], DISHES_LIST[list_value] + COLON)
        if list_value == CROISSANTS:
            for ingredients_list_value in range(len(CROISSANTS_ING_QUANTITY_LIST)):
                if CROISSANTS_ING_QUANTITY_LIST[ingredients_list_value] != 0:
                    print(INDENT, CROISSANTS_ING_QUANTITY_LIST[ingredients_list_value],
                          INGREDIENTS_DESCRIPTION_LIST[ingredients_list_value])
            print()
        if list_value == MACARONS:
            for ingredients_list_value in range(len(MACARONS_ING_QUANTITY_LIST)):
                if MACARONS_ING_QUANTITY_LIST[ingredients_list_value] != 0:
                    print(INDENT, MACARONS_ING_QUANTITY_LIST[ingredients_list_value],
                          INGREDIENTS_DESCRIPTION_LIST[ingredients_list_value])
            print()
        if list_value == BAGUETTES:
            for ingredients_list_value in range(len(BAGUETTES_ING_QUANTITY_LIST)):
                if BAGUETTES_ING_QUANTITY_LIST[ingredients_list_value] != 0:
                    print(INDENT, BAGUETTES_ING_QUANTITY_LIST[ingredients_list_value],
                          INGREDIENTS_DESCRIPTION_LIST[ingredients_list_value])
            print()
                
            
def nowhitespace(input_response):
    """
    This function removes all of the white spaces of any statement
    :param input_response: This parameter represents the
     word you would like to remove all of the white spaces from
    :return: the parameter as a single word
    """
    input_response = input_response.strip()
    input_response = input_response.split()
    input_response = INDENT.join(input_response)
    return input_response


def go_shopping():
    """
    This function will ask the user what they would like to purchase.
    It will also ask for the quantity of the specific item and record it.
    It will print out a over budget statement if the user went over budget.
    :return: one list that contains all the ingredients amount. The
    items are classified by using a sub-list.
    """
    flour_shopping_list = []
    egg_shopping_list = []
    butter_shopping_list = []
    yeast_shopping_list = []
    milk_shopping_list = []
    shopping_list = [flour_shopping_list] + [egg_shopping_list] + \
    [butter_shopping_list] + [yeast_shopping_list] + \
    [milk_shopping_list]
    starting_funds = 80.0
    ask_ingredients = BUTTER
    print(GREETING)
    # while-loop that will continue looping until the input is "NOTHING" or
    # its funds are less than zero
    while (ask_ingredients.upper() != NOTHING) and (starting_funds >= 0):
        ask_ingredients = nowhitespace(input(PURCHASE_QUESTION))
        ask_ingredients = ask_ingredients.lower()
        if ask_ingredients.upper() == NOTHING:
            print()
        elif (ask_ingredients not in INGREDIENTS) or (ask_ingredients == INDENT):
            print(INVALID_ENTRY)
        # for loop that validates the user's input and finds the correct follow-up question
        for list_value in range(len(INGREDIENTS)):
            if INGREDIENTS[list_value] == ask_ingredients:
                ask_quantity = INDENT
                while (ask_quantity == INDENT) or (float(ask_quantity) < 0.0):
                    ask_quantity = nowhitespace(input(ASK_QUANTITY_QUESTION[QUANTITY_QUESTION_PART_ONE] +
                                                      INGREDIENT_DESCRIPTION[list_value] +
                                                      ASK_QUANTITY_QUESTION[QUANTITY_QUESTION_PART_TWO] +
                                                      INGREDIENTS[list_value] +
                                                      ASK_QUANTITY_QUESTION[QUANTITY_QUESTION_PART_THREE]))
                    if ask_quantity == INDENT or float(ask_quantity) < 0:
                        print(INVALID_ENTRY)
                    elif float(ask_quantity) > 0.0:
                        # finds the correct ingredient and calculates its cost and
                        # appends the quantity to its specific list
                        for ingredient_value in range(1):
                            if ask_ingredients == INGREDIENTS[ingredient_value]:
                                starting_funds = starting_funds - (float(ask_quantity) * FLOUR_COST_PER_BAG)
                                flour_shopping_list.append(ask_quantity)
                            elif ask_ingredients == INGREDIENTS[ingredient_value + ONE]:
                                starting_funds = starting_funds - (float(ask_quantity) * EGGS_COST_PER_CRATE)
                                egg_shopping_list.append(ask_quantity)
                            elif ask_ingredients == INGREDIENTS[ingredient_value + TWO]:
                                starting_funds = starting_funds - (float(ask_quantity) * BUTTER_COST_PER_PACK)
                                butter_shopping_list.append(ask_quantity)
                            elif ask_ingredients == INGREDIENTS[ingredient_value + THREE]:
                                starting_funds = starting_funds - (float(ask_quantity) * YEAST_COST_PER_BAG)
                                yeast_shopping_list.append(ask_quantity)
                            elif ask_ingredients == INGREDIENTS[ingredient_value + FOUR]:
                                starting_funds = starting_funds - (float(ask_quantity) * MILK_COST_PER_JUG)
                                milk_shopping_list.append(ask_quantity)
    if starting_funds < 0.0:
        print(OVERSPENT)
    print()
    return shopping_list


def check_items_enough(shopping_cart):
    """
    A function that will determine if the user has enough ingredients. If they
    do not, then it will print out how much they still need
    :param shopping_cart:  A list of all of the imputed values
    :return: returns false if they don't have enough in ingredients. Returns true if the user does have enough
    ingredients
    """
    difference_list = []
    # for-loop that finds the total quantity amount of each ingredient (sublist)
    for first_list_value in range(len(shopping_cart)):
        total = 0.0
        for second_list_value in range(len(shopping_cart[first_list_value])):
            list_value = float(shopping_cart[first_list_value][second_list_value])
            total = total + list_value
        # for-loop that finds ingredient that corresponds to the value
        # and convert the value (if necessary) to cups or tsp and
        # will calculate its difference if its less than the required amount
        for num in range(1):
            if first_list_value == num:
                total_flour_cups = total * CUPS_FLOUR_PER_BAG
                if total_flour_cups < FLOUR_REQUIRED:
                    ingredient_difference = FLOUR_REQUIRED - total_flour_cups
                    difference_list.append(ingredient_difference)
                    print(DIDNT_BUY_ENOUGH, INGREDIENTS[first_list_value] + EXCLAMATION_POINT,
                          WE_NEEDED, ingredient_difference, MEASUREMENT[first_list_value])
            elif first_list_value == num + ONE:
                total_eggs = total * EGGS_PER_CRATE
                if total_eggs < EGGS_REQUIRED:
                    ingredient_difference = EGGS_REQUIRED - total_eggs
                    difference_list.append(ingredient_difference)
                    print(DIDNT_BUY_ENOUGH, INGREDIENTS[first_list_value] + EXCLAMATION_POINT,
                          WE_NEEDED, ingredient_difference, MEASUREMENT[first_list_value])
            elif first_list_value == num + TWO:
                total_butter = total * TBSP_BUTTER_PER_PACK
                if total_butter < BUTTER_REQUIRED:
                    ingredient_difference = BUTTER_REQUIRED - total_butter
                    difference_list.append(ingredient_difference)
                    print(DIDNT_BUY_ENOUGH, INGREDIENTS[first_list_value] + EXCLAMATION_POINT,
                          WE_NEEDED, ingredient_difference, MEASUREMENT[first_list_value])
            elif first_list_value == num + THREE:
                total_yeast = total * CUP_YEAST_PER_BAG
                total_yeast *= float(TSP_IN_CUP)
                if total_yeast < YEAST_REQUIRED:
                    ingredient_difference = float(YEAST_REQUIRED) - total_yeast
                    difference_list.append(ingredient_difference)
                    print(DIDNT_BUY_ENOUGH, INGREDIENTS[first_list_value] + EXCLAMATION_POINT,
                          WE_NEEDED, ingredient_difference, MEASUREMENT[first_list_value])
            elif first_list_value == num + FOUR:
                total_milk = total * GALLONS_MILK_PER_JUG
                total_milk *= float(CUPS_IN_GALLON)
                if total_milk < MILK_REQUIRED:
                    ingredient_difference = MILK_REQUIRED - total_milk
                    difference_list.append(ingredient_difference)
                    print(DIDNT_BUY_ENOUGH, INGREDIENTS[first_list_value] + EXCLAMATION_POINT,
                          WE_NEEDED, ingredient_difference, MEASUREMENT[first_list_value])
    if len(difference_list) > 0:
        print(FAILURE)
        return False
    else:
        return True


def is_valid_input(index, tasks):
    """
    determines whether the user input is valid in the bake() function
    given the list of supplied tasks.
    :param index: represents the length of the list
    :param tasks: represents the list of the task values
    :return: true if the index is valid and false if index is not valid
    """
    if FLOAT in index:
        print(INVALID_ENTRY)
        return False
    index = int(index)
    word_value = index - 1
    if (index > len(tasks)) or (index < ZERO):
        print(INVALID_ENTRY)
        return False
    if (len(tasks) <= THREE) and (len(tasks) > ONE):
        if tasks[word_value] == QUESTION_LIST[THREE]:
            print(WRONG_BAKING_RESPONSE)
            return False
        else:
            if tasks[word_value] == QUESTION_LIST[ONE]:
                print(MACARONS_STATEMENT)
                return True
            else:
                print(CROISSANTS_STATEMENT)
                return True
    elif QUESTION_LIST[ZERO] in tasks and len(tasks) > THREE:
        if tasks[word_value] == QUESTION_LIST[ZERO]:
            print(BAGUETTE_DOUGH_STATEMENT)
            return True
        else:
            print(BAGUETTES_NOT_FIRST)
            return False
    else:
        return True


def print_task_list(tasks_remaining):
    """
    prints the tasks that are remaining for the user to do
    in the bake() function
    :param tasks_remaining: a list of the menu options
    :return: none
    """
    for list_value in range(len(tasks_remaining)):
        print(str(list_value + 1) + DASH + tasks_remaining[list_value])


def bake():
    """
    presents the user with a list of tasks
    and asks to perform them in the correct order
    :return: none
    """
    question_list_copy = ["Begin the baguette dough", "Make the macarons",
                          "make the croissants", "bake the baguettes"]
    print(BAKE_INTRODUCTION)
    # this while loop will remain true until there isn't any more tasks
    # to perform
    while len(question_list_copy) > 0:
        print(REMAINING_TASKS_TITLE)
        print_task_list(question_list_copy)
        bake_action = nowhitespace(input(BAKE_QUESTION))
        if is_valid_input(bake_action, question_list_copy):
            question_list_copy.remove(question_list_copy[int(bake_action) - 1])
    print(WINNER)


if __name__ == "__main__":
    print_shopping_list()
    shopping_list_valid = check_items_enough(go_shopping())
    if shopping_list_valid:
        bake()
