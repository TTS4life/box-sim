#!/usr/bin/python3

import random
import copy

weapons = [
            "CZ75",
            "CZ75 Dual Wield",
            "Python",
            "Spectre",
            "FN FAL",
            "G11",
            "Famas",
            "AUG",
            "Commando",
            "Galil",
            "HS-10",
            "Spas-12",
            "Dragunov",
            "L96A1",
            "RPK",
            "HK21",
            "Ballistic Knife",
            "China Lake",
            "M72 Law",
            "Crossbow",
            "Ray Gun",
            "Thunder Gun",
            "Gersh Device",
            "Dolls"
]


class Player:
    def __init__(self):
        self.gun1 = None
        self.gun2 = None
        self.equipment = None

    # For cooop if ever implemented (probably not lol)
    def holdingBallisticKnife(self):
        return self.gun1 != "Ballistic Knife" or self.gun2 != "Ballistic Knife"
    


class Box:

    def roll(self, player):
        self.weapons = copy.deepcopy(weapons)

        #Remove what the player is holding
        if player.gun1 in self.weapons:
            self.weapons.remove(player.gun1)
        
        if player.gun2 in self.weapons:
            self.weapons.remove(player.gun2)

        if player.equipment is not None:
            self.weapons.remove(player.equipment)

        random.shuffle(self.weapons)
        return random.choice(self.weapons)
    
def find_greatest(stats, weapon):
    value = 0
    for stat in stats:
        if stat[weapon] > value:
            value = stat[weapon]
    return value

def find_least(stats, weapon):
    value = 10000
    for stat in stats:
        if stat[weapon] < value:
            value = stat[weapon]
    return value

    
def main():
    player = Player()
    box = Box()

    stats = []

    num_rolls = 2800

    stats_file = open("total_stats.csv", "w")
    stats_file.write("trial,thunderguns\n")

    for i in range (0, 500):
        # file = open(f"run_{i}", "w")
        stats.append({})
        for j in range (num_rolls):
            weapon = box.roll(player)

            if weapon in ('Gersh Device', 'Dolls'):
                player.equipment = weapon
            elif (player.gun2 is None or player.gun2 == "Thunder Gun"): #Keep TGun in weapon 1
                player.gun2 = weapon
            else:
                player.gun1 = weapon

            # print(f"{j}: {weapon}")

            try:
                stats[i][weapon] = stats[i][weapon] + 1
            except KeyError:
                stats[i][weapon] = 1     
                

        #     file.write(f"{j}: {weapon}: Player has {player.gun1}, {player.gun2}, and {player.equipment}\n")
        # file.write(f"\n\n ==========STATS==========\n")


        # for key, value in stats[i].items():
        #     percentage = round(value/num_rolls * 100, 2)
        #     file.write(f"{key} was rolled {value} times ({percentage}%) \n")
        # file.close()

        stats_file.write(f"{i},{stats[i]['Thunder Gun']}\n")
    
   
    stats_file.close()

    
if __name__ == "__main__":
    main() 