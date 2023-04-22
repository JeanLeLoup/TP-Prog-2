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

def option1():
   print("yes sir!")
   print(data.to_string())
   mainMenu()
def option2():
   print("yay 2!")
   from pandas import DataFrame
   dataFrm = DataFrame(data, columns=['Id', 'Catégorie', 'Description', 'Energ_Kcal'])
   # chemin vers un fichier pour stocker les resultats
   export_csv = dataFrm.to_csv(r'Pandaresult.csv', index=None, header=False)
   print(dataFrm)


def option3():
   print("yay 3!")
def option4():
   print("yay 4!")
def option5():
   print("yay 5!")
def option6():
   print("vous avez quitté!")
#------------------------------Début Code----------------------------------#
global val
global data
data = pd.read_csv("nutrition.csv")

mainMenu()
print("Veuillez taper votre selection:")
val = (input())
if val == "1":
   option1()
elif val == "2":
   option2()
elif val == "3":
   option3()
elif val == "4":
   option4()
elif val == "5":
   option5()
elif val == "6":
   option6()
else:
   print("oh no!")