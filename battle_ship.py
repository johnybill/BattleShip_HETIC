from enum import Enum
from class_de_base import MapSea
from class_de_base import Ship
from class_de_base import action
from class_de_base import dir
from class_ia import User
from class_ia import IaHunter
from class_ia import IaHunterUltime
from class_ia import IaDumb

import random


class player(Enum):
    USER = 6
    DUMB = 7
    HUNTER = 8
    ULTIMATE = 9






class BattleShip:
    def __init__(self):
        self.map_sea = MapSea(10)
        self.map_sea2 = None 
        self.nb_ship_rest = 5
        self.nb_ship_rest2 = 5
        self.list_ship = [Ship(i) for i in range(5, 1, -1)]
        self.list_ship.insert(2, Ship(3))
        self.player1 = None
        self.player2 = None
    
    
    def party_init(self):
        for sh in self.list_ship:
            sh.reset_ship()
        self.map_sea.reset_map()
        self.nb_ship_rest = 5
    
    
    def is_finish(self):
        return self.nb_ship_rest == 0
    
    
    def generate_grille(self):
        for sh in self.list_ship:
            x = random.randint(0, 9)
            y = random.randint(0, 9)
            direct = dir.VERTI if 1 == random.randint(1,2) else dir.HORI 
            while(not self.map_sea.peut_placer(sh, x, y, direct)):
                x = random.randint(0, 9)
                y = random.randint(0, 9)
                direct = dir.VERTI if 1 == random.randint(1,2) else dir.HORI 
            self.map_sea.place_ship(sh, x, y, direct)
        return

    
    def find_player(self, joueur):
        if joueur is player.USER:
            return User(self.map_sea)
        elif joueur is player.DUMB:
            return IaDumb(10)
        elif joueur is player.HUNTER:
            return IaHunter(10)
        else:
            return IaHunterUltime(10)


    def play_one_game(self, joueur, verbose=False, graphique=False):
        self.player1 = self.find_player(joueur)
        self.party_init()
        if verbose:
            print("welcome new Challenge !!")
        if graphique:
            self.print_map_cache()
        while(not self.is_finish()):
            self.player1.play_one_tour(self.map_sea)
        if verbose:
            print("Congratulation !!")


    def play_one_versus(self, jouer1, jouer2):
        self

    
    def print_map_cache(self):
        ligne_affiche = []
        for ligne in self.map_sea.map_cell:
            ligne_affiche = [conv_cell_int_cache(i) for i in ligne]
            print(ligne_affiche)


def conv_cell_int_cache(cell_m):
    if cell_m.is_hide():
        return 0
    else:
        if cell_m.is_ship():
            return 2
        else:
            return 1


