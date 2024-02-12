# File Imports
from Technique_Training import Fusion_Technique
from Items_List import Currency
from Characters import Logos_and_Characters
from Items_List import Guns
from Detroit_Map import District_One
from Items_List import ItemsList
from Restaurants import The_Game_Beery
from Restaurants import Jamals
from Restaurants import DahoodlinHut
from Items_List import Equipped_Weapon
from Detroit_Map import District_Two
from Detroit_Map import District_Three


# Other Modules
import json
import time
import os



# Pls dont cancel me also these are the values/lists
GameLoop = True
menu = True
play = False
Credits = False
Enemies = 0
Equipped_Weapon = "Placeholder"



print("Saved!")



# Clear function
def clear():
  os.system('cls')



def Save():
  with open('save_file', 'w') as savefile:
    json.dump(ItemsList, savefile)

  with open('save_Currency_file', 'w') as saveCfile:
    json.dump(Currency['Money'], saveCfile)

  print("SAVED!")

def load():
  global ItemsList
  with open('save_file','r') as savefile:
    ItemsList = json.load(savefile)
  with open('save_Currency_file', 'w') as saveCfile:
    Currency['Money'] = json.load(saveCfile)
  print("Loaded data!")



# District One, Two, and three Functions
def District_One_Option():

    os.system('cls')
    print(Logos_and_Characters['District One']), '\n', print("<-------------------------------------------------->")
    print("raid"), '\n', print("leave")

    station1_option = input("|>")

    if station1_option.lower() == ('raid'):
        District_One()

    if station1_option.lower() == ('leave'):
        os.system('cls')



def District_Two_Option():

    os.system('cls')
    print(Logos_and_Characters['District Two']), '\n', print("<-------------------------------------------------->")
    print("raid"), '\n', print("leave")

    station2_option = input("|>")

    if station2_option.lower() == ('raid'):
        District_Two()

    if station2_option.lower() == ('leave'):
        os.system('cls')


def District_Three_Option():

    os.system('cls')
    print(Logos_and_Characters['District Three']), '\n', print("<-------------------------------------------------->")
    print("raid"), '\n', print("leave")

    station3_option = input("|>")

    if station3_option.lower() == ('raid'):
        District_Three()

    if station3_option.lower() == ('leave'):
        os.system('cls')


# Menu For Detroit
def Goofy_ah_Menu():
  clear()

  print(Logos_and_Characters['Detroit']), '\n', print("<-------------------------------------------------->")
  print("Travel"), '\n', print("Inventory"), '\n', print("Menu"), '\n', print("Save")


# Save Function
def SAVE():
  clear()
  play == False
  print(Logos_and_Characters['Save']), '\n', print("<-------------------------------------------------->")
  print("\nsave"), '\n', print('load'), '\n', print("back")

  SAVEInput = input("|>")
  if SAVEInput.lower() == ('save'):
    Save()
    time.sleep(1)
  elif SAVEInput.lower() == ('load'):
    load()
    time.sleep(1)
  elif SAVEInput.lower() == ('back'):
    clear()
    play == True



# inventory function
def Inventory():

  clear()
  """Inventory Function. (Kinda) works"""
  global play
  play = False
  print(Logos_and_Characters['Inventory']), '\n', print("<-------------------------------------------------->")
  print("Cash:"),print(Currency['Money'])

  for items in ItemsList:
    print(f"\n-> {items}")
  
  print("\n Equip | Type 'back' to return to game menu")

  InventoryOption = input("|>")

  InventoryCase = InventoryOption.lower()

  match InventoryCase:
    case "equip":

      global Equipped_Weapon
      AmountEquipped = 0

      print("\nSelect what you want to equip")

      EquipInput = input('[EQUIP]>')
      GunEquip = Guns.get(EquipInput.lower())

      if GunEquip is not None and GunEquip['Owned'] == True and AmountEquipped <= 3:

        GunEquip['Equipped'] = True
        print("\nEquipped", GunEquip['Name'])
        AmountEquipped = AmountEquipped + 1

        time.sleep(2)
      else:
        print("Typed wrong/or dont have enough space")
        time.sleep(2)


    case "back":
      play = True

      clear()

  clear()
  play = True

      

# Travel function
def traveling():
  """Travelling guide"""

  global play

  clear()
  play = False
  print(Logos_and_Characters['Travel']), '\n', print("<-------------------------------------------------->")
  print("\n<-------------- DISTRICTS -------------->"), '\n', print("District One"), '\n', print("District Two"), '\n', print("District Three")
  print("\n<-------------- Food/Items -------------->"), '\n', print("The Game Beery"), '\n', print("Jamals"), '\n', print("Dahoodlin Hut")
  print("\n<-------------- Other -------------->"), '\n',print("Technique Training"),'\n', print("Back")

  traveloption = input("|>")

  TravelOptions = traveloption.lower()

  match TravelOptions:
    case "district one":
      District_One_Option()

    case "district two":
      District_Two_Option()

    case "district three":
      District_Three_Option()

    case "the game beery":
      clear()
      The_Game_Beery()

    case "jamals":
      clear()
      Jamals()

    case "dahoodlin hut":
      clear()
      DahoodlinHut()

    case "technique training":
      Fusion_Technique()

    case "back":
      clear()
      play = True

  clear()
  play = True



#Game loop
while GameLoop:

  while menu == True:
    """Menu screen"""
    print(Logos_and_Characters['MainLogo'])
    print("<-------------------------------------------------------------->")
    print("PLAY"), '\n', print("Credits"), '\n', print("Quit")
    print("<-------------------------------------------------------------->")

    option = input("|> ")

    OptionTypes  = option.lower()

    match OptionTypes:
      case "play":
        play = True
        menu = False

      case "credits":
        Credits = True
        menu = False

      case "quit":
        quit()

    clear()


  # Credits loop
  while Credits == True:

    """Hall Of Shame: The Dahoodimon Developers (ULTRAKILL REFERENCE!) """
    clear()
    print(Logos_and_Characters['Credits'])
    print("\nj7jhj - the god of Gen Alpha (aka the developer)")
    print("\n\t-- THE LIST --"), '\n', print("Arth - Ideas"), '\n', print("MrMix - Ideas")
    print("\ntype 'menu' to return to the menu")

    creditoption = input("|> ")


    if creditoption.lower() == ('menu'):
      clear()
      menu = True
      Credits = False


  # Play Loop
  while play == True:

    """The while loop for the entire game! May the brainrot begin"""

    Goofy_ah_Menu()
    MenuInput = input("|>")

    MenuOptions = MenuInput.lower()

    match MenuOptions:
      case "inventory":
        Inventory()
      case "travel":
        traveling()
      case "save":
        SAVE()
      case "menu":
        play = False
        menu = True
        clear()

    clear()
