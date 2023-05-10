import pandas as pd

# Lire le fichier CSV
df = pd.read_csv('NUTRITION.CSV')

# Afficher le format des données
print("Format des données:")
print(df.dtypes)

# Demander à l'utilisateur d'entrer les données
new_data = {}
for column in df.columns:
    if column != 'ID':
        new_data[column] = input(f"Entrez la valeur pour {column}: ")

# Ajouter les nouvelles données au DataFrame
df = df.append(new_data, ignore_index=True)

# Trier les données par ID
df = df.sort_values(by='ID')

# Afficher l'ensemble du fichier
print(df.to_string())

# Enregistrer les modifications dans le fichier CSV
df.to_csv('NUTRITION.CSV', index=False)
