from Items_List import Currency
from Characters import Logos_and_Characters
from Gang_Members import Enemies
from Characters import Frames
from Items_List import Guns
from Items_List import ItemsList
from Items_List import FUSION
from Items_List import Food
import time
import random
import os



def printt(string, strDelay):
  for i in str(string + "\n"):
    print(i, end="", flush=True)
    time.sleep(strDelay)



FusionTarget = ""
FusionUse = 0



def FUSIONATTACK():
    global FusionUse

    if FusionUse == 0:
        FusionUse = FusionUse + 1

        os.system('cls')
        printt("You/Doomsday Hong: PUBLIC DOMAIN EXPANSION: INFINITE FUSION!", 0.07)
        time.sleep(1)
        print("\n"), print(Logos_and_Characters['Fusion'])
        time.sleep(2)
        os.system('cls')

        for i in range(0, len(Frames)):
            print(Frames[i]), time.sleep(2), os.system('cls')
        
        time.sleep(2)


        Currency["HP"] += 90
        Enemies[FusionTarget]["HP"] -= 90


        if FusionTarget == "King Of Hearts" and Enemies['King Of Hearts']['HP'] <= 0:
            os.system('cls')
            print(Logos_and_Characters['Hole In One King Of Hearts']), '\n', print(Logos_and_Characters['Super Finish'])
            time.sleep(2)

        Guns['detroit fusion strike']['Owned'] = True
        ItemsList.append(Guns['detroit fusion strike'])
        Guns['detroit fusion strike']['Equipped'] = True

        time.sleep(1)
    else:
        print("You already used fusion")
        time.sleep(1)
        os.system('cls')



def food_search():
    global ItemsList
    for i in ItemsList:
        print('\n>', i)

    foodinput = input("|>")
    Food_Find = Food.get(foodinput.lower())

    if Food_Find is not None and Food_Find['Amount Owned'] >= 1:
        Currency["HP"] += Food_Find["HP Increase"]
        Food_Find['Amount Owned'] -= 1

        if Food_Find['Amount Owned'] == 0:
            ItemsList.remove(Food_Find)

        print(f"You used one {Food_Find['Name']}!")
        time.sleep(1)


def Gamble_Central():
    """Gamble Central"""

    MoneyGamble = 0
    
    def Gamble_Crentral_Attack():
        MissChance = random.randint(1,4)
        for i in ItemsList:
                print(i)

        print("\nSelect what you want to attack with")

        AttackInput = input('[ATTACK]>')
        AttackFChoice = Guns.get(AttackInput.lower())

        if AttackFChoice is not None and AttackFChoice['Equipped'] and MissChance <= 3:
            print("You chose", AttackFChoice['Name'], 'and dealed', AttackFChoice['Damage'], 'damage!')
            Enemies['King Of Hearts']['HP'] -= AttackFChoice['Damage']
            time.sleep(2)

            if MissChance == 1:
                print("You chose", AttackFChoice['Name'], 'and dealed', AttackFChoice['Critical Damage'], 'CRITICAL damage!')
                Enemies['King Of Hearts']['HP'] -= AttackFChoice['Critical Damage']
                time.sleep(2)



    def GambleFight():
        global MoneyGamble
        global FusionTarget

        FusionTarget = "King Of Hearts"

        print(Logos_and_Characters['King Of Hearts']), '\n', print(Enemies['King Of Hearts']['Name']), '\n', print(f"ENEMY HP:", Enemies['King Of Hearts']['HP'])
        print("\nYOUR HP:", Currency['HP']), '\n', print("<-------------------------------------------------------------->")

        if Currency['HP'] <= int(MoneyGamble) / 3 and FUSION['Owned'] == True and FusionUse == 0:
            print("FUSION IS AVAILABLE!")

        print("\nAttack"), '\n', print("Food")


        King_Of_Hearts_Attack_Menu = random.randint(1,4)
        if King_Of_Hearts_Attack_Menu <= 3:
            print("King Of Hearts dealed", Enemies['King Of Hearts']['dmg'], 'damage!')
            Currency['HP'] -= Enemies['King Of Hearts']['dmg']
        else:
            print("King Of Hearts missed!")

        
        OptionInput = input("|>")

        HeartsMatch = OptionInput.lower()

        match HeartsMatch:
            case 'food':
                food_search()
            case 'attack':
                Gamble_Crentral_Attack()
            case 'fusion' if Currency['HP'] < 40 and FUSION['Owned'] == True and FusionUse == 0:
                FUSIONATTACK()



    def GambleSet():
        global MoneyGamble
        GambleLoop = False

        MoneyInput = int(input("[MONEY]>"))

        if type(MoneyInput) == int and Currency['Money'] >= int(MoneyInput):
            GambleLoop = True

            Enemies['King Of Hearts']['HP'] = int(MoneyInput) * 3
            Enemies['King Of Hearts']['dmg'] = int(MoneyInput) / 2

            Currency['HP'] = 100 + int(MoneyInput)

            MoneyGamble = int(MoneyInput) * 3
            os.system('cls')

        else:
            print("you either dont have enough money or typed a letter")
            time.sleep(1)
            os.system('cls')


        while GambleLoop == True:
            if Enemies['King Of Hearts']['HP'] <= 0:
                os.system('cls')
                print (f"\nYou defeated The King Of Hearts and recieved {int(MoneyGamble)} money")

                Currency['Money'] + int(MoneyGamble)

                Enemies['King Of Hearts']['HP'] = 100
                Enemies['King Of Hearts']['dmg'] = 10

                MoneyGamble = 0

                time.sleep(2)

                break
            if Currency['HP'] <= 0:
                print("You died")

                Enemies['King Of Hearts']['HP'] = 100
                Enemies['King Of Hearts']['dmg'] = 10

                MoneyGamble = 0

                time.sleep(1)
                os.system('cls')

                break
            GambleFight()



    print(Logos_and_Characters['Gamble Central']), '\n', print("Welcome to gamble central! Gamble ALL YOUR MONIE!")

    print("\n<---------- OPTIONS ---------->"), '\n', print("Gamble Match")
    print("\n<---------- OTHER ---------->"), '\n', print("Back")

    Gamble_Option = input("[GAMBLE]>")

    Gamble_Match = Gamble_Option.lower()

    match Gamble_Match:
        case "gamble match":
            GambleSet()
        case "back":
            os.system('cls')

