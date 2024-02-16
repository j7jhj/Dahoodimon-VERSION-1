import time


Guns = {
  'tyrones last shot': {
      'Name': 'Tyrones Last Shot',
      'Damage': 30,
      'Critical Damage': 60,
      'Rarity': 'Boss Loot',
      'Owned': False,
      'Equipped': False
  },
  'amongus gun': {
      'Name': 'Amongus Gun',
      'Damage': 40,
      'Critical Damage': 30,
      'Rarity': 'Low Tier Crap',
      'Owned': True,
      'Equipped': True
  },
  "tech supports wrath": {
      'Name': "Tech Support's Wrath",
      'Damage': 70,
      'Critical Damage': 80,
      'Rarity': "Boss Loot",
      'Owned': False,
      'Equipped': False
  },  
  "the fat man": {
      'Name': "The Fat Man",
      'Damage': 120,
      'Critical Damage': 130,
      'Rarity': "Boss Loot",
      'Owned': False,
      'Equipped': False
  },
  "willys steampunk cannon": {
      'Name': "Willy's Steampunk Cannon",
      'Damage': 200,
      'Critical Damage': 250,
      'Rarity': "Boss Loot",
      'Owned': False,
      'Equipped': False
  },
  "detroit fusion strike": {
      'Name': 'Detroit Fusion Strike',
      'Damage': 50,
      'Critical Damage': 100,
      'Rarity': "FUSION EXCLUSIVE",
      'Owned': False,
      'Equipped': False
  }
}

techniques = {
    'grenade throw': {
        'Name': "Grenade",
        'Damage': 80,
        'Buff': 30,
        'Amount Owned': 0
    },
    'fusion': {
        'Name': "Fusion",
        'HP Buff': 90,
        'Damage Buff': 30,
        'Amount Owned': 0,
    },
    'health blessing': {
        'Name': "Health Blessing",
        'HP Buff': 60,
        'Amount Owned': 0,
    },
}

TechniqueKeys = {
    'Fusion Key': False
}

Currency = {
    'Money': 120,
    'HP': 100,
    'ArtilleryModeCurrency': {
        'MP': 100,
        'ArtilleryHP': 500
    }
}

Food = {
    'the last beery': {
        "Name": "The Last Beery",
        "HP Increase": 30,
        "Amount Owned": 0
    },
    'fnaf lore drop': {
        "Name": "FNAF Lore Drop",
        "HP Increase": 20,
        "Amount Owned": 0
    },
    'thats just a beery, a game beery': {
        "Name": "Thats Just A BEERY, A GAME BEERY!",
        "HP Increase": 80,
        "Amount Owned": 0
    },
    'jamanut the donut': {
        'Name': 'Jamanut The Donut',
        "HP Increase": 35,
        "Amount Owned": 0
    },
    'johannes the cookie': {
        'Name': 'Johannes The Cookie',
        "HP Increase": 20,
        "Amount Owned": 0
    },
    'the wild wolf': {
        'Name': 'The Wild Wolf',
        "HP Increase": 60,
        "Amount Owned": 0
    },
    'da hood is real': {
        'Name': 'Da Hood Is Real',
        "HP Increase": 45,
        "Amount Owned": 0
    },
    'spiked chocolate milk': {
        'Name': 'Spiked Chocolate Milk',
        "HP Increase": 30,
        "Amount Owned": 0
    },
    'made with love': {
        'Name': 'Made With Love',
        "HP Increase": 50,
        "Amount Owned": 0
    },
    'i stole your gf': {
        'Name': 'I Stole Your Gf',
        "HP Increase": 45,
        "Amount Owned": 0
    },

}

FUSION = {
    'HP': 400,
    'EN': 100,
    'Godlike Rizz':{
        'DMG': 60,
        'EN CONSUMPTION': 30
    },
    'Detroit Fusion Strike':{
        'DMG': 100,
        'EN CONSUMPTION': 60
    },
    'Godlike Recharge': 40,
    'Owned': False

}

ItemsList = [Guns['amongus gun']]


Equipped_Weapon = []
