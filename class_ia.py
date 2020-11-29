import random
class Pile():
    """ """
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
        """ """
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
        self.coup_jouer = {}
        self.track = False
        self.size_map = size
        self.grille = grille
        self.first_touch = None

    def croix_hunt(self, x,y):
        """ 
        retourne une liste de coordonnée des pointes adjaceant non joué du point (x, y)
        x - int - coordonné du point
        y - int - coordonné du point
        """
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

# Chaque fois la fonction choice_coup se trouve dans play_one_tour
class IaDumb(IA):
    """ 
    chaque fois l'IA prend une position aleatoire d'une cellule qui n'a pas été encore joué
    (on peux savoir si un cellule n'a pas été joué en appelant la fonction is_hide de la class cell)

    """
    def __init__(self,size_map, grille):
        super().__init__(size_map, grille)

    def choice_coup(self):
        self
    def play_one_tour(self):
        self

class IaHunter(IA):
    """
    cette IA possédent 2 phase distincts:
    - Hunter, l'ia cherche de manière aléatoire la position d'un bateau, une fois trouvé
        elle passe en mode track.
    - track l'Ia cherche les positions adjacentes du point trouvé jusqu'à que le bateau coule,
        si un autre bateau est découvert pendant cette phase, elle ajoute les positions adjacent 
        non joué de ce bateau et commence la track de celui-ci. (utilise le principe de la pile)
        la track prend fin une fois que tous les bateaux tracker sont coulés
    une fois la track terminé l'Ia recherche à nouveau de manière aléatoire le prochain bateau.
    """
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
    """
    cette Ia possédent la même phase de track que l'IaHunter, seul la phase Hunter 
    est différentes, l'Ia ne prendra en position aléatoire que des positions dont la somme 
    des coordonnées est un multiple de 2.

    """
    def __init__(self, size_map, grille):
        super().__init__(size_map, grille)

    def choice_coup(self):
        self
    def play_one_tour(self):
        self


class IALearn(IA):
    """ 
    cette IA aura en attribut un dictionnaire ayant pour clé un chiffre float et en valeurs
    une IA.
    chaque type doit être contenu dedans et la somme des clés doit faire 1 ou 100
    plusieurs implémentations sont possible pour cette IA 

    1. l'ia prend au hasard une des Ia en dictionnaire pour jouer un tour, l'ia comptera la 
    stratégie qu'elle a le plus joué et décidera de dimunier sa probabilité d'être joué à la prochaine partie.
    à l'inverse si elle gagne elle augmentera cette probabilité.
    2. l'ia prend au hasard une des Ia en dictionnaire et joue sa stratégie pendant toute la partie. 
    même résultat que dans le premier cas.   
    """
    def __init__(self,size_map, grille):
        super().__init__(size_map, grille)
    def choice_coup(self):
        self
    def play_one_tour(self):
        self

