# 4NL3-Course-Assignment-1
Assignment 1 for Natural Language Processing

Project structure
- normalize-text.py #main script for text normalization and token counting
- plot.py #Script for generating plots from output data
- plot.png #Bar plot of most frequent and least frequent words
- myfile.txt #Input text file
- counts.txt #Output text file

To run the normalization script:

python normalize-text.py myfile.txt -lowercase -stem -o counts.txt

Available Options
-lowercase	Convert all text to lowercase
-stem	Apply rule-based stemming
-lemmatize	Apply simple lemmatization
-stopwords	Remove common stopwords
-myopt	Remove accented characters

To generate plots:
- python plot.py counts.txt --output plot.png