from data_process import load_sents
from data_process import load_words
from data_process import write_file

general_words = load_words('data/N_General_Service_List.txt')
academeic_words = load_words('data/N_Academic_Word_List.txt')

reading_sents = load_sents('data/TPO1-49ReadingScripts.txt')
listening_sents = load_sents('data/TPO1-35listeningScripts.txt')

for word in general_words:
    sents = []
    for sent in reading_sents:
        if sent.find(word) >= 0:
            sents.append(sent)

    for sent in listening_sents:
        if sent.find(word) >= 0:
            sents.append(sent)

    write_file('./data/general/', word=word, sent_list=sents)

for word in academeic_words:
    sents = []
    for sent in reading_sents:
        if sent.find(word) >= 0:
            sents.append(sent)

    for sent in listening_sents:
        if sent.find(word) >= 0:
            sents.append(sent)

    write_file('./data/academic/', word=word, sent_list=sents)