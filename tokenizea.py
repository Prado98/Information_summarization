''' -*- coding: utf-8 -*-

text = raw_input("Enter the text to do the preprocessing : ")
text = "this's a sent tokenize test. this is sent two. is this sent three? sent 4 is cool! Now it's your turn."'''
#import csv
import os
import pandas as pd
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk import pos_tag
from nltk.corpus import stopwords
import string
from collections import Counter

stop_words = set(stopwords.words('english'))
text = pd.read_csv('C:\pyproject\python_dataset.csv')

rec_no = int(raw_input("Enter the record number to summarize: "))
text = text.ix[rec_no,0:6].ctext
print text
os.system('PAUSE')
#Cleaning the data!

# prepare a translation table to remove punctuation
#table = str.maketrans(str.punctuation, '')
# remove punctuation from each token
#text = text.translate(table)
text = text.replace(string.punctuation,"")
#tokenize on white space
text = text.split()
print "\n\n"
os.system('PAUSE')
# convert to lower case
text = [word.lower() for word in text]

# remove tokens with numbers in them
text = [word for word in text if word.isalpha()]

#stringify text so we can use sent_tokenize
text1 = ' '.join(text)

#remove duplicates
text1 = text1.split(" ")
for i in range(0, len(text)):
    text1[i] = "".join(text1[i])
UniqW = Counter(text1)
s = " ".join(UniqW.keys())
text = s
print('without duplicates: ',text)
print "\n\n"
os.system('PAUSE')
#Sentence tokenize
sent_tokenize_list = sent_tokenize(text)

postag = []
word_tokenize_list = []
print(sent_tokenize_list)
print "\n\n"
os.system('PAUSE')

#Word tokenize from the sentences and pos taggins
for i in sent_tokenize_list :
   word_tokenize_list.append(word_tokenize(i))
   postag.append(pos_tag(i))
print("\n\npostag :", postag)
print "\n\n"
os.system('PAUSE')
print("\n\nThis is the word tokenize list :",word_tokenize_list)
print "\n\n"
os.system('PAUSE')

stop_words = (list(stop_words))
#stop_words1 = []
stop_words = [str(stop_words[x]) for x in range(len(stop_words))]
#for i in stop_words:
    #print i
    #stop_words1.append(i[0::])
    #stop_words1.append(''+i+'')
#stop_words1.append('.')
print("\n\n\nMy Stop words :",str(stop_words))
print "\n\n"
os.system('PAUSE')

#print "Stop words",stop_words1
#Removing stop words
#filtered_sentence = [w for w in word_tokenize_list if not w in stop_words]
filtered_sentence = []
print "The removed words are :"
for a in word_tokenize_list:
    for w in a:
		if w not in stop_words:
 	       #print "Inside if"
			filtered_sentence.append(w)
 	       #print(w)
		else:
			print w," ",
print "\n\n"
os.system('PAUSE')
#final pre-processed data
print("\n\n\nThe filtered sentence : ",filtered_sentence)
#print "\n\n"
#os.system('PAUSE')
