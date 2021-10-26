#!/usr/bin/env python
# -*- coding: utf-8 -*-
#chap 7
import math
import turtle
def volume_masse_ellipsoide(a=1,b=1,c=1,masse_volumique = 1):
    volume = 4/3 * a * b * c * math.pi
    masse = masse_volumique * volume
    return masse,volume
def trie_lettre(phrase: str) -> (dict,list):
    dict = {}
    for lettre in phrase:
        if not lettre in dict.keys():
            dict[lettre] = 1
        else:
            dict[lettre] +=1
    return dict, sorted(dict.items(), key = lambda item:item[1],reverse=True)[0][0]
#Fonction pour exercise 4:
def validation_adn(adn: str)->bool:
    if not adn:
        return False
    else:
        for i in adn:
            if i != "a" and i != "t" and i != "g" and i != "c":
                return False
        return True
def saisie()->(str,str):
    valideur = True
    while valideur:
        sequence = input("Entrez une chaine d'ADN: ")
        chaine = input("Entrez une séquence: ")
        if validation_adn(sequence) and validation_adn(chaine):
            valideur = False
        else:
            print("mauvaise entrée")
    return sequence, chaine
def analyseur(chaine: str,sequence: str) -> float:
    liste_chaine = split_chain(chaine)
    occurence = 0
    for i in liste_chaine:
        if i == sequence:
            occurence += 1
    return occurence/len(liste_chaine) * 100
def split_chain(chaine:str)->list:
    liste_chaine = []
    for i in range(2,len(chaine)+2,2):
        liste_chaine.append(chaine[i-2:i])
    return liste_chaine
def principale()->None:
    chaine, sequence = saisie()
    pourcentage = analyseur(chaine,sequence)
    print("Il y a " + str(pourcentage) + "% de " + sequence)


if __name__ == '__main__':
    #print(volume_masse_ellipsoide(4,5,2,45))
    #print("La liste trié: " + str(trie_lettre("allo")[0]) + ", la lettre avec le nombre d'occurence le plus grand: " + str(trie_lettre("allo")[1]))
    #principale()