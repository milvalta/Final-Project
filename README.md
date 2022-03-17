Computational Literacy 2021: The Final Project


1. The aim of the project

Proverbs are an important form of cultural expression of a society. They are simple and concrete sayings that express truths based on common sense or the practical experience of humanity. They also differ from ordinary language as they are a part of oral history. Proverbs are used in seasoning speech, to entertain, to get comfort or show power of tradition (Lauhakangas, 2018). Because proverbs have the figurative meaning instead of literal, for NLP research, they often represent a challenge. In machine translation, the quality might be affected by lack of adequate processing. Identifying proverbs is an important subtask in computer sciences: Any NLP system will make mistakes in translation if it does not have knowledge of non compositional (...) proverbs (Garg & Goyal, 2014). 
Instead of identifying proverbs, this paper focuses on studying them. My aim is to try and implement computational methods to humanities data and experiment with distant reading. 
I study a Finnish proverb collection digitized by the Finnish Language Bank Kielipankki. My aim is to examine the themes in the proverbs by analyzing word frequencies and identify a basis for further analysis. 
The data used in this study consists of 85,974 text entries of proverbs collected from various areas in the 1930s. The collection includes proverbs written both in standard Finnish and in dialect. Adding to this, also the names of the collectors and the place and the year of collecting the proverbs are recorded in the set. For reasons explained further, the data used in this study includes only the standard language proverbs. 

My humanities research question is: 

What are the most popular topics in a set of digitized Finnish proverbs?  


2. Data

The data used in this paper consists of short sentences in Finnish language in text form. 
The list of these sentences are recorded in CSV format. 
The Kielipankki Finnish proverb collection contains 85,974 text entries of dialectal proverbs collected from various areas in the 1930s. This is only a part of the 1.4 million proverbs collected in different regions of Finland. 
The proverbs in the set are recorded both in dialect Finnish and in standard Finnish. Each proverb comes with information about the year and place of collecting, and the name of the collector. 
There are certain inherent biases in the set. We cannot know why particular proverbs are collected or what are left out. Many of the proverbs appear in the set more than once. The set is not a random sample of all of the collected entries, and does not represent all Finnish proverbs or the whole collection. The digitized part of the collection consists of proverbs written down in the 1930s around the country and so the collection should only represent itself. This is why it's impossible to draw any definite conclusions on, for example, the Finnish proverbs in general or the Finnish culture in the 1930s. 


3. Methods

Originally the plan was to employ topic modeling. However, it turned out that the proverbs are not suitable material for this kind of method as they are merely short sentences that contain too little information to form coherent topics. Afterwards it seems obvious that topic modeling would have been far beyond my capabilities as a programmer, as my experience with programming is nonexistent. 
To find "popular topics" in the proverbs, I decided to work with word frequency analysis, to extract the most frequent words and then analyze them using close reading. 
I ended up processing the data twice, first with a ready-made tool Voyant and then with Python and NLTK. Adding to this, I made an attempt to clean the data with OpenRefine, with little success, and ended up using the program to strongly simplify the dataset. 
This resulted into two sets of results that are compared and analyzed further. 
The next chapter explains the struggle in detail. 

3.1. Processing the data: The first attempt  

The first step was to upload the data into Voyant. It became immediately clear that preprocessing the data is crucial. Unsurprisingly the biggest words appearing in the word cloud created by Voyant were noise and metadata: conjunctions, years in which the proverbs have been collected, names of the collectors and places the proverbs are collected from. 
To get rid of the least meaningful words, I first applied a Finnish stopword list (found here). This removed a big chunk of the noise. To remove the metadata, to the existing stopwords list I added certain names and numbers (list in Appendix).
It turned out that Voyant is not optimal to preprocess the data. The tool is built for visualizing the data and not for cleaning it. This resulted in significant shortcomings in the cleaning of the data. Same proverbs appeared multiple times, written both in standard Finnish and in dialect, and I caused possible problems by adding insignificant words to the stopwords randomly, as they rose from the set. 
To enhance the reliability of the results, I created another dataset consisting only of the standard Finnish proverbs. This set does not include any metadata: the names, years, places and also the proverbs recorded in dialect were removed from the set with OpenRefine. Removing all but the standard Finnish proverbs eliminated both the context of the sentences, and the possibility of further study on, for instance, comparing regional differences. Creating this set was a major shortcut, but I ended up using it for this paper nevertheless. This kind of simple data set made it easier to focus on the research question as it minimized the risk of unknowingly biasing the data by cleaning it without fully understanding the process. 
In comparison to the data cleaned with Voyant, the simplified set only includes 604,072 total words and 60,636 unique word forms, whereas the first dataset included 1,666,563 total words and 130,329 unique word forms. 
The most frequent words were also notably different. In the first corpus, the most frequent words were: mies (3353); syö (2183); koira (2065); paha (2056); sika (2031).
In the second one, the most frequent words are: älä (2296); tulee (2225); hyvä (2018); saa (1933); mies (1783). 

3.1. Processing the data: The second attempt  

