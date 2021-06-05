## imports
import pandas as pd

# fonction permettant de retourner le nom du journal qui mentionne le plus de médicaments différents
# prend en paramètre le nom du fichier json (produit par la data pipeline) sous forme de string
def most_drug_journal(json_file) :
    
    df = pd.read_json(json_file)
    
    journal_list = df["journal"].unique() # liste des journaux
    drug_count = [] # nombre de drugs différents

    for i in range(len(journal_list)):
        drug_count.append(len(df[df["journal"] == journal_list[i]]["drug"].unique()))

    return(journal_list[drug_count.index(max(drug_count))])

print(most_drug_journal("result.json"))