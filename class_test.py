import unittest
from class_de_base import Cell
from class_de_base import dir
from class_de_base import action
from class_de_base import Ship
from class_de_base import MapSea
from class_ia import IaDumb
from class_ia import IaHunter
from class_ia import IaHunterUltime
from class_ia import Pile
from battle_ship import BattleShip


class test_ship(unittest.TestCase):
    
    
    def setUp(self):
        self.ship_test = Ship(2)
    
    
    def test_init_ship_except_lenght(self):
        self.assertEqual(2,self.ship_test.lenght)
        self.assertEqual(2, self.ship_test.life)
        self.assertFalse(self.ship_test.couler)

    def test_touche(self):
        self.assertEqual(2, self.ship_test.life)
        self.assertEqual(action.TOUCHE, self.ship_test.touche())
        self.assertEqual(1, self.ship_test.life)
        self.assertEqual(2, self.ship_test.lenght)
        self.assertFalse(self.ship_test.couler)
        self.assertEqual(action.COULER, self.ship_test.touche())
        self.assertEqual(0, self.ship_test.life)
        self.assertTrue(self.ship_test.couler)

    def test_is_couler(self):
        self.assertFalse(self.ship_test.is_couler())
        self.ship_test.touche()
        self.ship_test.touche()
        self.assertTrue(self.ship_test.is_couler())


    def test_reset_ship(self):
        self.ship_test.touche()
        self.ship_test.touche()
        self.assertEqual(0, self.ship_test.life)
        self.assertTrue(self.ship_test.couler)
        self.ship_test.reset_ship()
        self.assertEqual(2, self.ship_test.life)
        self.assertFalse(self.ship_test.couler)


class test_Cell(unittest.TestCase):    
    
    
    def setUp(self):
        self.ship_test = Ship(2)
        self.cell_test = Cell()

    def test_init(self):
        self.assertFalse(self.cell_test.jouer)
        self.assertIsNone(self.cell_test.ship_cell) 

    def test_change_view(self):
        self.assertEqual(self.cell_test.change_view(), action.NOTHING)
        self.assertTrue(self.cell_test.jouer)
        
    
    def test_add_ship(self):
        self.cell_test.add_ship(self.ship_test)
        self.assertIsInstance(self.cell_test.ship_cell, Ship)
    

    def test_is_ship(self):
        self.cell_test.add_ship(self.ship_test)
        self.assertTrue(self.cell_test.is_ship())

    def test_is_hide(self):
        self.assertTrue(self.cell_test.is_hide())
        self.cell_test.change_view()
        self.assertFalse(self.cell_test.is_hide())


