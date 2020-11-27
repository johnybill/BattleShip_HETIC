import random
class Pile():
    def __init__(self):
        self.stack = []
    
    def empile(self, x):
        self.stack.append(x)
        return None

    def depile(self):
        try:
            return self.stack.pop()
        except:
            return None


class User():
    def __init__(self, grille):
        self.grille = grille
    

    def choice_coup(self):
        bad_input = True
        while(bad_input):
            coor_str = input("entrer les coordonnées sous la forme 'x y'")
            try:
                coor = list(map(int,coor_str.split('_')))
                if self.grille[coor[0]][coor[1]].is_hide():
                    bad_input = False
            except:
                continue
        return coor


    def play_one_tour(self, liste_cell):
        coor = self.choice_coup()
        return liste_cell.see_cell(coor)


class IA:
    def __init__(self, size, grille):
        self.pile_coup = Pile()
        self.coup_jouer = []
        self.track = False
        self.size_map = size

    def croix_hunt(self, x,y):
        list_coor = []
        if 0 < x :
            list_coor.append([x - 1, y])
        if  y < 9:
            list_coor.append([x, y + 1])
        if x < 9:
            list_coor.append([x + 1, y])
        if 0 < y:
            list_coor.append([x, y - 1])
        return list_coor

    def after_coup(self, coup_jouer, resultat):
        pass

class IaHunter(IA):
    def __init__(self, size_map, grille):
        super().__init__(size_map, grille)
    
    def choice_coup(self):
        if self.track:
            return self.pile_coup.depile()
        else:
            random.randint(0, self.size_map)

    def play_one_tour(self):
        self


class IaHunterUltime(IA):
    def __init__(self, size_map, grille):
        super().__init__(size_map, grille)

    def choice_coup(self):
        self
    def play_one_tour(self):
        self


class IaDumb(IA):
    def __init__(self,size_map, grille):
        super().__init__(size_map, grille)

    def choice_coup(self):
        self
    def play_one_tour(self):
        self




class IALearn(IA):
    def __init__(self,size_map, grille):
        super().__init__(size_map, grille)
    def choice_coup(self):
        self
    def play_one_tour(self):
        self

