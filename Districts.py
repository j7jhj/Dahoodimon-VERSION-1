from Items_List import Guns
from Gang_Members import Enemies
import os 
import random
import time

from Items_List import ItemsList
from Items_List import Food
from Characters import Frames
from Characters import Logos_and_Characters
from Items_List import Currency
from Items_List import FUSION
from Items_List import TechniqueKeys

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


        Currency['HP'] += 90
        Enemies[FusionTarget]['HP'] -= 90

        if FusionTarget == "Tyrone" and Enemies['Tyrone']['HP'] <= 0:
            os.system('cls')
            print(Logos_and_Characters['Hole In One Tyrone']), '\n', print(Logos_and_Characters['Super Finish'])
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



    else: 
        print("You missed")
        time.sleep(1)



def District_Three():
    "District Three"

    District_Three_LOOP = True
    FUSION_District_Three_Loop = False


    def FUSIONOptions():

        os.system('cls')
        print("\nFUSION MOVES"), '\n', print("<-------------------------------------------------->")
        print("\nGodlike Rizz | 60 DMG | -30 EN"), '\n', print("Detroit Fusion Strike | 100 DMG | - 50 EN"), '\n', print("Godlike Recharge | + 40 EN")

        FUSIONTechniqueOption = input("[FUSION TECHNIQUE]>")
        FusionTechniqueMatch = FUSIONTechniqueOption.lower()

        match FusionTechniqueMatch:
            case "godlike rizz" if FUSION['EN'] >= 30:
                print(f"You used GODLIKE RIZZ and dealed 60 DMG")
                 
                Enemies['Steampunk Tyrone']['HP'] -= FUSION['Godlike Rizz']['DMG']
                FUSION['EN'] -= FUSION['Godlike Rizz']['EN CONSUMPTION']

                time.sleep(1)

            case "detroit fusion strke" if FUSION['EN'] >= 50:
                print(f"You used Detroit Fusion Strike and dealed 100 DMG")

                Enemies['Steampunk Tyrone']['HP'] -= FUSION['Detroit Fusion Strike']['DMG']
                FUSION['EN'] -= FUSION['Detroit Fusion Strike']['EN CONSUMPTION']
                
                time.sleep(1)

            case "godlike recharge":
                print(f"You used Godlike Recharge and recharged {FUSION['Godlike Recharge']} EN")
                FUSION['EN'] += FUSION['Godlike Recharge']

                time.sleep(1)
                


    def District_Three_Attack():
        MissChance = random.randint(1,4)
        for i in ItemsList:
            print(i)

        print("\nSelect what you want to attack with")

        AttackInput = input('[ATTACK]>')
        AttackFChoice = Guns.get(AttackInput.lower())

        if AttackFChoice is not None and AttackFChoice['Equipped'] and MissChance <= 3:
            print("You chose", AttackFChoice['Name'], 'and dealed', AttackFChoice['Damage'], 'damage!')
            Enemies['Steampunk Willie']['HP'] -= AttackFChoice['Damage']
            time.sleep(2)

            if MissChance == 1:
                print("You chose", AttackFChoice['Name'], 'and dealed', AttackFChoice['Critical Damage'], 'CRITICAL damage!')
                Enemies['Steampunk Willie']['HP'] -= AttackFChoice['Critical Damage']
                time.sleep(2)


    def Steampunk_Willie__Attack_Menu():
        """Battle Menu"""
        os.system('cls') 


        print(Logos_and_Characters['SteamPunk Willie']), '\n', print(Enemies['Steampunk Willie']['Name']), '\n', print(f"ENEMY HP:", Enemies['Steampunk Willie']['HP'])
        print("\nYOUR HP:", Currency['HP']), '\n', print("<-------------------------------------------------------------->")
        print("\nAttack"), '\n', print("Food")

        Doomsday_Hong_Attack_Menu = random.randint(1,4)
        if Doomsday_Hong_Attack_Menu <= 3 and Currency['HP'] <= 100:
            print("Steampunk Willie dealed", Enemies['Steampunk Willie']['dmg'], 'damage!')
            Currency['HP'] -= Enemies['Steampunk Willie']['dmg']
        else:
            print("Steampunk Willie missed!")

    
        OptionInput = input("|>")
        if OptionInput.lower() == ('food'):
            food_search()
        elif OptionInput.lower() == ('attack'):
            District_Three_Attack()
    

    def FUSIONMonologue():
        os.system('cls')
        printt("Steampunk Willie: You two will be defeated by me and Tyrone!", 0.07), '\n', printt("Tyrone: Lets charge. FULL POWER!", 0.07)
        time.sleep(2)
        os.system('cls')

        printt("\nYou: Your reign of rizz is almost over, Tyrone!", 0.07), '\n', printt("Doomsday Hong: When we fuse, you and your empire will fall!", 0.07)
        time.sleep(2)
        os.system('cls')

        printt("\nYou/Doomsday Hong: PUBLIC DOMAIN EXPANSION: INFINITE FUSION!", 0.07)
        time.sleep(1)
        os.system('cls')

    def EndMonologue():
        os.system('cls')
        printt("You: Its the end FOR YOU. RIZZLER BOMB CANNON!", 0.07), '\n', printt("Steampunk Tyrone: THIS IS NOT THE END! YOUR COUSIN WILL DEFEAT YOU", 0.07)
        time.sleep(2)
        os.system('cls')

        printt("\nDoomsday Hong: We defeated them!", 0.07), '\n', printt("You: We are now one step closer to defeating my cousin!", 0.07)
        time.sleep(1)
        os.system('cls')



    def Fusion_Stage():
        """FUSION Battle"""
        os.system('cls') 


        print(Logos_and_Characters['Steampunk Tyrone']), '\n', print(Enemies['Steampunk Tyrone']['Name']), '\n', print(f"ENEMY HP:", Enemies['Steampunk Tyrone']['HP'])
        print("\nYOUR HP:", FUSION['HP']), '\n',print("EN:",FUSION['EN']), '\n', print("<-------------------------------------------------------------->")
        print("Fusion Attack")

        Steampunk_Tyrone_chance = random.randint(1,4)
        if Steampunk_Tyrone_chance <= 3:
            print("Steampunk Tyrone dealed", Enemies['Steampunk Tyrone']['dmg'], 'damage!')
            FUSION['HP'] -= Enemies['Steampunk Tyrone']['dmg']
        else:
            print("Steampunk Tyrone missed!")

    
        OptionInput = input("|>")

        SteamPunk_battle_match = OptionInput.lower()

        match SteamPunk_battle_match:
            case "fusion attack":
                FUSIONOptions()



    while District_Three_LOOP == True:

        if Enemies['Steampunk Willie']['HP'] <= 0:

            FUSIONMonologue()
            District_Three_LOOP = False
            FUSION_District_Three_Loop = True
            
            break

        if Currency['HP'] <= 0 and Enemies['Steampunk Willie']['HP'] >= 500:

            print("You were defeated by Steampunk Willie.")

            Currency['HP'] = 100
            Enemies['Steampunk Tyrone']['HP'] == 700

            time.sleep(2)
            break

        
        Steampunk_Willie__Attack_Menu()

    while FUSION_District_Three_Loop == True:

        District_Three_Reward = random.randint(1,10)

        if Enemies['Steampunk Tyrone']['HP'] <= 0 and District_Three_Reward <= 9:

            EndMonologue()
            print("You defeated Steampunk Tyrone and recieved Willie's Steampunk Cannon")

            Guns['willys steampunk cannon']['Owned'] = True
            ItemsList.append(Guns['willys steampunk cannon'])

            Enemies['Steampunk Tyrone']['HP'] = 700
            Enemies['Steampunk Willie']['HP'] = 500

            time.sleep(2)

            break

        elif Enemies['Steampunk Tyrone']['HP'] <= 0 and District_Three_Reward == 10:
            EndMonologue()
            print("You defeated Steampunk Tyrone and recieved the FUSION KEY!")

            Enemies['Steampunk Tyrone']['HP'] = 700
            Enemies['Steampunk Willie']['HP'] = 500
            FUSION['HP'] = 400
            FUSION['EN'] = 100
            TechniqueKeys['Fusion Key'] = True

            ItemsList.append(TechniqueKeys['FusionKey'])

            time.sleep(1)
            break

        elif FUSION['HP'] <= 0:

            print("You were defeated by Steampunk Tyrone.")

            Currency['HP'] = 100
            FUSION['HP'] = 400
            FUSION['EN'] = 100
            Enemies['Steampunk Tyrone']['HP'] = 700

            time.sleep(2)

            break

        Fusion_Stage()

        time.sleep(1)



