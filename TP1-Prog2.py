# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
def afficherMenu():
   print("*****************************************************************************")
   print("1-Afficher l’ensemble des aliments depuis le fichier Nutrition.CSV       ****")
   print("2-Afficher les aliments en fonction d’une valeur nutritive à la fois     ****")
   print("3-Afficher les valeurs nutritives d’un aliment (Recherche par Id)        ****")
   print("4-Modifier une valeur nutritive d’un aliment par Id )                    ****")
   print("5-Ajouter un aliment                                                     ****")
   print("6-Quitter                                                                ****")
   print("*****************************************************************************")
   choixMenuValide()
def choixMenuValide():
   val = (input("Veuillez entrer votre selection:"))
   if val == "1":
      afficherFichierNutriments()
   elif val == "2":
      option2()
   elif val == "3":
      print(dataSortId.to_string())
      option3()
   elif val == "4":
      option4()
   elif val == "5":
      option5()
   elif val == "6":
      option6()
   else:
      print("*****ATTENTION: Veuillez selectionner une option valide! :ATTENTION*****\n")
      afficherMenu()
def afficherFichierNutriments():
   print(dataSortId.to_string())
   input("Tapez sur une touche pour revenir au menu")
   afficherMenu()
def option2():
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
   input("Tapez sur une touche pour revenir au menu")
   afficherMenu()
def option3():
   df = pd.read_csv("nutrition.csv", sep=";")
   val = input("Veuillez insérer la Id d’un aliment -->")
   if int(val) in df["Id"].values:
      print("L’élément est trouvé!")
      print("***********************************************")
      print(data.loc[int(val)])
      print("***********************************************")
      input("Tapez sur une touche pour revenir au menu")
      afficherMenu()
   else:
      numeroDeIDValide()
      afficherMenu()
def option4():
   global nutriment_select, new_val
   df = pd.read_csv("nutrition.csv", sep=";", encoding='utf-8')
   while True:
      print("*MENU4*\n *Modification d’une valeur nutritive d’un aliment recherche par Id*")
      print("\nVeuillez insérer l'Id du nutriment pour lequel vous voulez faire des modifications-->: ")
      choix = input("#: ")
      is_valid_id = numeroDeIDValide(int(choix))
      print(f"Is valid ID: {is_valid_id}")
      if is_valid_id:
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
      elif choix_nutriment == '6':
         break
      else:
         print("VEUILLEZ CHOISIR UN NUTRIMENT VALIDE")

      valeur_choisi = df.loc[df['Id'] == int(choix), nutriment_select].values[0]
      print("La valeur actuelle de {} est : {}".format(nutriment_select, valeur_choisi ))

      val_modifiable = input("Voulez-vous conserver cette valeur (Oui) OU modifier la valeur (Non) --> ")
      if val_modifiable.lower() == "non":
         new_val = input("Entrez la nouvelle valeur du nutriment: ")

      df.loc[df['Id'] == int(choix), nutriment_select] = new_val
      df.to_csv("nutrition.csv", sep=";", index=False)
      choix_menu = input("Voulez-vous retourner au menu principal (Oui) ou quitter le programme (Non)? ")
      if choix_menu.lower() == "non":
         break
      else:
         afficherMenu()


def option5():
   dfNoId = pd.read_csv('NUTRITION.CSV', index_col=False, sep=";")
   print("Format des données:")
   print(dfNoId.dtypes)
   new_data = {}
   for column in dfNoId.columns:
      if column != 'Id':
         new_data[column] = input(f"Entrez la valeur pour {column}: ")
         dfNoId = dfNoId._append(new_data, ignore_index=True)
         dfNoId.to_csv('NUTRITION.CSV', index=False, mode='a')
   print("Nouvel aliment ajouté avec succès !")

def option6():
    print("Voulez-vous quitter (Oui/Non) ?")
    Reponse = input("-->")
    if Reponse == "oui" or Reponse == "Oui":
        print("Au revoir !")
        exit()
    else:
        afficherMenu()
def option6():
   print("Voulez-vous quitter (Oui/Non) ?")
   Reponse = input("-->")
   if Reponse == "oui":
         print("Au revoir !")
         exit()
   elif Reponse == "Oui":
      print("Au revoir !")
      exit()
   else :
      afficherMenu()
   # ---- Valeurs Option 1 ---- #


def numeroDeIDValide(id_num):
   df = pd.read_csv('nutrition.csv', sep=';', encoding='utf-8')
   return id_num in df['Id'].values


def valeurNutritiveValides(valeur):
   if 0 <= valeur <= 10000:
      return True
   else:
      return False

global valeur
data = pd.read_csv("nutrition.csv", index_col='Id', sep=';', encoding='utf-8')
dataSortId = data.sort_values(by="Id", ascending=True)
tableau = data.values.tolist()
   # ---- Valeurs Option 2 ---- #
dataOptions = pd.read_csv("nutrition.csv", index_col='Id', sep=';', encoding='utf-8')
dataSortEner = dataOptions.sort_values(by="Energ_Kcal", ascending=False)
dataSortProt = dataOptions.sort_values(by="Protéine", ascending=False)
dataSortGras = dataOptions.sort_values(by="gras", ascending=False)
dataSortChol = dataOptions.sort_values(by="Cholestérol", ascending=False)
dataSortSodi = dataOptions.sort_values(by="Sodium", ascending=False)
# ------------------------------ Début Code ---------------------------------- #
afficherMenu()