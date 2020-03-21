import numpy as np


def getDictionaries_Word_Level():
    text = open("eminem-lyrics.txt", 'rb').read().decode(encoding='utf-8')
    text = text.upper().replace('\n', " \n ")

    words = text.split(' ')
    vocab = sorted(set(words))
    print(str(len(vocab)) + " unique words")
    txt2id = {u: i for i, u in enumerate(vocab)}
    id2txt = np.array(vocab)
    text_as_int = np.array([txt2id[c] for c in words])
    return txt2id, id2txt, text_as_int


def getDictionaries_Phoneme_Level():
    file = open("eminem-dictionary.txt", 'r')
    lines = file.readlines()
    file.close()

    spelling = dict()
    for l in lines:
        l=l.replace('\n','')
        spl = l.split(' ')
        spelling[spl[0]] = spl[1:]


getDictionaries_Phoneme_Level()
