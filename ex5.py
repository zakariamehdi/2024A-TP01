#TODO: Analyser la chaîne de caractères saisie et compter le nombre de médailles.
#      Attention si la chaîne est invalide, un message d'erreur est attendu.
country = input("Quel est le pays?")
code_medals = input("Quelles medales ont ete remportees?")
print(country,':')
print('-',code_medals.count('G'), 'Or')
print('-',code_medals.count('S'), 'Argent')
print('-',code_medals.count('B'), 'Bronze')