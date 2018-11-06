# -*- coding: utf-8 -*-
"""
Created on Sat Oct 13 13:43:16 2018

@author: vineet
"""
#import pandas as pd
##path = '0004.1999-12-14.farmer.ham.txt'
##features = ['message','label']
##sms = pd.read_table(path, header=None, names=features,index=0)
##print(sms)
#
##files = glob.glob('*ham*.csv')
##for f in files:
##    i=0
##    file = open(f,mode='r')
##    all_of_it = f.read()
##    result = pd.DataFrame({'message':all_of_it},index = [1])
##    if(i>0):
##        total_result = pd.concat(c[result,total_result], ignore_index=True)
##    else:
##        total_result = pd.DataFrame({'message':all_of_it},index = [1])
#
#
#
#features = ['message']
#files = glob.glob('*ham*.txt')
#
#result = pd.concat([pd.read_table(f,header =None,names = features) for f in files], ignore_index=True)
#
#print(result)
import glob
import math
import re

regex = re.compile('[@_!#$%^&*()<>?/\|},.{~:]-') 


with open('spclchar.txt') as f:
    spclchar = f.readlines()

spclchar = [x.strip() for x in spclchar]

                     
with open('stopwords.txt') as f:
    content = f.readlines()

content = [x.strip() for x in content]                     
#print(content)                     
                     
d = {}

d1 = {}

word_list2 = []
files1 = glob.glob('train/ham/*ham*.txt')


totalhamfiles = len(files1)
#print(totalhamfiles)
#for file in files1:
#    document_text = open(file, 'r')
#    text_string = document_text.readlines()
##match_pattern = re.findall(r'\b[a-z]\b', text_string)
##print(match_pattern)
#    for word in text_string:
#        word_list = word.split(" ")
#        word_list2.extend(word_list)
#    word_list2 = [x.strip() for x in word_list2]
#    for word in word_list2:
#        if word not in content:
#            if word not in spclchar:
#                d[word] = d.get(word, 0) + 1
#                
#            
#    for word in word_list2:
#        if word not in spclchar:
#            d1[word] = d1.get(word, 0) + 1
        
for file in files1:
    document_text = open(file, 'r')
    text_string = document_text.read()
#match_pattern = re.findall(r'\b[a-z]\b', text_string)
#print(match_pattern)
    
    word_list = text_string.split(" ")
     
    word_list = [x.strip() for x in word_list]
    for word in word_list:
        if word not in content:
            if word not in spclchar:
                d[word] = d.get(word, 0) + 1
                
            
    for word in word_list:
        if word not in spclchar:
            d1[word] = d1.get(word, 0) + 1            
        
     
#    print(d)
    
#print(d)
h = {}
h1 = {}

word_list4 = []

files2 = glob.glob('train/spam/*spam.txt')

totalspamfiles = len(files2)
#print(totalspamfiles)
totalfiles = totalhamfiles + totalspamfiles
#print(totalfiles)

#for file in files2:
#    document_text2 = open(file, 'r',encoding="Latin-1")
#    text_string2 = document_text2.readlines()
#    for word in text_string2:
#        word_list3 = word.split(" ")
#        word_list4.extend(word_list3)
#    word_list4 = [x.strip() for x in word_list4]        
#    for word in word_list4:
#        
#        if word not in content:
#            if word not in spclchar:
#                h[word] = h.get(word, 0) + 1
#                
#            
#    for word in word_list4:
#        if word not in spclchar:
#            h1[word] = h1.get(word, 0) + 1

for file in files2:
    document_text2 = open(file, 'r',encoding="Latin-1")
    text_string2 = document_text2.read()
    
    word_list3 = text_string2.split(" ")
        
    word_list3 = [x.strip() for x in word_list3]        
    for word in word_list3:
        
        if word not in content:
            if word not in spclchar:
                h[word] = h.get(word, 0) + 1
                
            
    for word in word_list3:
        if word not in spclchar:
            h1[word] = h1.get(word, 0) + 1






#       if word not in content:
#            if len(word)==1:
#                if regex.search(word) == None:
#                    h[word] = h.get(word, 0) + 1
#            else:
#                h[word] = h.get(word, 0) + 1
#    for word in word_list4:
#        if len(word)==1:
#            if regex.search(word) == None:
#                h1[word] = h1.get(word, 0) + 1
#        else:
#            h1[word] = h1.get(word, 0) + 1
            
            
        
     
#    print(h)

#print(h)
logspam = 0
logham = 0
logspam1 = 0
logham1 = 0
totalham = 0
totalspam = 0
totalham1 = 0
totalspam1 = 0
# calculate probability for ham
for values in d.values():
    totalham = totalham + values
#print(totalham)

for values in d1.values():
    totalham1 = totalham1 + values
#print(totalham1)
#print(totalham)

for values in h.values():
    totalspam = totalspam + values

for values in h1.values():
    totalspam1 = totalspam1 + values

#print(totalspam)

total = totalham+totalspam
total1 = totalham1 + totalspam1
#document_text3 = open('test/ham/0003.1999-12-14.farmer.ham.txt', 'r')
countham = 0
countspam = 0

