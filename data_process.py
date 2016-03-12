import nltk

def load_sents(script_file='data/TPO1-49ReadingScripts.txt'):
    script = open(script_file, mode='r')

    sentences = []
    for line in script:
        line = line.strip()
        if line.find(".") > 0:
            for sent in nltk.sent_tokenize(line):
                sent = sent.lower()
                sentences.append(sent)


    return sentences

def load_words(file='data/N_General_Service_List.txt'):
    words = []
    for line in open(file):
        line = line.strip()
        line = line.split(' ')
        words.append(line)

    return words

def write_file(path='./data/default/', word='default', sent_list=['just.', 'a.', 'test.']):
    file = open(path + word + '.txt', 'w')
    for sent in sent_list:
        file.write(sent + '\r\n')
    file.close()
