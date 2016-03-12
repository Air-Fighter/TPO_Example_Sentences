import nltk

from data_process import load_sents
from data_process import load_words
from data_process import write_file

general_words = load_words('data/N_General_Service_List.txt')
academeic_words = load_words('data/N_Academic_Word_List.txt')

reading_sents = load_sents('data/TPO1-49ReadingScripts.txt')
listening_sents = load_sents('data/TPO1-35listeningScripts.txt')

"""
print "...processing general words"
for word_set in general_words:

    print "\rprocessing word:", word_set,

    sents = []
    for sent in reading_sents:
        sent_words = nltk.word_tokenize(sent)
        for word in word_set:
            if word in sent_words:
                sents.append(sent)
                break


    for sent in listening_sents:
        sent_words = nltk.word_tokenize(sent)
        for word in word_set:
            if word in sent_words:
                sents.append(sent)
                break

    write_file('./data/general/', word=word_set[0], sent_list=sents)
"""

for word_set in academeic_words:
    print "\rprocessing word:", word_set,

    sents = []
    for sent in reading_sents:
        sent_words = nltk.word_tokenize(sent)
        for word in word_set:
            if word in sent_words:
                sents.append(sent)
                break


    for sent in listening_sents:
        sent_words = nltk.word_tokenize(sent)

        for word in word_set:
            if word in sent_words:
                sents.append(sent)
                break

    write_file('./data/academic/', word=word_set[0], sent_list=sents)