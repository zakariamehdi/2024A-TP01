# TODO: Créer un script pour calculer les ressources nécessaires pour assainir la Seine.
# TODO: Importer les modules nécessaires.

quantite_eau=float(input("Quelle est la quantite d'eau requise?"))
filtre= 0.2*quantite_eau
lampes_UV= 0.6*quantite_eau
chlore= 0.1*quantite_eau

print("Voici les elements necessaires pour", quantite_eau,"L \n     -Filtre =", filtre,"\n     -Lampes UV=", lampes_UV, "\n     -Chlore=", chlore,"kg")