def District_Two():
    District_Two_LOOP = True

    global FusionTarget
    FusionTarget = "Doomsday Hong"

    """District Two"""
    def DISTRICT2MONOOLOGUE():
        os.system('cls')
        printt("You: Its over. My rizz is just stronger than yours.", 0.07), '\n', printt("Doomsday Hong: Wait spare me! I will join you to stop Tyrone and Willie!", 0.07)
        time.sleep(1)
        os.system('cls')
        printt("You: Fine. We must learn the fusing technique before they do", 0.07), '\n', printt("Doomsday Hong: Okay.", 0.07)
        time.sleep(1)
        os.system('cls')
    


    def District_Two_Attack():
        MissChance = random.randint(1,4)
        for i in ItemsList:
            print(i)

        print("\nSelect what you want to attack with")

        AttackInput = input('[ATTACK]>')
        AttackFChoice = Guns.get(AttackInput.lower())

        if AttackFChoice is not None and AttackFChoice['Equipped'] == True and MissChance <= 3:
            print("You chose", AttackFChoice['Name'], 'and dealed', AttackFChoice['Damage'], 'damage!')
            Enemies['Doomsday Hong']['HP'] -= AttackFChoice['Damage']
            time.sleep(2)

            if MissChance == 1:
                print("You chose", AttackFChoice['Name'], 'and dealed', AttackFChoice['Critical Damage'], 'CRITICAL damage!')
                Enemies['Doomsday Hong']['HP'] -= AttackFChoice['Critical Damage']
                time.sleep(2)


    def Doomsday_Hong_Attack_Menu():
        """Battle Menu"""
        os.system('cls')

        print(Logos_and_Characters['Doomsday Hong']), '\n', print(Enemies['Doomsday Hong']['Name']), '\n', print(f"ENEMY HP:", Enemies['Doomsday Hong']['HP'])
        print("\nYOUR HP:", Currency['HP']), '\n', print("<-------------------------------------------------------------->")

        if Currency['HP'] < 40 and FUSION['Owned'] == True and FusionUse == 0:
            print("FUSION IS AVAILABLE!")

        print("\nAttack"), '\n', print("Food")

        Doomsday_Hong_Attack_Menu = random.randint(1,4)
        if Doomsday_Hong_Attack_Menu <= 3:
            print("Doomsday Hong dealed", Enemies['Doomsday Hong']['dmg'], 'damage!')
            Currency['HP'] -= Enemies['Doomsday Hong']['dmg']
        else:
            print("Doomsday Hong missed!")

    
        OptionInput = input("|>")

        DistrictTwoMatch = OptionInput.lower()

        match DistrictTwoMatch:
            case 'food':
                food_search()
            case 'attack':
                District_Two_Attack()
            case 'fusion' if Currency['HP'] < 40 and FUSION['Owned'] == True and FusionUse == 0:
                FUSIONATTACK()



    while District_Two_LOOP == True:

        if Enemies['Doomsday Hong']['HP'] <= 0:
            DISTRICT2MONOOLOGUE()
            loot_chance = random.randint(0,10)

            if loot_chance == 10:
                print("\nYou recieved the 'The Fat Man' Weapon!")

                Guns['the fat man']['Owned'] == True
                ItemsList.append(Guns['the fat man'])   

                Currency['HP'] = 100
                Enemies['Doomsday Hong']['HP'] = 500
                FusionTarget = ""

                Guns['detroit fusion strike']['Owned'] = False
                ItemsList.remove(Guns['detroit fusion strike'])
                Guns['detroit fusion strike']['Equipped'] = False
                FusionUse == 0

                time.sleep(2)

                break

            else: 
            
                Currency['Money'] += 90
                print("You defeated Doomsday Hong and recieved 90 money")
                
                Currency['HP'] = 100
                Enemies['Doomsday Hong']['HP'] = 500
                FusionTarget = ""

                Guns['detroit fusion strike']['Owned'] = False
                ItemsList.remove(Guns['detroit fusion strike'])
                Guns['detroit fusion strike']['Equipped'] = False
                FusionUse == 0

                time.sleep(2)

                break
            
        if Currency['HP'] <= 0:

            print("You were defeated by Doomsday Hong.")

            Currency['HP'] = 100
            Enemies['Doomsday Hong']['HP'] = 500
            FusionTarget = ""

            Guns['detroit fusion strike']['Owned'] = False
            ItemsList.remove(Guns['detroit fusion strike'])
            Guns['detroit fusion strike']['Equipped'] = False
            FusionUse == 0

            time.sleep(2)

            break

        Doomsday_Hong_Attack_Menu()