countham1 = 0
countspam1 = 0

finallogham = 0
finallogspam = 0

finallogham1 = 0
finallogspam1 = 0


files3 = glob.glob('test/spam/*spam.txt')
for file in files3:
    document_text3 = open(file, 'r',encoding="Latin-1")
    text_string3 = document_text3.read()
    word_list3 = text_string3.split(" ")
    for word in word_list3:
        logham = logham + math.log((d.get(word, 0)+1)/(totalham+total))
        logham1 = logham1 + math.log((d1.get(word, 0)+1)/(totalham1+total1))
        logspam = logspam + math.log((h.get(word, 0)+1)/(totalspam+total))
        logspam1 = logspam1 + math.log((h1.get(word, 0)+1)/(totalspam1+total1))
    finallogham = logham + math.log(totalhamfiles/totalfiles)
    finallogham1 = logham1 + math.log(totalhamfiles/totalfiles)
    finallogspam = logspam + math.log(totalspamfiles/totalfiles)
    finallogspam1 = logspam1 + math.log(totalspamfiles/totalfiles)
    if finallogham>finallogspam:
        countham = countham + 1
    else:
        countspam = countspam + 1
    if finallogham1>finallogspam1:
        countham1 = countham1 + 1
    else:
        countspam1 = countspam1 + 1
     
#    if logham>logspam:
#        countham = countham + 1
#    else:
#        countspam = countspam + 1
#    if logham1>logspam1:
#        countham1 = countham1 + 1
#    else:
#        countspam1 = countspam1 + 1
total_testspamfiles = 130         
        
print("Without stop words count of ham while testing spam ",countham)
print("Without stop words count of spam while testing spam ",countspam)

Accuracy = (countspam/total_testspamfiles)*100

print("Accuracy on ham set without stop words ",Accuracy)




print("With stop words count of ham while testing spam ",countham1)
print("With stop words count of spam while testing spam ",countspam1)



Accuracy1 = (countspam1/total_testspamfiles)*100

print("Accuracy on ham set with stop words ",Accuracy1)

            
countham2 = 0
countspam2 = 0
 
countham3 = 0
countspam3 = 0

logspam2 = 0
logham2 = 0

logspam3 = 0
logham3 = 0

finallogham2 = 0
finallogspam2 = 0

finallogham3 = 0
finallogspam3 = 0


files4 = glob.glob('test/ham/*ham*.txt')
for file in files4:
    document_text4 = open(file, 'r')
    text_string4 = document_text4.read()
    word_list4 = text_string4.split(" ")
    for word in word_list4:
        logham2 = logham2 + math.log((d.get(word, 0)+1)/(totalham+total))
        logham3 = logham3 + math.log((d1.get(word, 0)+1)/(totalham1+total1))
        logspam2 = logspam2 + math.log((h.get(word, 0)+1)/(totalspam+total))
        logspam3 = logspam3 + math.log((h1.get(word, 0)+1)/(totalspam1+total1))
    finallogham2 = logham2 + math.log(totalhamfiles/totalfiles)
    finallogham3 = logham3 + math.log(totalhamfiles/totalfiles)
    finallogspam2 = logspam2 + math.log(totalspamfiles/totalfiles)
    finallogspam3 = logspam3 + math.log(totalspamfiles/totalfiles)
    if finallogham2>finallogspam2:
        countham2 = countham2 + 1
    else:
        countspam2 = countspam2 + 1
    if finallogham3>finallogspam3:
        countham3 = countham3 + 1
    else:
        countspam3 = countspam3 + 1
        
#    if logham2>logspam2:
#        countham2 = countham2 + 1
#    else:
#        countspam2 = countspam2 + 1
#    if logham3>logspam3:
#        countham3 = countham3 + 1
#    else:
#        countspam3 = countspam3 + 1
        
print("Without stop words count of ham while testing ham ",countham2)
print("Without stop words count of spam while testing ham ",countspam2)

total_testhamfiles = 348

Accuracy2 = (countham2/total_testhamfiles)*100

print("Accuracy on ham set without stop words ",Accuracy2)

print("With stop words count of ham while testing ham ",countham3)
print("With stop words count of spam while testing ham ",countspam3)

Accuracy3 = (countham3/total_testhamfiles)*100

print("Accuracy on ham set with stop words ",Accuracy2)


#    print("word is ",word)
#    print(d.get(word, 0)+1)
#    print(math.log((d.get(word, 0)+1)/(total)))

#    print(h.get(word, 0)+1)
#    print(math.log((h.get(word, 0)+1)/(total)))
    

#print(logham)
#print(logspam)
        
#stopwords
    


 
#for word in match_pattern:
#    count = frequency.get(word,0)
#    frequency[word] = count + 1
#     
#frequency_list = frequency.keys()
# 
#for words in frequency_list:
#    print (words, frequency[words])

        
    



#
## Open a file: file
#file = open('0004.1999-12-14.farmer.ham.txt',mode='r')
# 
## read all lines at once
#all_of_it = file.read()
# 
#test = pd.DataFrame({'message':all_of_it},index = [2])
#print(test)
#
## close the file
#file.close()


