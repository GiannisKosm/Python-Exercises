#-*- coding: utf-8 -*-

import nltk
from nltk.tokenize import sent_tokenize
from nltk.tag import pos_tag
from nltk.corpus import wordnet as wn


print"Give me phrase1!"
x=raw_input()
print"Give me phrase2!"
y=raw_input()
x=nltk.word_tokenize(x)
y=nltk.word_tokenize(y)

tokens1=pos_tag(x)
tokens2=pos_tag(y)  
print tokens1
print tokens2

a=[]
b=[]
#προσθήκη λέξεων με συγκεκριμένα tag(ρήματα,ουσιαστικά,επίθετα) σε νέες λίστες
for (word,tag) in tokens1:
    if tag[:2]=='VB' or tag[:2]=='NN' or tag[:2]=='JJ':
        a.append(word)
print a

for (word,tag) in tokens2:
    if tag[:2]=='VB'or tag[:2]=='NN'or tag[:2]=='JJ':
        b.append(word)
print b
#εύρεση συνώνυμων λέξεων με βαση τα στοιχεία του α και αποθήκευση στο syn_set
syn_set=[]

for i in a:
 for synset in wn.synsets(i):
    for item in synset.lemmas():
     syn_set.append(item.name())
print ("Synonym words from phrase 1:" ,syn_set)

#Έλεγχος για ύπαρξη συνώνυμων λέξεων(ρήματων,ουσιαστικών και επιθετών) αναμέσα στις συνώνυμες λεξεις του α και αυτές του β
if any(word in syn_set for word in b):
    print "There are similarities"
else:
    print "No similarities"
            
    
                
        




