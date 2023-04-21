#import os
import pandas as pd


def mainMenu():
   print("*****************************************************************************")
   print("1-Afficher l’ensemble des aliments depuis le fichier Nutrition.CSV       ****")
   print("2-Afficher les aliments en fonction d’une valeur nutritive à la fois     ****")
   print("3-Afficher les valeurs nutritives d’un aliment (Recherche par ID)        ****")
   print("4-Modifier une valeur nutritive d’un aliment par ID )                    ****")
   print("5-Ajouter un aliment                                                     ****")
   print("6-Quitter                                                                ****")
   print("*****************************************************************************")

#------------------------------Début Code----------------------------------#

mainMenu()
print("Veuillez taper votre selection:")
val = (input())
data = pd.read_csv("nutrition.csv")
print(data)