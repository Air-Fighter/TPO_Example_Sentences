def load_words(file='data/N_General_Service_List.txt'):
    words = []
    for line in open(file):
        line = line[:-2]
        words.append(line)

    return words

if __name__ == '__main__':
    words = load_words()
    print len(words)
    print words[0]