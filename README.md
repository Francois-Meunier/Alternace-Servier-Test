# Test Servier - Alternance

- [Python](#python)
- [SQL](#sql)

## Python


### Explication démarche


### Traitement ad-hoc


### Pour aller plus loin


## SQL


### Première partie du test

Requête : 
```
SELECT DATE_FORMAT(date,'%d/%m/%Y') AS date, ROUND(SUM(prod_price*prod_qty)) AS ventes
FROM TRANSACTIONS
WHERE date BETWEEN '2020-01-01' AND '2020-12-31' 
GROUP BY date
```

### Seconde partie du test