Working with Voyant is likely to affect the reliability of the results, since it's not possible to really know how the tool analyzes the data. 
To create a more transparent dataset, I made an attempt to clean up and analyze the data using Python. I continued using the simplified data consisting only of the standard language proverbs.
The steps I took to create the second dataset were: 

importing the relevant packages; re, ntlk, matplotlib, 
cleaning the data, removing non-alphabetical characters using Python and regular expressions & turning the text into lowercase
creating a wordlist
tokenizing 
removing stopwords: finnish stop word list found in NLTK 
calling for the 20 most frequent words and creating a graph using matplotlib 


In addition to this, I tried and played a bit with NLTK and managed to create a lexical dispersion plot: 

As well as a Python-generated proverb: 

loukosta ', ' kauppa ', ' tÃ ¤ nne ', ' ohrankylvÃ ¶ Ã ¶ n ', ' taitaa
', ' saa ', ' vilu ', ' hiisi ', ' tahdot ', ' vÃ ¤ litÃ ¤', ' tulee
', ' eikÃ ¤', ' helmallinen ', ' korsi ', ' lestissÃ ¤ Ã ¤', ' pitÃ ¤
Ã ¤ n ', ' parempi ', ' suoloja ', ' kyllÃ ¤', ' vierestÃ ¤', ' pÃ ¤ Ã
¤ lÃ ¤ kÃ ¤ y ', ' kauan ', ' hessu ', ' punikki - vainajan ', ' Ã ¤
tÃ ¶


4. Analysis

In the first set, that is cleaned and processed with Voyant, the most frequently used word is "mies" ("a man"). It has been used 3353 times. 
After "mies", the most popular terms are "syö", "koira", "paha", "sika", "pois" and "akka". 
In the second set, processed with Python and NLTK, the most frequent word is "sanoi" ("said"). Other frequently used words are "kyllä", "eikä", "älä", "tulee", "hyvä", "saa", "mies", "ennen", "syö". Many of these words might be considered as filler words that have no substantial value. If the words "kyllä", "eikä" and "älä" would be added to the stopword list and ignored in this analysis, the list of the top words in the dataset 2 would  significantly resemble the first one. This is to conclude that the results verify each other. 
Based on the results, the word "mies" appears in high frequency in the proverbs. In both data, a man seems to be the usual operator: the protagonist in folklore or at least its subject. 
There is likely something to be said about the fact that men, dogs and pigs appear in the proverbs far more often than, for instance, women (that are referred with the word "akka", hag). Analyzing the gendered language of these proverbs gives grounds to future research. 

To get a better idea of the man in the proverbs, they can be explored with Korp. 
Some examples of the proverbs with a word "mies":
Ei sota yhtä miestä kaipaa.
Ei se ole mies	eikä mikään, joka ei tohdi omiin housuihinsa paskantaa.
Ei työ miestä pahenna jos ei mies työtä.
Aamurusko on miehen tuska. 
Sanasta miestä, sarvesta härkää.
Puuro miehen tiellä pitää.
Most of these sentences seem to relate to gender: they comment and recreate the expectations towards men and in this sense, they are performative. However, in some proverbs the man seems to be acting as a synonym to "human". In English, this conclusion would be quite obvious since the word "man" is often used when referring to individual people or the "mankind". But in Finnish, the words human and man are not interchangeable, and so this tendency might be worth further exploration. 
Another frequent word in both sets is "koira". This is fitting, since dog is a man's best friend. The popularity of dog-related proverbs indicate that dogs have been very important companions for humans. 
Papin leski on niin kuin kalamiehen koira.
Se koira se älähtää, johonka kalikka kalahtaa.
Kyllä koira kusee, kun kannon löytää.
Ei se koira pure, joka haukkuu.
Based on the most frequent words, it seems like the biggest themes of the proverbs in this collection are associated with rural life. 
One interesting topic for future DH research could be studying the different purposes of proverbs in the collection, using the categories by Lauhakangas (2018). How many of the proverbs fall into the category of "Power of tradition","Resolving conflicts" and "Feeling of togetherness"? 

5. Potential bias and problems

As already mentioned, there are biases both in the data and in processing it. The code used in processing the data with Python is clumsy and incomplete and might cause some problems I'm not even aware about. 
In addition to this, the analysis is also likely to be flawed. Without any expertise in history, linguistics or folkloristics, my abilities to interpret and analyze proverbs is quite limited. Even if I got some kind of an answer to the research question, I suspect that my attempts at distant and close reading were left quite shallow. 
For trustable analysis, the research should be done in collaboration with multiple fields ranging from computer science to history and linguistics. 

Appendix: My stopwords

alatornio
eno
evijärvi
hailuoto
hausjärvi 
isokyrö
joutseno
juva
kalanti
kiuruvesi
kivennapa
kuhmoinen
kurkijoki
laukaa
loimaa
nivala
nummi
pälkäne
paltamo
riistavesi
rovaniemi
ruovesi
tyrvää
ulvila
valkeala
1930
1931
1932
1933
1934
1935
1936
1937
1938
1939
