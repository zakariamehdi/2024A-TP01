# TODO: Écrire un programme qui demande le pourcentage de charge actuel de la batterie du bateau,
#        calcule la distance restante en km en fonction de ce pourcentage,
#        et affiche le résultat au format "XX km".
#        Assurez une gestion du pourcentage valide au cours de votre programme (% toujours dans [0 ; 100]).

battery_level = float(input("Saisir le niveau de batterie du bateau: "))
if battery_level <= 100 and >=  50 :
    print(round(((battery_level-50)*2+70),1),"km")
elif battery_level < 50 and >= 25 :
    print(round(((battery_level-25)*0,5+57,5),))
