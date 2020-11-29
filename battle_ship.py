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
        self.instance_player = [IaDumb(10,None), IaHunter(10, None), IaHunterUltime(10, None), User(None)]
        self.player1 = None
        self.player2 = None
    
    
    def party_init(self):
        """
        réinitialise les bateaux, le nombre de bateau qui reste a couler
        et le plateau de jeu    
        """
        for sh in self.list_ship:
            sh.reset_ship()
        self.map_sea.reset_map()
        self.nb_ship_rest = 5
    
    
    def is_finish(self):
        """ 
        retourne une valeur boolean pour dire si la partie est terminée
        """
        return self.nb_ship_rest == 0
    
    
    def generate_grille(self):
        """ 
        placer de manière aléatoire les bateaux sur la map du jeu
        """
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

    
    def find_player(self, joueur, map_jeu):
        """
        retourne l'instance joueur désirer et ajouter le plateau jeu au joueur
        joueur - enum - indique quelle joueur on souhaite 
        map_jeu - MapSea - le plateau de jeu du joueur
        """
        if joueur is player.USER:
             self.instance_player[3].grille = map_jeu
             return self.instance_player[3]
        elif joueur is player.DUMB:
            self.instance_player[0].grille = map_jeu
            return self.instance_player[0]
        elif joueur is player.HUNTER:
            self.instance_player[1].grille = map_jeu
            return self.instance_player[1]
        else:
            self.instance_player[2].grille = map_jeu
            return self.instance_player[2]


    def play_one_game(self, joueur, verbose=False, graphique=False):
        self.player1 = self.find_player(joueur, self.map_sea)
        self.party_init()
        #TODO faire cette fonction pour que le player 
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


