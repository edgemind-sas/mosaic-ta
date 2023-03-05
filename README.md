
# Table des matières

1.  [Contexte](#org88c0f39)
2.  [Objectifs](#orgab0a09d)
3.  [Axes de recherche](#org6d24c19)
    1.  [Formalisation et modélisation probabiliste](#org32a2afc)
    2.  [Analyse technique](#orga2f4b0c)
        1.  [Généralité](#org6d063ad)
        2.  [Indicateurs étudiés](#org771a176)
        3.  [Modèles décisionnels](#org717fac8)
        4.  [Backtesting](#org8a55124)
4.  [Références](#org1d962a0)



<a id="org88c0f39"></a>

# Contexte

Une crypto-monnaie est une monnaie virtuelle qui opère indépendamment des banques et des
gouvernements. La particularité des marchés de crypto-monnaies provient de sa décentralisation. Cela
signifie que ces monnaies ne sont pas émises par une autorité centrale (un État par exemple) mais
via des algorithmes exécutés sur un réseau informatique assurant leur cohérence et la sécurité des
transactions. Ces marchés évoluent en fonction de l’offre et de la demande, mais, s’agissant de
marchés décentralisés, ils sont souvent mieux protégés des changements économiques et politiques qui
impactent généralement les devises traditionnelles [1].  

Bien que le potentiel économique de ces nouvelles monnaies reste à évaluer, ces dernières offrent
déjà à certains pays en développement une alternative de financement plus fiable qu’une monnaie
traditionnelle gérée par des infrastructures bancaires ou des institutions étatiques
défaillantes. Toutefois, de part leur jeunesse, le comportement des marchés de crypto-monnaies
s’avère parfois très volatile. La gestion des risques de ces nouveaux actifs financiers apparaît
donc comme un enjeu socio-économique fort pour les prochaines années.  

Depuis 2014, la société EdgeMind développe des méthodes et des outils pour l’évaluation et la
prévision des risques industriels. Pour ce faire, EdgeMind met en œuvre différentes techniques de
machine learning et de simulation afin de modéliser le comportement dynamiques de systèmes complexes
et anticiper l’occurrence de situations indésirables en fonction de l’évolution des contextes
opérationnels. 

La société EdgeMind cherche aujourd’hui à diversifier son activité en abordant le domaine des
risques financiers, en se focalisant dans un premier temps sur les problématiques liées à l’analyse
des cryptomonnaies et à la gestion d’actifs algorithmiques. En effet, qu’il soit question
d’industrie ou de finance, les enjeux autour de la gestion d’actifs sont similaires, à savoir
prévoir l’évolution future du système d’actifs considéré et déterminer un ensemble d’actions
permettant d’agir sur ce système de manière à optimiser ses performances dans le temps. Par exemple,
la maintenance prévisionnelle (ou prédictive) est une manière de valoriser les données
opérationnelles afin d’optimiser la disponibilité d’un système d’actifs industriels. Dans la
finance, les algorithmes de trading font de même pour valoriser un portefeuille d’actifs [2]. Nous
souhaitons donc dans ce projet expérimenter une partie des méthodes d’analyses prédictives
développées pour la gestion des risques industriels sur le domaine des risques financiers.  

Par ailleurs, contrairement au secteur industriel, les données sur les principaux actifs financiers
sont disponibles à des niveaux d’échantillonnage élevés (de l’ordre de la seconde). Cette
spécificité est particulièrement intéressante pour l’élaboration d’algorithmes d’aide à la décision
auto-apprenants proches du temps réel, mais soulève dans le même temps de nombreux verrous
scientifiques et techniques 


<a id="orgab0a09d"></a>

# Objectifs

Ce projet a pour objectif général l’élaboration d’une IA autonome capable de :

1.  évaluer les risques liés à la gestion de crypto-actifs (e.g. crypto-monnaies), i.e. prévoir les
    performances futures des actifs sur un horizon temporel donné ;
2.  prendre des décisions visant à optimiser les performances d’un portefeuille de crypto-actifs ;
3.  s'auto adapter en “temps réel” en fonction de l’évolution de contexte économique et sociétal courant.


<a id="org6d24c19"></a>

# Axes de recherche


<a id="org32a2afc"></a>

## Formalisation et modélisation probabiliste

Qu’il s’agisse de prévoir l’évolution d’actifs traditionnels [3] [4], ou de crypto-monnaies
[5] [6] [7], les scientifiques travaillant sur l’élaboration de modèles probabilistes s’intéressent,
pour la plupart, aux approches dites paramétriques. Ceci s’explique principalement par la simplicité
de ces modèles et leur relative interprétabilité. En revanche, les approches paramétriques peinent à
correctement représenter les comportements extrêmes d’actifs volatiles. Des articles récents ont
montré l’intérêt des méthodes non-paramétriques afin de prévoir l’évolution du Bitcoin [8]
[9]. Ces modèles, plus complexes, semblent difficilement compatibles avec la prise en compte de
variables exogènes permettant d’expliquer le comportement des actifs considérés.   
Notre objectif est de lever la limitation précédente en proposant une approche non-paramétrique
discrète (la distribution des rendements des actifs est discrétisée). À notre connaissance, cette
approche n’a pas été expérimentée dans le cadre des cryto-actifs et possèdent l’avantage d’être
compatible avec des techniques de modélisation probabilistes pertinentes (e.g. techniques
bayésiennes) pour répondre à la problématique. 


<a id="orga2f4b0c"></a>

## Analyse technique


<a id="org6d063ad"></a>

### Généralité

Dans le domaine de l’analyse des marchés financiers, l'analyse technique correspond à un ensemble
d'outils dont le but est de prédire les rendements futurs des actifs financiers en étudiant
l’historique des données de marché disponibles, principalement le cours et le volume des actifs
considérés [10].  Dans l’article de revue de littérature sur l’analyse technique [11], les auteurs
listent les principales méthodologies d’analyses mises en œuvre depuis une cinquantaine d’années.  
La grande majorité des méthodologies présentées reposent sur la construction d’indicateurs
particuliers jugés pertinents par leurs auteurs (e.g. [12], [13]). Toutefois, l’évaluation de ces
indicateurs n’est réalisée que sur la base de backtesting empiriques sur des périodes choisies
arbitrairement et relativement courtes lorsqu’il s’agit d’analyse intra-journalière.  
Comme les auteurs de l’article [11], nous partageons le constat que l’évaluation des performances de
l’analyse technique nécessite une consolidation mathématique. Pour ce faire, nous proposons de
développer une [stratégie d’évaluation des indicateurs techniques innovante](indicator_analysis.md) fondée sur l’analyse de
la distribution conditionnelle des rendements par rapport aux indicateurs observés.


<a id="org771a176"></a>

### Indicateurs étudiés

-   [Marteau généralisé](indic/indic_gh.html)
-   [Niveau de volume mobile](indic/indic_mvl.html)


<a id="org717fac8"></a>

### Modèles décisionnels


<a id="org8a55124"></a>

### Backtesting

-   Construire un environnement de backtesting comparable à une plateforme d'échanges
-   Évaluer les performances du prototype sur l'environnement de backtesting.
-   Réaliser des expérimentations "à blanc" en temps réel sur différentes périodes : 1 heure, 12 heures, 24 heures, 2 jours, une semaine.


<a id="org1d962a0"></a>

# Références

[1]A. Stachtchenko, “Manuel de survie dans la jungle des poncifs anti-Bitcoin (version longue),” Medium. Jan. 2022. Accessed: Feb. 08, 2022. [Online]. Available: <https://medium.com/@AlexStach/manuel-de-survie-dans-la-jungle-des-poncifs-anti-bitcoin-version-longue-523e381745ff>

[2]D.-Y. Park and K.-H. Lee, “Practical Algorithmic Trading Using State Representation Learning and Imitative Reinforcement Learning,” Ieee access, vol. PP, p. 1, Nov. 2021, doi: 10.1109/ACCESS.2021.3127209.

[3]J. Shen, A Stochastic LQR Model for Child Order Placement in Algorithmic Trading. 2020.

[4]D. Snow, “Machine Learning in Asset Management - Part 1 : Portfolio Construction - Trading Strategies,” The journal of financial data science, vol. 2, no. 1, pp. 10–23, Jan. 2020, doi: 10.3905/jfds.2019.1.021.

[5]E. Bouri, C. K. M. Lau, B. Lucey, and D. Roubaud, “Trading volume and the predictability of return and volatility in the cryptocurrency market,” Finance research letters, vol. 29, pp. 340–346, Jun. 2019, doi: 10.1016/j.frl.2018.08.015.

[6]N. Crone, E. Brophy, and T. Ward, Exploration of Algorithmic Trading Strategies for the Bitcoin Market. 2021.

[7]P. Hansen, C. Kim, and W. Kimbrough, Periodicity in Cryptocurrency Volatility and Liquidity. 2021.

[8]M. Balcilar, E. Bouri, R. Gupta, and D. Roubaud, “Can volume predict Bitcoin returns and volatility? A quantiles-based approach,” Economic modelling, vol. 64, pp. 74–81, Aug. 2017, doi: 10.1016/j.econmod.2017.03.019.

[9]I. Jiménez, A. Mora-Valencia, and J. Perote, “Semi-nonparametric risk assessment with cryptocurrencies,” Research in international business and finance, vol. 59, p. 101567, Jan. 2022, doi: 10.1016/j.ribaf.2021.101567.

[10]R. Yamamoto, “Intraday technical analysis of individual stocks on the Tokyo Stock Exchange,” Journal of banking & finance, vol. 36, no. 11, pp. 3033–3047, Nov. 2012, doi: 10.1016/j.jbankfin.2012.07.006.

[11]R. T. Farias Nazário, J. L. e Silva, V. A. Sobreiro, and H. Kimura, “A literature review of technical analysis on stock markets,” The quarterly review of economics and finance, vol. 66, pp. 115–126, Nov. 2017, doi: 10.1016/j.qref.2017.01.014.

[12]A. Hassanniakalager, G. Sermpinis, and C. Stasinakis, “Trading the foreign exchange market with technical analysis and Bayesian Statistics,” Journal of empirical finance, vol. 63, pp. 230–251, Sep. 2021, doi: 10.1016/j.jempfin.2021.07.006.

[13]D. Bao and Z. Yang, “Intelligent stock trading system by turning point confirming and probabilistic reasoning,” Expert systems with applications, vol. 34, no. 1, pp. 620–627, Jan. 2008, doi: 10.1016/j.eswa.2006.09.043.

