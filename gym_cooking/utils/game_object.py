from collections import defaultdict

from gym_cooking.utils.config import *

OBJ_TO_GOODS_GS = defaultdict(lambda: "Unknown")

OBJ_TO_GOODS_GS.update({
    'FireExtinguisher': 'Fire Extinguisher',
    'Plate': 'Plate',

    'FreshLettuce': 'Fresh Lettuce',
    'FreshOnion': 'Fresh Onion',
    'FreshTomato': 'Fresh Tomato',
    'FreshBellpepper': 'Fresh Bellpepper',

    'ChoppingLettuce': 'Chopping Lettuce',
    'ChoppingOnion': 'Chopping Onion',
    'ChoppingTomato': 'Chopping Tomato',
    'ChoppingBellpepper': 'Chopping Bellpepper',

    'ChoppedLettuce': 'Chopped Lettuce',
    'ChoppedOnion': 'Chopped Onion',
    'ChoppedTomato': 'Chopped Tomato',
    'ChoppedBellpepper' : 'Chopped Bellpepper',

    'ChoppedLettuce-ChoppedOnion': 'L-O Ingredients',
    'ChoppedLettuce-ChoppedTomato': 'L-T Ingredients',
    'ChoppedOnion-ChoppedTomato': 'O-T Ingredients',
    'ChoppedLettuce-ChoppedOnion-ChoppedTomato': 'L-O-T Ingredients',

    'ChoppedBellpepper-ChoppedLettuce' : 'B-L Ingredients',
    'ChoppedBellpepper-ChoppedOnion'   : 'B-O Ingredients',
    'ChoppedBellpepper-ChoppedTomato'  : 'B-T Ingredients',
    'ChoppedBellpepper-ChoppedLettuce-ChoppedOnion' : 'B-L-O Ingredients',
    'ChoppedBellpepper-ChoppedOnion-ChoppedTomato'  : 'B-O-T Ingredients',
    'ChoppedBellpepper-ChoppedLettuce-ChoppedTomato': 'B-L-T Ingredients', 


    'ChoppedLettuce-ChoppedOnion-Plate': 'L-O Ingredients with Plate',
    'ChoppedLettuce-ChoppedTomato-Plate': 'L-T Ingredients with Plate',
    'ChoppedOnion-ChoppedTomato-Plate': 'O-T Ingredients with Plate',
    'ChoppedLettuce-ChoppedOnion-ChoppedTomato-Plate': 'L-O-T Ingredients with Plate',

    'ChoppedBellpepper-ChoppedLettuce-Plate' : 'B-L Ingredients with Plate',
    'ChoppedBellpepper-ChoppedOnion-Plate'   : 'B-O Ingredients with Plate',
    'ChoppedBellpepper-ChoppedTomato-Plate'  : 'B-T Ingredients with Plate',
    'ChoppedBellpepper-ChoppedLettuce-ChoppedOnion-Plate' : 'B-L-O Ingredients with Plate',
    'ChoppedBellpepper-ChoppedOnion-ChoppedTomato-Plate'  : 'B-O-T Ingredients with Plate',
    'ChoppedBellpepper-ChoppedLettuce-ChoppedTomato-Plate': 'B-L-T Ingredients with Plate', 

    'CookedLettuce-CookedOnion-Plate': 'Plated L-O Soup',
    'CookedLettuce-CookedTomato-Plate': 'Plated L-T Soup',
    'CookedOnion-CookedTomato-Plate': 'Plated O-T Soup',
    'CookedLettuce-CookedOnion-CookedTomato-Plate': 'Plated L-O-T Soup',

    'CookedBellpepper-CookedLettuce-Plate' : 'Plated B-L Soup',
    'CookedBellpepper-CookedOnion-Plate'   : 'Plated B-O Soup',
    'CookedBellpepper-CookedTomato-Plate'  : 'Plated B-T Soup',
    'CookedBellpepper-CookedLettuce-CookedOnion-Plate' : 'Plated B-L-O Soup',
    'CookedBellpepper-CookedOnion-CookedTomato-Plate'  : 'Plated B-O-T Soup',
    'CookedBellpepper-CookedLettuce-CookedTomato-Plate': 'Plated B-L-T Soup', 

    'GrillLettuce-GrillOnion-Plate': 'Plated L-O Soup',
    'GrillLettuce-GrillTomato-Plate': 'Plated L-T Soup',
    'GrillOnion-GrillTomato-Plate': 'Plated O-T Soup',
    'GrillLettuce-GrillOnion-GrillTomato-Plate': 'Plated L-O-T Soup',

    'GrillBellpepper-GrillLettuce-Plate' : 'Plated B-L Soup',
    'GrillBellpepper-GrillOnion-Plate'   : 'Plated B-O Soup',
    'GrillBellpepper-GrillTomato-Plate'  : 'Plated B-T Soup',
    'GrillBellpepper-GrillLettuce-GrillOnion-Plate' : 'Plated B-L-O Soup',
    'GrillBellpepper-GrillOnion-GrillTomato-Plate'  : 'Plated B-O-T Soup',
    'GrillBellpepper-GrillLettuce-GrillTomato-Plate': 'Plated B-L-T Soup', 


    'CharredLettuce-CharredOnion-Plate': 'Plated Charred L-O Soup',
    'CharredLettuce-CharredTomato-Plate': 'Plated Charred L-T Soup',
    'CharredOnion-CharredTomato-Plate': 'Plated Charred O-T Soup',
    'CharredLettuce-CharredOnion-CharredTomato-Plate': 'Plated Charred L-O-T Soup',

    'CharredBellpepper-CharredLettuce-Plate' : 'Plated Charred B-L Soup',
    'CharredBellpepper-CharredOnion-Plate'   : 'Plated Charred B-O Soup',
    'CharredBellpepper-CharredTomato-Plate'  : 'Plated Charred B-T Soup',
    'CharredBellpepper-CharredLettuce-CharredOnion-Plate' : 'Plated Charred B-L-O Soup',
    'CharredBellpepper-CharredOnion-CharredTomato-Plate'  : 'Plated Charred B-O-T Soup',
    'CharredBellpepper-CharredLettuce-CharredTomato-Plate': 'Plated Charred B-L-T Soup', 

    'BurnLettuce-BurnOnion-Plate': 'Plated Burn L-O Grill',
    'BurnLettuce-BurnTomato-Plate': 'Plated Burn L-T Grill',
    'BurnOnion-BurnTomato-Plate': 'Plated Burn O-T Grill',
    'BurnLettuce-BurnOnion-BurnTomato-Plate': 'Plated Burn L-O-T Grill',

    'BurnBellpepper-BurnLettuce-Plate' : 'Plated Burn B-L Grill',
    'BurnBellpepper-BurnOnion-Plate'   : 'Plated Burn B-O Grill',
    'BurnBellpepper-BurnTomato-Plate'  : 'Plated Burn B-T Grill',
    'BurnBellpepper-BurnLettuce-BurnOnion-Plate' : 'Plated Burn B-L-O Grill',
    'BurnBellpepper-BurnOnion-BurnTomato-Plate'  : 'Plated Burn B-O-T Grill',
    'BurnBellpepper-BurnLettuce-BurnTomato-Plate': 'Plated Burn B-L-T Grill', 
})

