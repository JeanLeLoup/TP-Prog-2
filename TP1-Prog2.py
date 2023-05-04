# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np


def mainMenu():
   print("*****************************************************************************")
   print("1-Afficher l’ensemble des aliments depuis le fichier Nutrition.CSV       ****")
   print("2-Afficher les aliments en fonction d’une valeur nutritive à la fois     ****")
   print("3-Afficher les valeurs nutritives d’un aliment (Recherche par Id)        ****")
   print("4-Modifier une valeur nutritive d’un aliment par Id )                    ****")
   print("5-Ajouter un aliment                                                     ****")
   print("6-Quitter                                                                ****")
   print("*****************************************************************************")
   val = (input("Veuillez entrer votre selection:"))
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
   mainMenu()
   input("Tapez une touche pour continuer:")
def option1():
   print("yay 1!")
   print(dataSortId.to_string())
def option2():
   print("yay 2!")
   print("Veuillez choisir une valeur nutritive : (Energ_Kcal; Protéine; gras; Cholestérol; Sodium) ")
   choix = input()
   if choix == "Energ_Kcal":
      from pandas import DataFrame
      dataFrmEnerg = DataFrame(dataSortEner, columns=['Catégorie', 'Description', 'Energ_Kcal'], )
      print(dataFrmEnerg.to_string())
      dataFrmEnerg.to_csv(r'nutrition_Energ_Kcal.csv')
   elif choix == "Protéine":
      from pandas import DataFrame
      dataFrmProt = DataFrame(dataSortProt, columns=['Catégorie', 'Description', 'Protéine'], )
      print(dataFrmProt.to_string())
      dataFrmProt.to_csv(r'nutrition_Protéine.csv')
   elif choix == "gras":
      from pandas import DataFrame
      dataFrmGras = DataFrame(dataSortGras, columns=['Catégorie', 'Description', 'gras'], )
      print(dataFrmGras.to_string())
      dataFrmGras.to_csv(r'nutrition_gras.csv')
   elif choix == "Cholestérol":
      from pandas import DataFrame
      dataFrmChol = DataFrame(dataSortChol, columns=['Catégorie', 'Description', 'Cholestérol'], )
      print(dataFrmChol.to_string())
      dataFrmChol.to_csv(r'nutrition_Cholestérol.csv')
   elif choix == "Sodium":
      from pandas import DataFrame
      dataFrmSodium = DataFrame(dataSortSodi, columns=['Catégorie', 'Description', 'Sodium'], )
      print(dataFrmSodium.to_string())
      dataFrmSodium.to_csv(r'nutrition_Sodium.csv')
   # pour exportation ###################################
   #from pandas import DataFrame
   #dataFrmEnerg = DataFrame(dataSortId, columns=['Catégorie', 'Description', 'Energ_Kcal'], )
   #print(dataFrmEnerg.to_string())
   # chemin vers un fichier pour stocker les resultats
   #export_csv = dataFrmEnerg.to_csv(r'Pandaresult.csv')
def option3():
   print("yay 3!")
   val = input("Veuillez insérer la Id d’un aliment -->")
   print("L’élément est trouvé!")
   print("***********************************************")
   print(dataEnTete.loc[int(val)])
   print("***********************************************")


def option4():
   df = pd.read_csv("nutrition.csv", sep=";")
   while True:
      print("*MENU4*\n *Modification d’une valeur nutritive d’un aliment recherche par Id*")
      print("\nVeuillez insérer l'Id du nutriment pour lequel vous voulez faire des modifications-->: ")
      choix = input("#: ")
      if int(choix) in df["Id"].values:
         print(df.loc[df["Id"] == int(choix), ["Id", "Description"]])
         print("Veuillez saisir le numéro correspondant du nutriment voulu!: ")
         print("1- Energ_kcal")
         print("2- Protéine")
         print("3- gras")
         print("4- Cholesterol")
         print("5- Sodium")
      else:
         print("*****ATTENTION: Veuillez insérer un Id de nutriment valide! :ATTENTION*****\n")
         continue

      choix_nutriment =input()

      if choix_nutriment == "1":
         nutriment_select = "Energ_Kcal"
      elif choix_nutriment =="2":
         nutriment_select ="Protéine"
      elif choix_nutriment == '3':
         nutriment_select = 'gras'
      elif choix_nutriment == '4':
         nutriment_select = 'Cholestérol'
      elif choix_nutriment == '5':
         nutriment_select = 'Sodium'
      else:
         print("VEUILLEZ CHOISIR UN NUTRIMENT VALIDE")

      valeur_choisi = df.loc[df['Id'] == int(choix), nutriment_select].values[0]
      print("La valeur actuelle de {} est : {}".format(nutriment_select, valeur_choisi ))

      val_modifiable = input("Voulez-vous conserver cette valeur (Oui) OU modifier la valeur (Non) --> ")
      if val_modifiable.lower() == "non":
         new_val = input("Entrez la nouvelle valeur du nutriment: ")


def option5():
   print("yay 5!")
def option6():
   print("vous avez quitté!")
# ------------------------------ Début Code ---------------------------------- #
global val
#global data
#global dataSortId
   # ---- Valeurs Option 1 ---- #
data = pd.read_csv("nutrition.csv", index_col='Id', sep=';', encoding='utf-8')
dataSortId = data.sort_values(by="Id", ascending=True)
   # ---- Valeurs Option 2 ---- #
dataOptions = pd.read_csv("nutrition.csv", index_col='Id', sep=';', encoding='utf-8')
dataSortEner = dataOptions.sort_values(by="Energ_Kcal", ascending=False)
dataSortProt = dataOptions.sort_values(by="Protéine", ascending=False)
dataSortGras = dataOptions.sort_values(by="gras", ascending=False)
dataSortChol = dataOptions.sort_values(by="Cholestérol", ascending=False)
dataSortSodi = dataOptions.sort_values(by="Sodium", ascending=False)
   # ---- Valeurs Option 3 ---- #
dataEnTete = pd.read_csv("nutrition.csv",index_col='Id',sep=';', encoding='utf-8')
   # ---- Valeurs Option 4 ---- #

   # ---- Valeurs Option 5 ---- #

   # ---- Valeurs Option 6 ---- #

mainMenu()
