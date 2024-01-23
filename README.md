Abstract:
This project implements the combination of Redis and Python to store and visualize performance data for tracking. Using Redis as a database management system, I extracted daily sales prices from a home property sales dataset, then aggregated and stored them in Redis. Then, I calculated daily, monthly, and yearly revenue from the stored data, providing a clear understanding of financial performance over different times. I created a web application that facilitates the comprehension of revenue trends and fluctuations over time. This project demonstrates how to harness the fast storage and data processing capabilities of Redis along with Python's computation and visualization abilities for efficient revenue analysis.

Résumé:
Ce projet met en œuvre la combinaison de Redis et Python pour stocker et visualiser les données de performances afin de les suivre. En utilisant Redis comme un système de gestion de base de données, nous avons extrait les prix des ventes quotidiennes à partir d'un dataset de ventes de propriétés de maison, puis nous les avons regroupés et stockés dans Redis. Ensuite, nous calculons les revenus quotidiens, mensuels et annuels à partir des données stockées, ce qui permet d'obtenir une vision claire des performances financières sur différentes périodes. Nous avons créé une application web qui facilite la compréhension des tendances et des variations des revenus au fil du temps. Ce projet démontre comment combiner les fonctionnalités de stockage rapide et de traitement de données de Redis avec les capacités de calcul et de visualisation de Python pour une analyse efficace.

I. Introduction
Le suivi des performances est un aspect crucial de la gestion efficace d'une entreprise. Il permet d'évaluer les résultats, d'identifier les domaines d'amélioration et de prendre des décisions éclairées pour optimiser les opérations. Dans le cadre de ce projet, je propose de développer un système de suivi des performances en utilisant une base de données NoSQL. Je vais mettre en place un modèle de données adapté aux besoins de suivi des performances, en identifiant les métriques clés et les relations entre les entités. Je vais ensuite utiliser les fonctionnalités de la base de données NoSQL pour collecter, stocker, interroger et analyser les données de performances de manière efficace.

II. Processus du projet
Dans ce projet, j'ai utilisé un dataset de ventes de maisons par jour, et à partir d'elle, j'ai extrait les données que j'ai travaillées pour obtenir les données de performance. Lorsque les données sont prêtes, j'utilise Python pour les stocker dans Redis sous forme d'un hachage qui prend les jours comme des clés et les différentes ventes comme une valeur sous forme d'un objet JSON avec l'ID de vente comme une clé et le prix comme une valeur de cette clé. Ensuite, j'ai calculé les revenus quotidiens, mensuels et annuels qui vont être les données de performance que je stocke dans Redis. Ces données seront de type clé/valeur, avec la clé pouvant être un jour, mois ou année, et la valeur comme le revenu quotidien, mensuel ou annuel. Ce processus permet une meilleure analyse des performances financières grâce à la manipulation et à la visualisation des données avec Redis.

![image](https://github.com/KhadijaHdd/performance-monitoring-systems-NoSQL/assets/108769529/a4b65864-899b-4302-b592-59282f2b2e34)

III. Explication du dataSet
J'ai accumulé des données sur les ventes immobilières pour la période 2007-2019 pour une région spécifique. Les données contiennent les prix de vente des maisons et des unités de 1, 2, 3, 4, 5 chambres. Ce sont les variables interdépendantes. Les données peuvent être résumées comme suit : 
- Date de vente
- Prix
- Type de propriété : unité ou maison
- Nombre de chambres : 1,2,3,4,5 (ce sont les multivariables que nous ciblons)
- Code postal à 4 chiffres (à titre indicatif uniquement, nous ne nous attendons pas à ce que ce point de données soit utile)

V. Résultat
Mon application Flask utilise Redis pour récupérer les données et les afficher dans une page web. J'importe les modules Flask, render_template, redis et json pour créer une instance de l'application Flask qui récupère à partir de Redis les données de performance qui sont dans mon affichage "les revenus annuels de ventes". La capture d'écran suivante illustre mon affichage (tableau de bord).

![image](https://github.com/KhadijaHdd/performance-monitoring-systems-NoSQL/assets/108769529/fe0c489f-5615-4b8a-8365-0945141102cc)
