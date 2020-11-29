from enum import Enum


class action(Enum):
    HIDE = 0
    NOTHING = 1
    TOUCHE = 2
    COULER = 3

class dir(Enum):
    HORI = 0
    VERTI = 1


class Ship:
    def __init__(self, lengh):
        if  1 < lengh < 6:
            self.lenght = lengh
            self.life = lengh
        else:
            raise ValueError
        self.couler = False
    

    def touche(self):
        """ 
        enlever un point de vie du bateau, 
            si la vie n'est pas à 0: renvoie TOUCHE
            sinon renvoie COULER
        return enum action
        """
        self.life -= 1
        if self.life == 0:
            self.couler = True
            return action.COULER
        else:
            return action.TOUCHE


    def is_couler(self):
        """
        renvoie si le bateau est coulée
        return type: bool
        """
        return self.couler
    

    def reset_ship(self):
        """ 
        le bateau récuper sa vie et le fait de ne pas être couler.
        return type: None
        """
        self.couler = False
        self.life = self.lenght


class Cell:
    def __init__(self):
        self.jouer = False
        self.ship_cell = None
    
    
    def change_view(self):
        """ 
        retourne la valeur d'un cellule caché, après la cellule est visible
        return enum - action
        """
        self.jouer = True
        if self.ship_cell is None:
            return action.NOTHING
        else:
            return self.ship_cell.touche()

    
    def add_ship(self, ship):
        """
        ajouter un pointeur de l'instance Ship
        return None
        """
        self.ship_cell = ship

    
    def is_ship(self):
        """ 
        vérifie si un bateau est sur la cellule.
        return Bool
        """
        return not self.ship_cell is None
    
    
    def reset_cell(self):
        """ 
        cache la cellule et enlever le pointeur du bateau
        return None
        """
        self.jouer = False
        self.add_ship(None)
    
    
    def is_hide(self):
        """
        verifie si la cellule est cache.
        return Bool 
        """
        return not self.jouer 


class MapSea:
    def __init__(self, size):
        self.size = size
        self.map_cell = [[Cell() for _ in range(self.size)] for _ in range(self.size)]

    
    def place_ship(self, ship, x, y, direct):
        """
        place un bateau sur la map.
        ship - instance - classe Ship
        x - int - coordonné de ligne du nez de bateau 
        y - int - coordonné de colonne du nez de bateau
        direct - enum - indique si le bateau est placé de manière 
        horizontale ou verticale.
        return None
        """
        if direct is dir.HORI:
            for i in range(y, ship.lenght + y):
                self.map_cell[x][i].add_ship(ship)
        else:
            for i in range(x, ship.lenght + x):
                self.map_cell[i][y].add_ship(ship)
        return None
    
    
    def peut_placer(self, ship, x, y, direct):
        """
        verifie si le bateau peut être placer avec cette configuration.
        ship - instance - classe Ship
        x - int - coordonné de ligne du nez de bateau 
        y - int - coordonné de colonne du nez de bateau
        direct - enum - indique si le bateau est placé de manière 
        horizontale ou verticale.
        return Bool
        """
        if direct is dir.HORI:
            if (y + ship.lenght) > self.size:
                return False
            elif x > self.size:
                return False
            else:
                for i in range(y, y + ship.lenght):
                    if self.map_cell[x][i].is_ship():
                        return False
                return True 
        else:
            if (x + ship.lenght) > self.size:
                return False
            elif 0 > y > self.size:
                return False
            else:
                for i in range(x, x + ship.lenght):
                    if self.map_cell[i][y].is_ship():
                        return False
                return True 


    def see_cell(self, x, y):
        """
        regarde ce qui se trouve sur une cellule du plateau.
        x - int - coordoné de la celulle 
        y - int - coordonné de la cellule
        return - enum - action
        """
        # return action.COULER 
        return self.map_cell[x][y].change_view()


    def reset_map(self):
        """ 
        les celulles sont de nouveau caché et ne contient aucun bateau.
        """
        for ligne in self.map_cell:
            for cell_m in ligne:
                cell_m.reset_cell()