class test_map_sea(unittest.TestCase):

    def setUp(self):
        self.map_sea_test = MapSea(5)
        self.cell_test = Cell()
    
    
    def test_map_init(self):
        self.assertEqual(self.map_sea_test.size, len(self.map_sea_test.map_cell))
        self.assertEqual(self.map_sea_test.size, len(self.map_sea_test.map_cell[1]))
        for ligne in self.map_sea_test.map_cell:
            for member in ligne:
                self.assertIsInstance(member, Cell)
    

    def test_place_ship(self):
        ship1 = Ship(5)
        self.map_sea_test.place_ship(ship1, 0, 0, dir.HORI)
        for i in range(5):
            self.assertTrue(self.map_sea_test.map_cell[0][i].is_ship())
            self.assertTrue(self.map_sea_test.map_cell[0][i].ship_cell.lenght)
        ship2 = Ship(2)
        self.map_sea_test.place_ship(ship2, 1, 1, dir.VERTI)
        for i in range(2):
            self.assertTrue(self.map_sea_test.map_cell[i + 1][1].is_ship())
            self.assertTrue(self.map_sea_test.map_cell[i + 1][1].ship_cell.lenght)
        nb_cell_with_ship = 0
        for ligne in self.map_sea_test.map_cell:
            for cell_m in ligne:
                if cell_m.is_ship():
                    nb_cell_with_ship += 1
        self.assertEqual(7,nb_cell_with_ship)


    def test_peut_placer(self):
        ship1 = Ship(5)
        # test quand il y a rien sur la map
        for i in range(self.map_sea_test.size):
            self.assertTrue(self.map_sea_test.peut_placer(ship1, i, 0, dir.HORI))

        for i in range(self.map_sea_test.size):
            self.assertTrue(self.map_sea_test.peut_placer(ship1, 0, i, dir.VERTI))
         
        for i in range(self.map_sea_test.size):
            for j in range(1, self.map_sea_test.size):
                self.assertFalse(self.map_sea_test.peut_placer(ship1, i, j, dir.HORI))

        for i in range(1,self.map_sea_test.size):
            for j in range( self.map_sea_test.size):
                self.assertFalse(self.map_sea_test.peut_placer(ship1, i, j, dir.VERTI))
        
        self.map_sea_test.place_ship(ship1, 2, 0, dir.HORI)
        ship2 = Ship(3)
        # test quand il y a un bateau sur la map
        for i in range(self.map_sea_test.size):
            for j in range(self.map_sea_test.size):
                self.assertFalse(self.map_sea_test.peut_placer(ship2, i, j, dir.VERTI))

        for i in range(self.map_sea_test.size):
            self.assertFalse(self.map_sea_test.peut_placer(ship2, 0, i, dir.VERTI))
        
        for i in range(3, self.map_sea_test.size):
            self.assertTrue(self.map_sea_test.peut_placer(ship2, i, 0, dir.HORI))

    def test_see_cell(self):
        ship2 = Ship(2)
        self.map_sea_test.place_ship(ship2, 1,0, dir.HORI)
        self.assertEqual(action.NOTHING, self.map_sea_test.see_cell(0,0))
        self.assertEqual(action.TOUCHE, self.map_sea_test.see_cell(1,0))
        self.assertEqual(action.COULER, self.map_sea_test.see_cell(1,1))


    def test_reset_map(self):
        ship1 = Ship(5)
        ship2 = Ship(2)
        self.map_sea_test.place_ship(ship1, 0, 0, dir.HORI)
        self.map_sea_test.place_ship(ship2, 1, 0, dir.VERTI)
        nb_cell_with_ship = 0
        for ligne in self.map_sea_test.map_cell:
            for cell_m in ligne:
                if cell_m.is_ship():
                    nb_cell_with_ship += 1
        self.assertEqual(7,nb_cell_with_ship)
        for ligne in self.map_sea_test.map_cell:
            ligne[0].change_view()
        self.map_sea_test.reset_map()
        nb_cell_with_ship = 0
        for ligne in self.map_sea_test.map_cell:
            for cell_m in ligne:
                if cell_m.is_ship():
                    nb_cell_with_ship += 1
        self.assertEqual(0,nb_cell_with_ship)
        for ligne in self.map_sea_test.map_cell:
            self.assertTrue(ligne[0].is_hide())

class test_BattleShip(unittest.TestCase):
    def setUp(self):
        self.bs_test = BattleShip()

    def test_init_BattleShip(self):
        self.assertIsInstance(self.bs_test.map_sea, MapSea)
        self.assertEqual(5, self.bs_test.nb_ship_rest)


    def test_is_finish(self):
        self.assertFalse(self.bs_test.is_finish())
    
    
    def test_generate_grille(self):
        for ligne in self.bs_test.map_sea.map_cell:
            for cell_m in ligne:
                self.assertFalse(cell_m.is_ship())
        self.bs_test.generate_grille()
        nb_cell_with_ship = 0
        for ligne in self.bs_test.map_sea.map_cell:
            for cell_m in ligne:
                if cell_m.is_ship():
                    nb_cell_with_ship += 1
        self.assertEqual(17,nb_cell_with_ship)

    
    def test_print_map_cache(self):
        print()
        self.bs_test.print_map_cache() 