OBJ_TO_GOODS_POT = {
    'CookingLettuce': 'Cooking Lettuce',
    'CookingOnion': 'Cooking Onion',
    'CookingTomato': 'Cooking Tomato',
    'CookingBellpepper': 'Cooking Bellpepper',

    'CookedLettuce': 'Cooked Lettuce',
    'CookedOnion': 'Cooked Onion',
    'CookedTomato': 'Cooked Tomato',
    'CookedBellpepper': 'Cooked Bellpepper',

    'CharredLettuce': 'Charred Lettuce',
    'CharredOnion': 'Charred Onion',
    'CharredTomato': 'Charred Tomato',
    'CharredBellpepper': 'Charred Bellpepper',

    'CharredLettuce-Fire': 'Charred Lettuce',
    'CharredOnion-Fire': 'Charred Onion',
    'CharredTomato-Fire': 'Charred Tomato',
    'CharredBellpepper-Fire': 'Charred Bellpepper',

    'CookingLettuce-CookingOnion': 'L-O Soup',
    'CookingLettuce-CookingTomato': 'L-T Soup',
    'CookingOnion-CookingTomato': 'O-T Soup',
    'CookingBellpepper-CookingOnion': 'B-O Soup',
    'CookingBellpepper-CookingTomato': 'B-T Soup',
    'CookingBellpepper-CookingLettuce': 'B-L Soup',

    'CookingLettuce-CookingOnion-CookingTomato': 'L-O-T Soup',
    'CookingBellpepper-CookingOnion-CookingTomato': 'B-O-T Soup',
    'CookingBellpepper-CookingLettuce-CookingTomato': 'B-L-T Soup',
    'CookingBellpepper-CookingLettuce-CookingOnion': 'B-L-O Soup',

    'CookedLettuce-CookedOnion': 'L-O Soup',
    'CookedLettuce-CookedTomato': 'L-T Soup',
    'CookedOnion-CookedTomato': 'O-T Soup',
    'CookedBellpepper-CookedOnion': 'B-O Soup',
    'CookedBellpepper-CookedTomato': 'B-T Soup',
    'CookedBellpepper-CookedLettuce': 'B-L Soup',

    'CookedLettuce-CookedOnion-CookedTomato': 'L-O-T Soup',
    'CookedBellpepper-CookedOnion-CookedTomato': 'B-O-T Soup',
    'CookedBellpepper-CookedLettuce-CookedTomato': 'B-L-T Soup',
    'CookedBellpepper-CookedLettuce-CookedOnion': 'B-L-O Soup',

    'CharredLettuce-CharredOnion': 'L-O Soup',
    'CharredLettuce-CharredTomato': 'L-T Soup',
    'CharredOnion-CharredTomato': 'O-T Soup',
    'CharredBellpepper-CharredOnion': 'B-O Soup',
    'CharredBellpepper-CharredTomato': 'B-T Soup',
    'CharredBellpepper-CharredLettuce': 'B-L Soup',

    'CharredLettuce-CharredOnion-CharredTomato': 'L-O-T Soup',
    'CharredBellpepper-CharredOnion-CharredTomato': 'B-O-T Soup',
    'CharredBellpepper-CharredLettuce-CharredTomato': 'B-L-T Soup',
    'CharredBellpepper-CharredLettuce-CharredOnion': 'B-L-O Soup',

    'CharredLettuce-CharredOnion-Fire': 'L-O Soup',
    'CharredLettuce-CharredTomato-Fire': 'L-T Soup',
    'CharredOnion-CharredTomato-Fire': 'O-T Soup',
    'CharredBellpepper-CharredOnion-Fire': 'B-O Soup',
    'CharredBellpepper-CharredTomato-Fire': 'B-T Soup',
    'CharredBellpepper-CharredLettuce-Fire': 'B-L Soup',

    'CharredLettuce-CharredOnion-CharredTomato-Fire': 'L-O-T Soup',
    'CharredBellpepper-CharredOnion-CharredTomato-Fire': 'B-O-T Soup',
    'CharredBellpepper-CharredLettuce-CharredTomato-Fire': 'B-L-T Soup',
    'CharredBellpepper-CharredLettuce-CharredOnion-Fire': 'B-L-O Soup',
}

