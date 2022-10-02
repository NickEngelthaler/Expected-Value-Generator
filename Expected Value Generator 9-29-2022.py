# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 15:17:16 2022

@author: nengelthaler
"""

import random

total_gains = 0
max_gains = 0
n_game = 10000

for game in range(n_game):
    game_gain = 0
    
    while True:
        dice = random.randint(1,6)
        if dice > 3:
            game_gain +=  dice 
            total_gains +=  dice
        else:
            break 
        
    if game_gain > max_gains:
        max_gains = game_gain

average_won = total_gains/n_game
 

print("The Average amount won = ", average_won, "The max amount won = " , max_gains)