class test_iaDumb(unittest.TestCase):
    def setUp(self):
        self.test_map = MapSea(5)
        self.ia_test = IaDumb(5, self.test_map)
    
    def test_init_ia_dumb(self):
        self.assertListEqual(self.ia_test.coup_jouer, [])
        self.assertFalse(self.ia_test.track)
        self.assertEqual(self.ia_test.size_map, self.test_map.size)

    def test_choice_coup(self):
        self.assertTrue(self.ia_test)
    
    
    def test_play_one_tour(self):
        pass

class test_IaHunter(unittest.TestCase):
    def setUp(self):
        self.test_map = MapSea(10)
        self.ia_test = IaHunter(10, self.test_map)
    
    def test_init_IA_Hunter(self):
        self.assertIsInstance(self.ia_test.pile_coup, Pile)
        self.assertIsInstance(self.ia_test.coup_jouer, set)
        self.assertFalse(self.ia_test.track)
        self.assertEqual(self.ia_test.size_map, self.test_map.size)

    def test_croix_hunt(self):
        # la croix quand il y aucune coup fait
        self.assertListEqual([[0, 1],[1, 2], [2, 1], [1, 0]], 
                            self.ia_test.croix_hunt(1, 1))
        self.assertListEqual([[0, 1],[1, 0]],self.ia_test.croix_hunt(0, 0))
        self.assertListEqual([[0, 2],[1, 1],[0, 0]],self.ia_test.croix_hunt(0, 1))
        self.assertListEqual([[1, 9],[0, 8]],self.ia_test.croix_hunt(0, 9))
        self.assertListEqual([[0, 9],[2, 9],[1, 8]],self.ia_test.croix_hunt(1, 9))
        self.assertListEqual([[8, 9],[9, 8]],self.ia_test.croix_hunt(9, 9))
        self.assertListEqual([[8, 1],[9, 2],[9, 0]],self.ia_test.croix_hunt(9, 1))
        self.assertListEqual([[8, 0],[9, 1]],self.ia_test.croix_hunt(9, 0))
        self.assertListEqual([[0, 0],[1, 1],[2, 0]],self.ia_test.croix_hunt(1, 0))
    # quand il y a 1 coups déjà joué en adjacent
        self.test_map.see_cell(0, 1)
        self.test_map.see_cell(1, 1)
        self.test_map.see_cell(9, 1)
        self.test_map.see_cell(9, 8)
        self.assertListEqual([[1, 2], [2, 1], [1, 0]], 
                            self.ia_test.croix_hunt(1, 1))
        self.assertListEqual([[1, 0]],self.ia_test.croix_hunt(0, 0))
        self.assertListEqual([[0, 2],[0, 0]],self.ia_test.croix_hunt(0, 1))
        self.assertListEqual([[1, 9],[0, 8]],self.ia_test.croix_hunt(0, 9))
        self.assertListEqual([[0, 9],[2, 9],[1, 8]],self.ia_test.croix_hunt(1, 9))
        self.assertListEqual([[8, 9]],self.ia_test.croix_hunt(9, 9))
        self.assertListEqual([[8, 1],[9, 2],[9, 0]],self.ia_test.croix_hunt(9, 1))
        self.assertListEqual([[8, 0]],self.ia_test.croix_hunt(9, 0))
        self.assertListEqual([[0, 0],[2, 0]],self.ia_test.croix_hunt(1, 0))
    # quand il y a 2 coups déjà joué 

    def test_choice_coup(self):
        self.assertTrue(self.ia_test)
     
    
    def test_play_one_tour(self):
        pass


class test_IaHunterUltime(unittest.TestCase):
    def setUp(self):
        self.test_map = MapSea(5)
        self.ia_test = IaHunterUltime(5, self.test_map)
        
    
    def test_init_ia_dumb(self):
        pass

    def test_choice_coup(self):
        self.assertTrue(self.ia_test)
        pass
    
    
    def test_play_one_tour(self):
        pass

if __name__ == '__main__':
    unittest.main()