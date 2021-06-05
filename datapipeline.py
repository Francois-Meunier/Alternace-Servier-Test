## imports
import pandas as pd

## fonctions

# Uniformisation des dates au format Datetime
# prend en argument le dataframe et la colonne (string) contenant la date
def date_datetime_rename(df,col):
    df.rename(columns={col: "date"}, inplace=True) #renomme la colonne en "date"
    df[col] = pd.to_datetime(df[col])

# Renomme les colonnes du titre de l'article et du journal
# prend en argument le dataframe et la colonne (string) contenant le titre de l'article 
def title_rename(df,col_title, col_journal):
    df.rename(columns={col_title: "title"}, inplace=True) #renomme la colonne en "title"
    df.rename(columns={col_journal: "journal"}, inplace=True) #renomme la colonne en "journal"

# Met chaîne de caractère en minuscule : afin d'uniformiser les mots à rechercher
# prend en argument le dataframe et la colonne (string) à mettre en minuscule
def string_lowercase(df,col):
    for i in range(len(df[col])):
        df[col][i] = df[col][i].lower()

# Retourne un dataframe avec pour une catégorie d'article, les mentions de chacune des drugs
# prend en argument une origine d'articles : pubmed ou clinical trials par exemple, et cette catégorie sous forme de string
def output_df(category,string_cat):
    info = [category["title"],category["journal"],string_cat]
    index = 0
    data = []
    output_col = ['drug', 'category', 'title', 'journal', 'date']

    for drug in drugs["drug"]:
        for art_title in info[0] :
            if drug in art_title :
                data.append([drug,info[2],art_title,category["journal"][index],category["date"][index]])
        index += 1

    return(pd.DataFrame(data, columns = output_col))
        
## lecture des données

drugs = pd.read_csv("data/drugs.csv")
pubmed = pd.read_csv("data/pubmed.csv")
pubmed_json = pd.read_json('data/pubmed.json')
clinical_trials = pd.read_csv("data/clinical_trials.csv")

# concaténation des 2 df pubmed
frames = [pubmed,pubmed_json]
pubmed = pd.concat(frames,ignore_index=True)

### Data pipeline

## data pre-processing

# uniformisation des dates, titres, et noms de colonnes
date_datetime_rename(pubmed,"date")
date_datetime_rename(clinical_trials,"date")
title_rename(pubmed,"title","journal")
title_rename(pubmed_json,"title","journal")
title_rename(clinical_trials,"scientific_title","journal")
string_lowercase(drugs,"drug")
string_lowercase(pubmed,"title")
string_lowercase(clinical_trials,"title")

## output
pubmed_output = output_df(pubmed,"pubmed")
clinical_trials = output_df(clinical_trials,"clinical_trials")
frames2 = [pubmed_output,clinical_trials]
result = pd.concat(frames2,ignore_index=True)

result_json = result.to_json(r'result.json')

# affichage du fichier JSON avec pandas
print(pd.read_json('result.json')) 