def convertion(nombre):
    if (nombre[0]=="I"):
        return 1
    if (nombre[0]=="V"):
        return 5
    if (nombre[0]=="X"):
        return 10
    if (nombre[0]=="L"):
        return 50
    if (nombre[0]=="C"):
        return 100
    if (nombre[0]=="D"):
        return 500
    if (nombre[0]=="M"):
        return 1000
    return 0

def particularite(nombre):
    if nombre[0] == "I":
        if nombre[1] == "V" or nombre[1] == "X" or nombre[1] == "L" or nombre[1] == "C" or nombre[1] == "D" or nombre[1] == "M":
            return -1
        return 1
    if nombre[0] == "V":
        if nombre[1] == "X" or nombre[1] == "L" or nombre[1] == "C" or nombre[1] == "D" or nombre[1] == "M":
            return -5
        return 5
    if nombre[0] == "X":
        if nombre[1] == "L" or nombre[1] == "C" or nombre[1] == "D" or nombre[1] == "M":
            return -10
        return 10
    if nombre[0] == "L":
        if nombre[1] == "C" or nombre[1] == "D" or nombre[1] == "M":
            return -50
        return 50
    if nombre[0] == "C":
        if nombre[1] == "D" or nombre[1] == "M":
            return -100
        return 100
    if nombre[0] == "D":
        if nombre[1] == "M":
            return -500
        return 500

def afficher_nombre(nombre):
    longueur = len(nombre)
    i = 0
    somme_nombre =0
    while ( i<longueur -1):
        if (convertion(nombre[i])<convertion(nombre[i+1])):
            somme_nombre = somme_nombre + particularite(nombre[i:i + 2])
        else:
            somme_nombre = somme_nombre + convertion(nombre[i])
        i=i+1
    somme_nombre = somme_nombre + convertion(nombre[i])
    return somme_nombre

def somme(operande,nombre1,nombre2):
    if (operande == '+'):
        nombre1=afficher_nombre(nombre1)
        nombre2=afficher_nombre(nombre2)
        return nombre1 +nombre2

def soustraction(operande,nombre1,nombre2):
    if ( operande == '-' ):
        nombre1 = afficher_nombre(nombre1)
        nombre2 = afficher_nombre(nombre2)
        if nombre1 < nombre2 :
            return nombre2-nombre1
        return nombre1 - nombre2

def multiplication(operande,nombre1,nombre2):
    if ( operande == '*' ):
        nombre1 = afficher_nombre(nombre1)
        nombre2 = afficher_nombre(nombre2)
        return nombre1 * nombre2

def division(operande,nombre1,nombre2):
    if ( operande == '/' ):
        nombre1 = afficher_nombre(nombre1)
        nombre2 = afficher_nombre(nombre2)
        if nombre2 != 0 :
            return nombre1 / nombre2
        return "Erreur"
