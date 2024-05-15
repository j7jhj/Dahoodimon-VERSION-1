from Items_List import TechniqueKeys
from Characters import Logos_and_Characters
from Items_List import Currency
from Characters import FusionFrames
import os
from Characters import DodgeFrames
from Items_List import WeaveState
from Items_List import FUSION
from Gang_Members import Enemies
import time

FusionTarget = "Puppet Tyrone"


def printt(string, strDelay):
  for i in str(string + "\n"):
    print(i, end="", flush=True)
    time.sleep(strDelay)

def Weave_State_Technique():
    def Weave_State_Training():

        os.system('cls')
        printt("When you active your weave state ability, you have the ability to dodge attacks randomly. After dodging 3 times, you will be able to unlock the super attack", 0.07)
        time.sleep(1)
        printt('However, after using the super attack, you will no longer be able to use the weave statefor the remainder of the battle!', 0.07)
        time.sleep(1)
        printt("You will also have access to the power up ability that gives up extra hp after falling below 50 hp! Im going to attack you and see if you dodge it!", 0.07)
        time.sleep(1)

        print("Trainer attacked you!")
        time.sleep(1)
        
        for i in range(0, len(DodgeFrames)):
            print(DodgeFrames[i]), time.sleep(0.5), os.system('cls')
        
        print("Great! You should know the basics of the weave state by now! Good luck!")

        TechniqueKeys['Weave State Key'] == False
        WeaveState['Owned'] == True

        time.sleep(2)
        os.system('cls')

    if TechniqueKeys['Weave State Key'] == True:
        Weave_State_Training()
    else:
        print("You dont have a weave state key")
        time.sleep(1)
        os.system('cls')

def Fusion_Technique():
    def FusionTraining():
        
        FusionTrainingLoop = True
        os.system('cls')

        printt("When you reach below 40 HP, you can be able to fuse.", 0.07), '\n', printt("Fusion will grant you more HP and use a special ability to damage the opponent", 0.07)
        time.sleep(1)

        os.system('cls')
        printt("Lets try it. I dealed 70 dmg and you only have 30 HP now. Type 'FUSION' to use it!", 0.07)
        time.sleep(1)

        os.system('cls')

        while FusionTrainingLoop == True:
            Currency['HP'] = 20

            print(Logos_and_Characters['Puppet Tyrone']), '\n', print("ENEMY HP:", Enemies['Puppet Tyrone']['HP'])

            print("YOUR HP:", Currency['HP'])

            FusionInput = input("|>")
            if FusionInput.lower() == ("fusion"):
                os.system('cls')
                printt("You/Doomsday Hong: PUBLIC DOMAIN EXPANSION: INFINITE FUSION! GODLIKE RIZZ!", 0.07)

                time.sleep(1)
                print("\n"), print(Logos_and_Characters['Fusion'])
                time.sleep(2)
                os.system('cls')

                for i in range(0, len(FusionFrames)):
                    print(FusionFrames[i]), time.sleep(2), os.system('cls')
                
                time.sleep(2)

                Currency['HP'] += 70
                Enemies[FusionTarget]['HP'] -= 60

                time.sleep(1)

            else:
                print("Typed wrong")

            if Enemies['Puppet Tyrone']['HP'] == 0:
                
                print("Dealed 60 DMG to PUPPET TYRONE!"), '\n', print("You defeated PUPPET TYRONE!")
                time.sleep(2)

                os.system('cls')
                printt("Congrats! You defeated someone with the FUSION technique! Remember, its like a final trump card ability!", 0.07)

                Enemies['Puppet Tyrone']['HP'] = 60
                Currency['HP'] = 100

                FUSION['Owned'] = True

                time.sleep(1)
                break

    os.system('cls')
  
    print(Logos_and_Characters['Techniques']), '\n', print("<-------------------------------------------------->")
    print("\nFusion"), '\n', print("Back")

    TechniqueInput = input("|>")

    TechniqueMatch = TechniqueInput.lower()

    match TechniqueMatch:
        case "fusion" if TechniqueKeys['Fusion Key'] == True:
            FusionTraining()
        case "back": 
            os.system('clear')
    
    if TechniqueKeys['Fusion Key'] == False:
        print("You do not have the key")
        time.sleep(1)


