#TP1
#compter le nombre de mots d'une chaine

#définir la chaine
chaine="la fonction devra retourner le nombre de mots"
#imprimer la chaine
print("La chaine de charactères est: "+chaine)
#utiliser split pour compter le nombre de mots
count_word=len(chaine.split())
#imprimer le nombre de mots
print("Le nombre de mots est: "+str(count_word))
