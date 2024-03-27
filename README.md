# Crossway_docdecode



## Presentation

Un petit script Python pour decoder les comptes-rendus d'examens patients dans Crossway (McKesson). Le document brut (LOB) doit etre extrait de la base de donnee Oracle et nommé compte-rendu.lob, le script génerera le fichier compte-rendu.rtf en retour.
Le codage est assez simple, les données du fichier sont en fait zippées et le resultat est corrompu artificiellement en modifiant certains passages (ajout d'un ou deux caractères) en fonction de 3 codes precis recontrés dans le flux de donnée résultant.

