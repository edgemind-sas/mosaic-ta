
# Table des matières

1.  [Contexte](#orgedfdde8)
2.  [Objectifs](#org75368f2)
3.  [Axes de recherche](#org18e3774)
    1.  [Formalisation et modélisation probabiliste](#org434e715)
    2.  [Analyse technique](#org7bba7b1)
        1.  [Généralité](#orgd500f5f)
        2.  [Indicateurs étudiés](#org16117db)
    3.  [Modèles décisionnels](#org0080b32)
    4.  [Backtesting](#org8e3f5ae)
4.  [Références](#org58b841a)



<a id="orgedfdde8"></a>

# Contexte

Une crypto-monnaie est une monnaie virtuelle qui opère indépendamment des banques et des
gouvernements. La particularité des marchés de crypto-monnaies provient de sa décentralisation. Cela
signifie que ces monnaies ne sont pas émises par une autorité centrale (un État par exemple) mais
via des algorithmes exécutés sur un réseau informatique assurant leur cohérence et la sécurité des
transactions. Ces marchés évoluent en fonction de l’offre et de la demande, mais, s’agissant de
marchés décentralisés, ils sont souvent mieux protégés des changements économiques et politiques qui
impactent généralement les devises traditionnelles <stachtchenko_manuel_2022>.  

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
finance, les algorithmes de trading font de même pour valoriser un portefeuille d’actifs <park_practical_2021>. Nous
souhaitons donc dans ce projet expérimenter une partie des méthodes d’analyses prédictives
développées pour la gestion des risques industriels sur le domaine des risques financiers.  

Par ailleurs, contrairement au secteur industriel, les données sur les principaux actifs financiers
sont disponibles à des niveaux d’échantillonnage élevés (de l’ordre de la seconde). Cette
spécificité est particulièrement intéressante pour l’élaboration d’algorithmes d’aide à la décision
auto-apprenants proches du temps réel, mais soulève dans le même temps de nombreux verrous
scientifiques et techniques 


<a id="org75368f2"></a>

# Objectifs

Ce projet a pour objectif général l’élaboration d’une IA autonome capable de :

1.  évaluer les risques liés à la gestion de crypto-actifs (e.g. crypto-monnaies), i.e. prévoir les
    performances futures des actifs sur un horizon temporel donné ;
2.  prendre des décisions visant à optimiser les performances d’un portefeuille de crypto-actifs ;
3.  s'auto adapter en “temps réel” en fonction de l’évolution de contexte économique et sociétal courant.


<a id="org18e3774"></a>

# Axes de recherche


<a id="org434e715"></a>

## Formalisation et modélisation probabiliste

Qu’il s’agisse de prévoir l’évolution d’actifs traditionnels <&shen_stochastic_2020> <&snow_machine_2020>, ou de crypto-monnaies
<&bouri_trading_2019> <&crone_exploration_2021> <&hansen_periodicity_2021>, les scientifiques travaillant sur l’élaboration de modèles probabilistes s’intéressent,
pour la plupart, aux approches dites paramétriques. Ceci s’explique principalement par la simplicité
de ces modèles et leur relative interprétabilité. En revanche, les approches paramétriques peinent à
correctement représenter les comportements extrêmes d’actifs volatiles. Des articles récents ont
montré l’intérêt des méthodes non-paramétriques afin de prévoir l’évolution du Bitcoin <&balcilar_can_2017>
<&jimenez_semi-nonparametric_2022>. Ces modèles, plus complexes, semblent difficilement compatibles avec la prise en compte de
variables exogènes permettant d’expliquer le comportement des actifs considérés.   
Notre objectif est de lever la limitation précédente en proposant une approche non-paramétrique
discrète (la distribution des rendements des actifs est discrétisée). À notre connaissance, cette
approche n’a pas été expérimentée dans le cadre des cryto-actifs et possèdent l’avantage d’être
compatible avec des techniques de modélisation probabilistes pertinentes (e.g. techniques
bayésiennes) pour répondre à la problématique.

Par ailleurs, nous introduisons certaines [notions fondamentales](notions_bases.md), notamment autour du calcul des
rendements, qui serviront de base commune aux dévelppements ultérieurs.


<a id="org7bba7b1"></a>

## Analyse technique


<a id="orgd500f5f"></a>

### Généralité

Dans le domaine de l’analyse des marchés financiers, l'analyse technique correspond à un ensemble
d'outils dont le but est de prédire les rendements futurs des actifs financiers en étudiant
l’historique des données de marché disponibles, principalement le cours et le volume des actifs
considérés <&yamamoto_intraday_2012>.  Dans l’article de revue de littérature sur l’analyse technique <&farias_nazario_literature_2017>, les auteurs
listent les principales méthodologies d’analyses mises en œuvre depuis une cinquantaine d’années.  
La grande majorité des méthodologies présentées reposent sur la construction d’indicateurs
particuliers jugés pertinents par leurs auteurs (e.g. <&hassanniakalager_trading_2021>, <&bao_intelligent_2008>). Toutefois, l’évaluation de ces
indicateurs n’est réalisée que sur la base de backtesting empiriques sur des périodes choisies
arbitrairement et relativement courtes lorsqu’il s’agit d’analyse intra-journalière.  
Comme les auteurs de l’article <&farias_nazario_literature_2017>, nous partageons le constat que l’évaluation des performances de
l’analyse technique nécessite une consolidation mathématique. Pour ce faire, nous proposons de
développer une [stratégie d’évaluation des indicateurs techniques innovante](indicator_analysis.md) fondée sur l’analyse de
la distribution conditionnelle des rendements par rapport aux indicateurs observés.


<a id="org16117db"></a>

### Indicateurs étudiés

-   [Marteau généralisé](indic/indic_gh.md)
-   [Niveau de volume mobile](indic/indic_mvl.md)
-   [RSI](indic/indic_rsi.md)
-   [*Support Range Index*](indic/indic_sri.md)


<a id="org0080b32"></a>

## Modèles décisionnels


<a id="org8e3f5ae"></a>

## Backtesting

[Documentation sur la partie backtesting](.backtests/backtests.md).


<a id="org58b841a"></a>

# Références

<MOSAIC.bib>

