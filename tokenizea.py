''' -*- coding: utf-8 -*-'''

#import csv
import pandas as pd
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.tag import pos_tag
from nltk.corpus import stopwords
from decimal import Decimal

stop_words = set(stopwords.words('english'))


def sentence_length(m, sentence):
    n_sentence = len(sentence.split(' '))
    return round(n_sentence/m, 3)


def title_feature(sentence, hd):
    tf = []
    for h in hd:
        i = 0
        if h in sentence.split():
            tf.append(sentence[i])
        i += 1

def sentence_pos(pos, sent, end):
    if(pos==0 or sent == end):  #len_sentence: should be last sentence
        return 1
    else:
        return 0
            

def proper_nouns(sentence):
    tagged_sent = pos_tag(sentence.split())
    l = len(sentence.split())
    proper_nouns = [word for word,pos in tagged_sent if pos == 'NNP']
    print(proper_nouns)
    pn = len(proper_nouns)/l
    return round(pn, 3)


#text = input("Enter the text to do the preprocessing : ")
text = pd.read_csv(r"C:\pyproject\ourdataset.csv", error_bad_lines=False)
head = text['Heading']
rec_no = int(input("Enter the record number to summarize: "))
text = text.ix[rec_no,0:5].Article 
text1 = text.split('.')


#Stopword removal
stop_words = set(stopwords.words('english'))
word_tokens = word_tokenize(text)
filtered_sentence = [w for w in word_tokens if not w in stop_words]
filtered_sentence = []
for w in word_tokens:
    if w not in stop_words:
        filtered_sentence.append(w)
filtered_sentence = ' '.join(filtered_sentence)
    
#print('\n\n')
#print('\n\nAfter stopword removal, text looks like this: \n\n', filtered_sentence)

#Sentence segmentation
sent = filtered_sentence.split('.')
print('\n\n')

#create feature matrix using empty dataframe
feature_matrix = pd.DataFrame()

#Title Feature
len_head = len(head)
tf = []
hd = head[rec_no].split(' ')
for i in range(0, len(sent)):
    title_feature(sent[i], hd)


    
#Sentence length
l = []
sl = []
for i in range(0, len(sent)):     #to find max length sentence
    l.append(len(sent[i].split()))
max_length = max(l)
for i in range(0, len(sent)):
    sl.append(sentence_length(max_length, sent[i]))



#Sentence Position
sp = []
r = sent[::-1]
for i in range(0, len(sent)):
    sp.append(sentence_pos(i, sent[i], r[0]))

    
#Proper Nouns
list_pn = []
for i in range(0, len(sent)):
    list_pn.append(proper_nouns(sent[i]))

feature_matrix = pd.DataFrame({'Sentence Length': sl, 'Sentence Position': sp, 'Proper Nouns': list_pn})
print(feature_matrix)


#classification
sl_value = []
avg = sum(sl)/float(len(sl))
mini = min(sl)
maxi = max(sl)
for i in range(0, len(sl)):
    if (sl[i] <= avg and sl[i] >= mini):
        sl_value.append('l')
    elif (sl[i] >= avg and sl[i] <= maxi):
        sl_value.append('h')

sp_value = []
for i in sp:
    if sp[i] == 1:
        sp_value.append('h')
    else:
        sp_value.append('l')

pn_value = []
avg = sum(list_pn)/float(len(list_pn))
mini = min(list_pn)
maxi = max(list_pn)
for i in range(0, len(list_pn)):
    if (list_pn[i] <= avg and list_pn[i] >= mini):
        pn_value.append('l')
    elif (list_pn[i] >= avg and list_pn[i] <= maxi):
        pn_value.append('h')


#class
class_list = []
for i in range(0, len(sent)):
    if ((sl_value[i] == 'h' and sp_value[i] == 'h' and pn_value[i] == 'h') or (sl_value[i] == 'h' and pn_value[i] == 'h')):
        class_list.append('I')
    else:
        class_list.append('NI')


#summary
summary = []
summary.append(text1[1])
for i in range(2, len(text1)-1):
    if (class_list[i] == 'I'):
        summary.append(text1[i])
summary.append(text1[-2])
final_sum = '. '.join(summary)
print('\n\n', final_sum)

