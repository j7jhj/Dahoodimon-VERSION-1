from Items_List import Currency
from Characters import Logos_and_Characters
from Characters import DodgeFrames
from Characters import WeaveOmegaAttack
from Gang_Members import Enemies
from Characters import FusionFrames
from Items_List import Guns
from Items_List import ItemsList
from Items_List import FUSION
from Items_List import Food
from Items_List import WeaveState
from Items_List import TechniqueKeys
import time
import random
import os



def printt(string, strDelay):
  for i in str(string + "\n"):
    print(i, end="", flush=True)
    time.sleep(strDelay)



MainTarget = ""
FusionUse = 0
WeaveStateUse = 1
WeaveStateActive = False
WeaveDodgeUse = 3
WeavePowerUpuse = 3
ShopLoop = True
WeaveUltAttack = 0

def WeavePowerUp():
    global WeaveStateUse
    global WeavePowerUpuse

    if WeaveStateActive == True and Currency['HP'] <= 40:
        os.system('cls')
        print(Logos_and_Characters['Power Up'])

        Currency['HP'] += 40
        WeavePowerUpuse = WeavePowerUpuse - 1

        time.sleep(1)
        os.system('cls')



def WeaveStateAttack():
    global WeaveStateUse
    global WeaveStateActive

    if WeaveStateUse == 1 and WeaveState['Owned'] == True: 

        os.system('cls')
        printt("You: This.. This is the true power of the Weave Nation!", 0.07)
        time.sleep(1)
        print("\n"), print(Logos_and_Characters['Weave State'])

        WeaveStateActive = WeaveStateActive = True
        WeaveStateUse = WeaveStateUse - 1
        Currency['HP'] += 60

        time.sleep(1), os.system('cls')

    else:
        print("Technique not learned")



def WeaveDodgeMove():
    global WeaveDodgeUse

    if WeaveDodgeUse > 0:
        os.system('cls')
        for i in range(0, len(DodgeFrames)):
            print(DodgeFrames[i]), time.sleep(0.5), os.system('cls')

        Currency['HP'] += Enemies[MainTarget]['dmg']
        WeaveState['ULTGauge'] += 1
        WeaveDodgeUse = WeaveDodgeUse - 1
        WeaveUltAttack + 1
        
        time.sleep(1), os.system('cls')

        if WeaveState['ULTGauge'] == 3:
            os.system('cls')
            for i in range(0, len(WeaveOmegaAttack)):
                print(WeaveOmegaAttack[i]), time.sleep(1), os.system('cls')
            
            Enemies[MainTarget]['HP'] -= Enemies[MainTarget]['dmg'] * 5
            WeaveState['ULTGauge'] == 0 

            if Enemies[MainTarget]['HP'] <= 0:
                os.system('cls')
                print(Logos_and_Characters['Weave Super Finish'])
                time.sleep(2)
            time.sleep(1)

    else:
        print("Already used all dodges")
        time.sleep(1)
        os.system('cls')


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

        for i in range(0, len(FusionFrames)):
            print(FusionFrames[i]), time.sleep(2), os.system('cls')
        
        time.sleep(2)


        Currency["HP"] += 90
        Enemies[MainTarget]["HP"] -= 90


        if MainTarget == "King Of Hearts" and Enemies['King Of Hearts']['HP'] <= 0:
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
        global MainTarget

        if WeavePowerUpuse >= 1:
            WeavePowerUp()

        MainTarget = "King Of Hearts"

        print(Logos_and_Characters['King Of Hearts']), '\n', print(Enemies['King Of Hearts']['Name']), '\n', print(f"ENEMY HP:", Enemies['King Of Hearts']['HP'])
        print("\nYOUR HP:", Currency['HP']), '\n', print("<-------------------------------------------------------------->")

        if Currency['HP'] <= int(MoneyGamble) / 3 and FUSION['Owned'] == True and FusionUse == 0:
            print("FUSION IS AVAILABLE!")
        elif Currency['HP'] <= int(MoneyGamble) / 3 and WeaveState['Owned'] == True and WeaveStateUse == 1:
            print("WEAVE State is available")

        print("\nAttack"), '\n', print("Food")


        King_Of_Hearts_Attack_Menu = random.randint(1,4)
        if King_Of_Hearts_Attack_Menu <= 3:
            print("King Of Hearts dealed", Enemies['King Of Hearts']['dmg'], 'damage!')
            Currency['HP'] -= Enemies['King Of Hearts']['dmg']
        else:
            print("King Of Hearts missed!")

        if WeaveStateActive == True and King_Of_Hearts_Attack_Menu <= 1:
            WeaveDodgeMove()
        
        OptionInput = input("|>")

        HeartsMatch = OptionInput.lower()

        match HeartsMatch:
            case 'food':
                food_search()
            case 'attack':
                Gamble_Crentral_Attack()
            case 'fusion' if Currency['HP'] < 40 and FUSION['Owned'] == True and FusionUse == 0:
                FUSIONATTACK()
            case 'weave state' if Currency['HP'] <= 60:
                WeaveStateAttack()  


    def GambleSet():
        global MoneyGamble
        global WeaveStateUse 
        global WeaveStateActive 
        global WeaveDodgeUse 
        
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

                WeaveStateUse = 1
                WeaveStateActive = False
                WeaveDodgeUse = 5
                
                MoneyGamble = 0

                time.sleep(2)

                break
            if Currency['HP'] <= 0:
                print("You died")

                Enemies['King Of Hearts']['HP'] = 100
                Enemies['King Of Hearts']['dmg'] = 10

                WeaveStateUse = 1
                WeaveStateActive = False
                WeaveDodgeUse = 5

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

