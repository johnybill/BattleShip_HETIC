# BattleShip_HETIC

# Lisez le svp
le fichier battle_ship.py contient la classe principal pour faire tourner le jeu
  #TODO il faut finir les fonctions permettant d'y jouer seul ou contrer quelqu'un (on pourra jouer que contrer des IA) 
  
le fichier classe_de_base contient toutes  les class utiles au plateau et au jeu. Toutes les fonctions marchent et on déjà été testé.

le fichier class_test contient toutes les tests unitaires de toutes les classes, chaque partie sera confirmé par la validation de ces tests - Ce fichier EST INTOUCHABLE sans mon accord. les tests seront à ma charge toute au long du projet, si vous pensez qu'un test ne va pas. je serais ravie d'en parler.  

le fichier class_ia contient toutes les classes IA et User
  toutes les classes contient les méthodes choice_coup et play_one_tour:
    choice_coup renvoie le prochaine case à jouer pour les IA et la case choisi par le joueur, la case choisie devra être non jouée
    play_one_tour fait jouer le joueur pendant un tour, pour les IAHunter et IaHunterUltimate ça permet de changer de status Hunter et track quand on touche ou coule un bateau
    
  toutes les classes sont hérité de IA:
  * class IaDumb   :  joue de manière aléatoire
  * class IaHunter :  cherche de manière aléatoire, s'il touche un bateau, recherche les cellules adjacente pour chercher 
  * class IaHunterUltime  :   