def District_One():
    District_One_LOOP = True
    global FusionTarget

    FusionTarget = "Tyrone"

    """District One"""

    def DISTRICT1MONOOLOGUE():
        os.system('cls')
        printt("You: You are my first victim. Any last words?", 0.07), '\n', printt("Tyler: NO. I am Willie's right hand man. I will not lose", 0.07)
        time.sleep(1)
        os.system('cls')
        printt("Tyler: The next time I see you. Me and Willie will use fusion. *Disappears* ", 0.07), '\n', printt("You: Crap. I must also learn the technique. But with who?", 0.07)
        time.sleep(1)
        os.system('cls')



    def District_One_Attack():
        MissChance = random.randint(1,4)
        for i in ItemsList:
            print(i)

        print("\nSelect what you want to attack with")

        AttackInput = input('[ATTACK]>')
        AttackFChoice = Guns.get(AttackInput.lower())

        if AttackFChoice is not None and AttackFChoice['Equipped'] == True and MissChance <= 3:
            print("You chose", AttackFChoice['Name'], 'and dealed', AttackFChoice['Damage'], 'damage!')
            Enemies['Tyrone']['HP'] -= AttackFChoice['Damage']
            time.sleep(2)

            if MissChance == 1:
                print("You chose", AttackFChoice['Name'], 'and dealed', AttackFChoice['Critical Damage'], 'CRITICAL damage!')
                Enemies['Tyrone']['HP'] -= AttackFChoice['Critical Damage']
                time.sleep(2)



    def Trevor_Attack_Menu():
        """Battle Menu"""
        os.system('cls') 



        print(Logos_and_Characters['Tyrone']), '\n', print(Enemies['Tyrone']['Name']), '\n', print(f"ENEMY HP:", Enemies['Tyrone']['HP'])
        print("\nYOUR HP:", Currency['HP']), '\n', print("<-------------------------------------------------------------->")

        if Currency['HP'] < 40 and FUSION['Owned'] == True and FusionUse == 0:
            print("FUSION IS AVAILABLE!")

        print("\nAttack"), '\n', print("Food")

        TrevorChance = random.randint(1,4)
        if TrevorChance <= 3:
            print("Tyrone dealed", Enemies['Tyrone']['dmg'], 'damage!')
            Currency['HP'] -= Enemies['Tyrone']['dmg']
        else:
            print("Tyrone missed!")
    
        OptionInput = input("|>")
        DistrictOneMatch = OptionInput.lower()

        match DistrictOneMatch:
            case 'food':
                food_search()
            case 'attack':
                District_One_Attack()
            case 'fusion' if Currency['HP'] < 40 and FUSION['Owned'] == True and FusionUse == 0:
                FUSIONATTACK()
          
        


    while District_One_LOOP == True:
        if Enemies['Tyrone']['HP'] <= 0:
            loot_chance = random.randint(0,10)

            if loot_chance == 10:

                DISTRICT1MONOOLOGUE()

                print("\nYou recieved the 'Tyrones Last Shot' Weapon!")

                Guns['tyrones last shot']['Owned'] == True
                ItemsList.append(Guns['tyrones last shot'])   

                Currency['HP'] = 100
                Enemies['Tyrone']['HP'] = 200
                FusionTarget = ""

                Guns['detroit fusion strike']['Owned'] = False
                ItemsList.remove(Guns['detroit fusion strike'])
                Guns['detroit fusion strike']['Equipped'] = False
                FusionUse == 0

                time.sleep(2)

                break
            else: 
                DISTRICT1MONOOLOGUE()

                Currency['Money'] += 40
                print("You defeated Tyrone and recieved 40 money")
                
                Currency['HP'] = 100
                Enemies['Tyrone']['HP'] = 200

                Guns['detroit fusion strike']['Owned'] = False
                ItemsList.remove(Guns['detroit fusion strike'])
                Guns['detroit fusion strike']['Equipped'] = False
                FusionUse == 0

                FusionTarget = ""

                time.sleep(2)

                break
            
        if Currency['HP'] <= 0:

            print("You were defeated by Tyrone.")

            Currency['HP'] = 100
            Enemies['Tyrone']['HP'] = 200          
            FusionTarget = ""

            Guns['detroit fusion strike']['Owned'] = False
            ItemsList.remove(Guns['detroit fusion strike'])
            Guns['detroit fusion strike']['Equipped'] = False
            FusionUse == 0

            time.sleep(2)

            break

        Trevor_Attack_Menu()