OBJ_TO_GOODS_FRYINGPAN = {
    'CookingLettuce': 'Cooking Lettuce',
    'CookingOnion': 'Cooking Onion',
    'CookingTomato': 'Cooking Tomato',
    'CookingBellpepper': 'Cooking Bellpepper',

    'GrillLettuce': 'Grill Lettuce',
    'GrillOnion': 'Grill Onion',
    'GrillTomato': 'Grill Tomato',
    'GrillBellpepper': 'Grill Bellpepper',

    'BurnLettuce': 'Burn Lettuce',
    'BurnOnion': 'Burn Onion',
    'BurnTomato': 'Burn Tomato',
    'BurnBellpepper': 'Burn Bellpepper',

    'BurnLettuce-Fire': 'Burn Lettuce',
    'BurnOnion-Fire': 'Burn Onion',
    'BurnTomato-Fire': 'Burn Tomato',
    'BurnBellpepper-Fire': 'Burn Bellpepper',

    'CookingLettuce-CookingOnion': 'L-O Grill',
    'CookingLettuce-CookingTomato': 'L-T Grill',
    'CookingOnion-CookingTomato': 'O-T Grill',
    'CookingBellpepper-CookingOnion': 'B-O Grill',
    'CookingBellpepper-CookingTomato': 'B-T Grill',
    'CookingBellpepper-CookingLettuce': 'B-L Grill',

    'CookingLettuce-CookingOnion-CookingTomato': 'L-O-T Grill',
    'CookingBellpepper-CookingOnion-CookingTomato': 'B-O-T Grill',
    'CookingBellpepper-CookingLettuce-CookingTomato': 'B-L-T Grill',
    'CookingBellpepper-CookingLettuce-CookingOnion': 'B-L-O Grill',

    'GrillLettuce-GrillOnion': 'L-O Grill',
    'GrillLettuce-GrillTomato': 'L-T Grill',
    'GrillOnion-GrillTomato': 'O-T Grill',
    'GrillBellpepper-GrillOnion': 'B-O Grill',
    'GrillBellpepper-GrillTomato': 'B-T Grill',
    'GrillBellpepper-GrillLettuce': 'B-L Grill',

    'GrillLettuce-GrillOnion-GrillTomato': 'L-O-T Grill',
    'GrillBellpepper-GrillOnion-GrillTomato': 'B-O-T Grill',
    'GrillBellpepper-GrillLettuce-GrillTomato': 'B-L-T Grill',
    'GrillBellpepper-GrillLettuce-GrillOnion': 'B-L-O Grill',

    'BurnLettuce-BurnOnion': 'L-O Grill',
    'BurnLettuce-BurnTomato': 'L-T Grill',
    'BurnOnion-BurnTomato': 'O-T Grill',
    'BurnBellpepper-BurnOnion': 'B-O Grill',
    'BurnBellpepper-BurnTomato': 'B-T Grill',
    'BurnBellpepper-BurnLettuce': 'B-L Grill',

    'BurnLettuce-BurnOnion-BurnTomato': 'L-O-T Grill',
    'BurnBellpepper-BurnOnion-BurnTomato': 'B-O-T Grill',
    'BurnBellpepper-BurnLettuce-BurnTomato': 'B-L-T Grill',
    'BurnBellpepper-BurnLettuce-BurnOnion': 'B-L-O Grill',

    'BurnLettuce-BurnOnion-Fire': 'L-O Grill',
    'BurnLettuce-BurnTomato-Fire': 'L-T Grill',
    'BurnOnion-BurnTomato-Fire': 'O-T Grill',
    'BurnBellpepper-BurnOnion-Fire': 'B-O Grill',
    'BurnBellpepper-BurnTomato-Fire': 'B-T Grill',
    'BurnBellpepper-BurnLettuce-Fire': 'B-L Grill',

    'BurnLettuce-BurnOnion-BurnTomato-Fire': 'L-O-T Grill',
    'BurnBellpepper-BurnOnion-BurnTomato-Fire': 'B-O-T Grill',
    'BurnBellpepper-BurnLettuce-BurnTomato-Fire': 'B-L-T Grill',
    'BurnBellpepper-BurnLettuce-BurnOnion-Fire': 'B-L-O Grill',
}

