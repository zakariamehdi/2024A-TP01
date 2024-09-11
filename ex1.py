# TODO: Créer un script permettant le formattage du livre des records des JO.



country = input("De quelle nationalité est l'athlète ? ")
athlete = input("Quel est le nom de l'athlète?")
date = input("Quelle est la date du record?")
sport = input("Dans quel sport?")
categorie = input("Quelle est la categorie specifique?")
record = input("Quel est le record?")
a='--------------------'
chaine1, chaine2, chaine3=f'{date}', f'{sport}-{categorie}', f'{athlete} {country}-{record}'
print('Nouveau record :\n', a, '\n', chaine1, '\n', chaine2, '\n', chaine3)
