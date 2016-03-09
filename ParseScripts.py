import nltk

def load_scripts(script_file='data/TPO1-49ReadingScripts.txt'):
    script = open(script_file, mode='r')

    sentences = []
    for line in script:
        line = line[:-2]
        if line.find(".") > 0:
            for sent in nltk.sent_tokenize(line):
                sentences.append(sent)


    return sentences

if __name__ == '__main__':
    reading_scripts = 'data/TPO1-49ReadingScripts.txt'
    listening_scripts = 'data/TPO1-35listeningScripts.txt'

    reading_sents = load_scripts(reading_scripts)
    listening_sents = load_scripts(listening_scripts)

    print len(reading_sents)
    print len(listening_sents)
