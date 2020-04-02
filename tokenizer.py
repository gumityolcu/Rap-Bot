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
    text = open("eminem-lyrics-phonemes.txt", 'rb').read().decode(encoding='utf-8')
    text = text.upper().replace('\n', " \n ")

    words = text.split(' ')
    vocab = sorted(set(words))
    print(str(len(vocab)) + " unique words")
    txt2id = {u: i for i, u in enumerate(vocab)}
    id2txt = np.array(vocab)
    text_as_int = np.array([txt2id[c] for c in words])
    return txt2id, id2txt, text_as_int


def generatePhonemeLevelLyrics():
    file = open("eminem-dictionary-without-stress.txt", 'r')
    lines = file.readlines()
    file.close()

    print('Reading dictionary')

    spelling = dict()
    for l in lines:
        l = l.replace('\n', '')
        spl = l.split(' ', 1)
        spelling[spl[0]] = spl[1]

    print(spelling)
    text = open("eminem-lyrics.txt", 'rb').read().decode(encoding='utf-8')
    words = text.upper()
    words = words.replace(' ', ' <SPACE> ')
    words = words.replace('\n', " <NEWLINE> ")
    words = words.replace(',', ' <COMMA>')
    words = words.replace('.', ' <DOT>')
    words = words.replace('!', ' <E_MARK>')
    words = words.replace('?', ' <Q_MARK>')
    splitWords = words.split(' ')
    f = open("eminem-lyrics-phonemes.txt", 'w')
    for w in splitWords:
        if w in spelling:
            f.write(spelling[w]+' ')
    f.close()

def reduceDictionary():
    f=open('eminem-dictionary-with-stress.txt','r')
    lines=f.readlines()
    f.close()
    f=open('eminem-dictionary-without-stress.txt','w')
    for l in lines:
        spl=l.split(' ',1)
        spl[1]=spl[1].replace('0','')
        spl[1]=spl[1].replace('1','')
        spl[1]=spl[1].replace('2','')
        f.write(spl[0]+' '+spl[1])
    f.close()