def Shop():
    os.system('cls')
    print(Logos_and_Characters['Shop']), '\n', print("<-------------------------------------------------------------->")
    print("\n<---------- GUNS ---------->")

    PriceList = ["Tyrones Last Shot: 200 MONEY", "The Fat Man: 600 MONEY", "Willy's Steampunk Cannon: 1000 MONEY", "Tech Support's Wrath: 400 MONEY"]

    for i in range(len(PriceList)):
        print("\n"), print(PriceList[i])

    print("<---------- OTHER ---------->"), '\n', print("Purchase"), '\n', print("leave")
    
    PurchaseOption = input("[SHOP]>")
    PurchaseMatch = PurchaseOption.lower()

    match PurchaseOption:
        case "leave":
            printt("\nCome back soon", 0.07)

            ShopLoop == False

            time.sleep(1)
            os.system('cls')
        case "purchase":
            Purchase = input("\n[PURCHASE]>")
            PurchaseMatch = Guns.get(Purchase.lower())

            if PurchaseMatch['Owned'] == False and Currency['Money'] >= PurchaseMatch['Price']:
                os.system('cls')

                print(f"You have bought {PurchaseMatch['Name']} for {PurchaseMatch['Price']} MONEY")

                PurchaseMatch['Owned'] = True
                Currency['Money'] -= PurchaseMatch['Price']
                ItemsList.append(PurchaseMatch)

                time.sleep(2)
                os.system('cls')
            else:
                print("You either own this gun already or dont have enough money")
                ShopLoop == False

def RaidShop():
    print(Logos_and_Characters['RAIDS Shops']),
    if Currency['Ranked XP'] >= 300:
        print(Logos_and_Characters['S RANK'])
    print("\n<-------------- ITEMS -------------->")
    print("\nWeave State Key | 1500 RAID COINS"), print("\n100 Money | 10 Raid Coins"), print("\n<-------------- PICK -------------->")

    ShopInput = input("[RAIDS SHOP]> ")
    ShopMatch = ShopInput.lower()

    match ShopMatch:
        case "weave state key" if Currency['RAIDS Coins'] >= 1500:
            TechniqueKeys['Weave State Key'] == True
            Currency['RAIDS Coins'] -= 150

            print(f"You bought a Weave State Key! | You now have {Currency['RAIDS Coins']} RAIDS Coins LEFT!")

            time.sleep(1)
            os.system('cls')
        case "100 money" if Currency['RAIDS Coins'] >= 10:
            Currency['Money'] += 100
            Currency['RAIDS Coins'] -= 10

            print(f"You bought 100 Money! | You now have {Currency['RAIDS Coins']} RAIDS Coins LEFT!")

            time.sleep(1)
            os.system('cls')
    
    print("Insufficient Funds or typed incorrectly")

    time.sleep(1)
    os.system('cls')