ALL_FRESH_FOOD = ['Tomato', 'Lettuce', 'Onion','Bellpepper']
ALL_ASSEMBLE = ['L-O Ingredients', 'L-T Ingredients', 'O-T Ingredients', 
                'B-L Ingredients', 'B-O Ingredients', 'B-T Ingredients',
                'L-O-T Ingredients','B-L-O Ingredients','B-O-T Ingredients','B-L-T Ingredients']

ALL_SOUP = ['L-O Soup', 'L-T Soup', 'O-T Soup', 
            'B-L Soup', 'B-O Soup', 'B-T Soup',
            'L-O-T Soup','B-L-O Soup','B-O-T Soup','B-L-T Soup',]

ALL_GRILL = ['L-O Grill', 'L-T Grill', 'O-T Grill', 
            'B-L Grill', 'B-O Grill', 'B-T Grill',
            'L-O-T Grill','B-L-O Grill','B-O-T Grill','B-L-T Grill',]


GOODS_TO_OBJ_GS = defaultdict(lambda: "Unknown")
GOODS_TO_OBJ_GS.update({v: k for k, v in OBJ_TO_GOODS_GS.items()})
GOODS_TO_OBJ_GS.update({
    "L-O Soup": "CookedLettuce-CookedOnion",
    "L-T Soup": "CookedLettuce-CookedTomato",
    "O-T Soup": "CookedOnion-CookedTomato",
    "B-O Soup": "CookedBellpepper-CookedOnion",
    "B-T Soup": "CookedBellpepper-CookedTomato" ,
    "B-L Soup": "CookedBellpepper-CookedLettuce",

    "L-O-T Soup": "CookedLettuce-CookedOnion-CookedTomato",
    "B-O-T Soup": "CookedBellpepper-CookedOnion-CookedTomato",
    "B-L-T Soup": "CookedBellpepper-CookedLettuce-CookedTomato",
    "B-L-O Soup": "CookedBellpepper-CookedLettuce-CookedOnion",
})

