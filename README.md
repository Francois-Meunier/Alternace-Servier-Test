# Test Servier - Alternance

- [Python](#python)
- [SQL](#sql)

## Python


### Explication démarche

> fichier datapipeline.py

La sortie de la data pipeline est un fichier qui donne des informations sur les médicament : dans quel type de revue ils ont été mentionnés (Pubmed ou Clinical trials par exemple), le titre de l'article, le nom du journal, ainsi que la date.<br>
J'ai donc imaginé la strucutre du fichier de sortie comme un tableau de 5 colonnes : 
- drug : nom du médicament
- category : le type de revue (base de donnée)
- title : titre de l'article
- journal : le nom du journal
- date : la date<br>
<br>
Et donc une ligne est ajoutée à chaque fois qu'un médicament est mentionné, comprenant toutes les informations.<br>
La règle est la suivante : un médicament est mentionné dans un artcile si il est présent dans le titre.<br>
Donc pour chaque type de revue, on vérifie si le nom du médicament est présent dans le titre de chaque article. Si c'est le cas, on récupère 3 choses : le nom du médicament, le titre de l'article, le nom du journal, ainsi que la date.<br>
<br>
Afin de vérifier si un médicament est présent dans un article, j'ai utilisé if "mot" in "phrase". Mais les majuscules sont prise en compte.<br>
J'ai tout d'abord uniformisé les données.<br>
En renommant les nom de colonnes des dataframes, pour plus de simplicité, en uniformisant les dates (au format Datetime), et en mettant les noms des médicaments et les titres des articles en minuscule.<br>
<br>
Ensuite la fonction output_df(category,string_cat) reprend le raisonnement expliqué ci-dessus.<br>
On concatène les dataframes obtenus par catégorie de revue et on le met en JSON.<br>
<br>
Toutes les fonctions sont commentées dans le code.<br>

### Traitement ad-hoc

> fichier adhoc.py

Le but est d'avoir le nom du journal qui mentionne le plus de médicaments différents.<br>
En parcourant le dataframe, j'ai incrémenté un compteur de nombre de médicaments différents, pour chaque journal, puis il reste le max à retourner.<br>
<br>
N.B. Pour la partie python, j'ai laissé dans le répository le Jupyter Notebook dans lequel j'ai fais mes tests.<br>

### Pour aller plus loin

- Quels sont les éléments à considérer pour faire évoluer votre code afin qu’il puisse gérer de grosses volumétries de données (fichiers de plusieurs To ou millions de fichiers par exemple) ?
<br>
- Pourriez-vous décrire les modifications qu’il faudrait apporter, s’il y en a, pour prendre en considération de telles volumétries ?
<br>

## SQL


### Première partie du test

Dans l'échantillon de de la table TRANSACTION, la date est au format dd/mm/yy, alors que dans
l'extrait du résultat de la requête le format est dd/mm/yyyy. Les dates ne pouvant être stockées
dans une base de donnée SQL que selon le format suivant : yyyy-mm-dd, j'en ai déduis qu'il fallait affichier.<br>
la date avec DATE_FORMAT() et la synthaxe '%d/%m/%Y'. C'est le format '%d/%m/%y qui a été utilisé pour l'échantillon de l'énoncé.<br>
Pour la période j'ai utilisé BETWEEN qui fonctionne bien dans ce cas.<br>
Les ventes sont arrondies à l'unité, j'ai donc utilisé ROUND()<br>

Requête : 
```
SELECT DATE_FORMAT(date,'%d/%m/%Y') AS date, ROUND(SUM(prod_price*prod_qty)) AS ventes
FROM TRANSACTIONS
WHERE date BETWEEN '2020-01-01' AND '2020-12-31' 
GROUP BY date
```

### Seconde partie du test

La jointure à faire est une jointure externe, LEFT JOIN avec la table TRANSACTION.<br>
Afin de faire la différence entre les ventes de meuble et de déco, j'ai utilisé deux CASE.<br>
Le résultat est groupé sur l'id client, par ordre décroissant.<br>

Requête :
```
SELECT client_id, SUM(CASE WHEN product_type='MEUBLE' THEN prod_qty*prod_price END) as ventes_meuble, SUM(CASE WHEN product_type='DECO' THEN prod_qty*prod_price END) as ventes_deco 
FROM transactions LEFT JOIN product_nomenclature ON transactions.prop_id = product_nomenclature.product_id 
WHERE date BETWEEN '2020-01-01' AND '2020-12-31'
GROUP BY client_id DESC
```