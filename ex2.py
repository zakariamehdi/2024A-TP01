# TODO: Créer un script pour calculer les ressources nécessaires pour assainir la Seine.
# TODO: Importer les modules nécessaires.

quantite_eau=float(input("Quelle est la quantite d'eau requise?"))
filtre= 0.2*quantite_eau
lampes_UV= 0.6*quantite_eau
chlore= 0.1*quantite_eau



print(f"Voici les elements necessaires pour {quantite_eau}L")
print(f"-Filtre = {filtre:14}")
print(f"-Lampes UV= {lampes_UV:12}" )
print(f"-Chlore= {chlore:15}kg")