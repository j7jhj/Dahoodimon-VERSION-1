from Characters import Logos_and_Characters
from Items_List import Currency
from Items_List import Food
from Items_List import ItemsList
import time

# All the restaraunts in the game
def The_Game_Beery():
    """The Game Beery: But hey, thats just a beery, a GAME BEERY, thanks for drinking!"""
    print(Logos_and_Characters['Game Beery']), '\n', print("<----------------------------------------------------------------------------->")
    print("MENU: (30 Money) The Last Beery | (20 Money) FNAF Lore Drop | (80 Money) Thats just a beery, a GAME BEERY")
    print("<----------------------------------------------------------------------------->")

    Game_Beery_option = input("|>")
    if Game_Beery_option.lower() == ("the last beery") and Currency['Money'] >= 30:
        Food['the last beery']['Amount Owned'] += 1
        Currency['Money'] -= 30

        if Food['the last beery'] in ItemsList:
            print("'Added The Last Beery in inventory")
        else:
            ItemsList.append(Food['the last beery'])

        print(f"You've recieved one 'The Last Beery' drink! | Current balance: {Currency['Money']}")

        time.sleep(1)
    elif Game_Beery_option.lower() == ("fnaf lore drop") and Currency['Money'] >= 20:
        Food['fnaf lore drop']['Amount Owned'] += 1
        Currency['Money'] -= 20

        if Food['fnaf lore drop'] in ItemsList:
            print("'Added FNAF Lore Drop in inventory")
        else:
            ItemsList.append(Food['fnaf lore drop'])

        print(f"You've recieved one 'FNAF Lore Drop' drink! | Current balance: {Currency['Money']}")

        time.sleep(1)
    elif Game_Beery_option.lower() == ("thats just a beery, a game beery") and Currency['Money'] >= 80:
        Food['thats just a beery, a game beery']['Amount Owned'] += 1
        Currency['Money'] -= 80

        if Food['thats just a beery, a game beery'] in ItemsList:
            print("'Added Thats Just A BEERY, A GAME BEERY! in inventory")
        else:
            ItemsList.append(Food['thats just a beery, a game beery'])

        print(f"You've recieved one 'Thats Just A BEERY, A GAME BEERY!' drink! | Current balance: {Currency['Money']}")

        time.sleep(1)
    else:
        print("You dont have any money/returning back to menu")

        time.sleep(1)



def Jamals():
    """Jamal Inc. Get delicious treats!"""
    print(Logos_and_Characters['Jamals']), '\n', print("<----------------------------------------------------------------------------->")
    print("MENU: (32 Money) Jamanut The Donut | ( 15 Money) Johannes The Cookie")
    print("<----------------------------------------------------------------------------->")

    Jamal_option = input("|>")
    """Jamanut the Donut  + Johannes Cookie"""
    if Jamal_option.lower() == ("jamanut the donut") and Currency['Money'] >= 32:
        Food['jamanut the donut']['Amount Owned'] += 1
        Currency['Money'] -= 32

        if Food['jamanut the donut'] in ItemsList:
            print("'Added Jamanut Donut in inventory")
        else:
            ItemsList.append(Food['jamanut the donut'])

        print(f"You've recieved one 'Jamanut The Donut'! | Current balance: {Currency['Money']}")
        
        time.sleep(1)
    elif Jamal_option.lower() == ("johannes the cookie") and Currency['Money'] >= 15:
        Food['johannes the cookie']['Amount Owned'] += 1
        Currency['Money'] -= 15

        if Food['johannes the cookie'] in ItemsList:
            print("'Added Johannes The Cookie in inventory")
        else:
            ItemsList.append(Food['johannes the cookie'])

        print(f"You've recieved one 'Johannes The Cookie'! | Current balance: {Currency['Money']}")

        time.sleep(1)
    else:
        print("You dont have any money/returning back to menu")

        time.sleep(1)



def DahoodlinHut():
    """Da Hoodlin Hut! Prices are so low!"""
    print(Logos_and_Characters['Da Hoodlin Hut']), '\n', print("<----------------------------------------------------------------------------->")
    print("MENU: (50 Money) The Wild Wolf | ( 20 Money) Da Hood Is Real")
    print("<----------------------------------------------------------------------------->")

    DahoodlinHut_option = input("|>")
    """The Wild Wolf + Da Hood Is Real"""
    if DahoodlinHut_option.lower() == ("the wild wolf") and Currency['Money'] >= 50:
        Food['the wild wolf']['Amount Owned'] += 1
        Currency['Money'] -= 50

        if Food['the wild wolf'] in ItemsList:
            print("'Added The Wild Wolf in inventory")
        else:
            ItemsList.append(Food['the wild wolf'])

        print(f"You've recieved one 'The Wild Wolf'! | Current balance: {Currency['Money']}")
        
        time.sleep(1)
    elif DahoodlinHut_option.lower() == ("da hood is real") and Currency['Money'] >= 20:
        Food['da hood is real']['Amount Owned'] += 1
        Currency['Money'] -= 20

        if Food['da hood is real'] in ItemsList:
            print("'Added Da Hood Is Real in inventory")
        else:
            ItemsList.append(Food['da hood is real'])

        print(f"You've recieved one 'Da Hood Is Real'! | Current balance: {Currency['Money']}")

        time.sleep(1)
    else:
        print("You dont have any money/returning back to menu")

        time.sleep(1)
