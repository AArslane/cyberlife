#Narnia0 : Payload 

##Objectif :
Modifier la variable 'val' grace à un buffer overflow pour obtenir '0xdeadbeef' :
  1.Trouver la distance entre 'buf' et 'val' (20 oct)
  2.Mettre en place le payload : 
    Padding de 20 bytes : ('B*20')
    4 bytes pour val en little-endian
  3.Tester Payload

##Fichiers :
-make_payload.py
-payload.bin

##Résultat :
-val modifié : accès au mot de passe.