def MarshallOHIORaid():

    Marshall_Ohio_Loop = True
    global WeaveUltAttack
    global WeaveDodgeUse
    global MainTarget
    global WeavePowerUpuse
    global WeaveStateActive

    def Marshall_Ohio_Attack():
        MissChance = random.randint(1,4)
        for i in ItemsList:
            print(i)

        print("\nSelect what you want to attack with")

        AttackInput = input('[ATTACK]>')
        AttackFChoice = Guns.get(AttackInput.lower())

        if AttackFChoice is not None and AttackFChoice['Equipped'] == True and MissChance <= 3:
            print("You chose", AttackFChoice['Name'], 'and dealed', AttackFChoice['Damage'], 'damage!')
            Enemies['Marshall Ohio']['HP'] -= AttackFChoice['Damage']
            time.sleep(2)

            if MissChance == 1:
                print("You chose", AttackFChoice['Name'], 'and dealed', AttackFChoice['Critical Damage'], 'CRITICAL damage!')
                Enemies['Marshall Ohio']['HP'] -= AttackFChoice['Critical Damage']
                time.sleep(2)



    def MarshallOhioMenu():
        """Battle Menu"""
        os.system('cls') 
        
        if WeavePowerUpuse >= 0:
            WeavePowerUp()

        print(Logos_and_Characters['Marshall Ohio']), '\n', print(Enemies['Marshall Ohio']['Name']), '\n', print(f"ENEMY HP:", Enemies['Marshall Ohio']['HP'])
        print("\nYOUR HP:", Currency['HP']), '\n', print("<-------------------------------------------------------------->")

        if Currency['HP'] < 40 and FUSION['Owned'] == True and FusionUse == 0:
            print("FUSION IS AVAILABLE!")
        elif Currency['HP'] < 60 and WeaveState['Owned'] == True and WeaveStateUse == 1:
            print("WEAVE State is available")

        TrevorChance = random.randint(1,4)

        if TrevorChance <= 3:
            print("[Marshall Ohio dealed", Enemies['Marshall Ohio']['dmg'], 'damage!]')
            Currency['HP'] -= Enemies['Marshall Ohio']['dmg']
        else:
            print("Marshall Ohio missed!")

        if WeaveStateActive == True and TrevorChance <= 1:
            WeaveDodgeMove()

        print("\nAttack"), '\n', print("Food")

        OptionInput = input("|>")
        DistrictOneMatch = OptionInput.lower()

        match DistrictOneMatch:
            case 'food':
                food_search()
            case 'attack':
                Marshall_Ohio_Attack()
            case 'fusion' if Currency['HP'] < 40 and FUSION['Owned'] == True and FusionUse == 0:
                FUSIONATTACK()
            case 'weave state' if Currency['HP'] < 60:
                WeaveStateAttack()  



    while Marshall_Ohio_Loop == True:

        if Enemies['Marshall Ohio']['HP'] <= 0:
            
            Currency['RAIDS Coins'] += 100    
            if Currency['Ranked XP'] >= 300:
                Currency['RAIDS Coins'] += 50  
                         
            print("You defeated Marshall Ohio and recieved 10 RAIDS Coins | Gained 10 RP")
                
            Currency['HP'] = 100
            Enemies['Marshall Ohio']['HP'] = 2000

            Currency['Ranked XP'] += 10

            FusionUse == 0
            WeaveStateUse = 1
            WeaveStateActive = False
            WeaveDodgeUse = 4
            WeavePowerUpuse = 3
            WeaveUltAttack = 0

            MainTarget = ""

            time.sleep(2)

            break
            
        if Currency['HP'] <= 0:

            print("You were defeated by Marshall Ohio. | Lost 5 RP")

            Currency['HP'] = 100
            Currency['Ranked XP'] -= 5
            Enemies['Marshall Ohio']['HP'] = 2000         
            MainTarget = ""
            if FusionUse == 1:
                Guns['detroit fusion strike']['Owned'] = False
                if Guns['Detroit fusion strike'] in ItemsList:
                    ItemsList.remove(Guns['detroit fusion strike'])
                Guns['detroit fusion strike']['Equipped'] = False

            FusionUse == 0
            WeaveStateUse = 1
            WeaveStateActive = False
            WeaveDodgeUse = 4
            WeavePowerUpuse = 3
            WeaveUltAttack = 0

            time.sleep(2)

            break

        MarshallOhioMenu()



def RaidMenu():
    print(Logos_and_Characters['RAIDS']), "\n<-------------------------------------------------------------->"
    if Currency['Ranked XP'] >= 300:
        print(Logos_and_Characters['S RANK'])
    print("Marhsall Ohio (NEW)")

    RaidOption = input("[RAID OPTION]>")
    RaidOptionMatch = RaidOption.lower()

    match RaidOptionMatch:
        case "marshall ohio":
            MarshallOHIORaid()

    print("exiting...")


def Raid():
    print(Logos_and_Characters['RAIDS']), print("\nWELCOME TO THE R.A.I.D.S (Rambunctious Anarchy In Different Sizes)")
    print("<-------------------------------------------------------------->"), print("\nRaid"), print("\nShop"), print("\nStats"), print("\nLeave")

    RaidInput = input("|>")
    RaidMatch = RaidInput.lower()

    match RaidMatch:
        case "leave":
            os.system('cls')
        case "raid":
            os.system('cls')
            RaidMenu()
        case "shop":
            os.system('cls')
            RaidShop()
        case "stats":
            os.system('cls')
            RaidShop()