GOODS_TO_OBJ_GS.update({
    "L-O Grill": "GrillLettuce-GrillOnion",
    "L-T Grill": "GrillLettuce-GrillTomato",
    "O-T Grill": "GrillOnion-GrillTomato",
    "B-O Grill": "GrillBellpepper-GrillOnion",
    "B-T Grill": "GrillBellpepper-GrillTomato" ,
    "B-L Grill": "GrillBellpepper-GrillLettuce",

    "L-O-T Grill": "GrillLettuce-GrillOnion-GrillTomato",
    "B-O-T Grill": "GrillBellpepper-GrillOnion-GrillTomato",
    "B-L-T Grill": "GrillBellpepper-GrillLettuce-GrillTomato",
    "B-L-O Grill": "GrillBellpepper-GrillLettuce-GrillOnion",
})


HT_MAP = {
    'Chop': 'Chop',
    'Assemble': 'Prepare',
    'Cook': 'Cook',
    'Grill' : 'Grill',
    'Putout': 'Putout',
    'Pick': 'Plate',
    'Serve': 'Serve',
    'Drop': 'Drop',
    'Leave': 'Leave',
}

#T O L 
STANDARD_MAP = defaultdict(lambda: "Unknown")
STANDARD_MAP.update({
    "assemble": ["L-O Ingredients", "L-T Ingredients", "O-T Ingredients", "L-O-T Ingredients"],
    "dish" : [ "L-O Soup", "L-T Soup", "O-T Grill", "L-O Grill",
              "L-O-T Soup", "L-O-T Grill"],
})

#T L B
CONCAVE_MAP= defaultdict(lambda: "Unknown")
CONCAVE_MAP.update({
    "assemble": ["B-L Ingredients", "B-T Ingredients", "L-T Ingredients", "B-L-T Ingredients"],
    "dish" : [ "B-L Soup", "B-T Soup", "L-T Soup", "B-L-T Soup"],
})

#B L O
PARTITION_MAP = defaultdict(lambda: "Unknown")  
PARTITION_MAP.update({
    "assemble": ["B-L Ingredients", "B-O Ingredients", "L-O Ingredients", "B-L-O Ingredients"],
    "dish" : [ "B-L Grill", "B-O Grill", "L-O Grill", "B-L-O Grill"],
})

#B L O T
DIFFICULT_MAP = defaultdict(lambda: "Unknown")
DIFFICULT_MAP.update({
    "assemble": ALL_ASSEMBLE,
    "dish" : ["B-O Soup", "L-T Soup", 
              "O-T Grill", "B-L Grill",
              "L-O-T Soup", "B-O-L Grill"],
})
