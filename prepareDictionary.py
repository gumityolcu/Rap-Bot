f = open("eminem-lyrics.txt", "r")
bars = f.readlines()
f.close()

CMUSpelling = dict()
diction = dict()
f = open("CMU/cmudict-0.7b.txt", "r")
dictLines = f.readlines()
vocabulary = list()
f.close()

for l in range(0, len(dictLines)):
    dictLines[l] = dictLines[l].replace("\n", "")
    if dictLines[l][0:3] != ";;;":
        spl = dictLines[l].split(" ")
        if spl[0][-1] != ')':
            CMUSpelling[spl[0]] = spl[2:]

CMUSpelling["<Q_MARK>"] = ""
CMUSpelling["<E_MARK>"] = ""
CMUSpelling["<DOT>"] = ""
CMUSpelling["<COMMA>"] = ""
CMUSpelling["<BEGINSONG>"] = ""
CMUSpelling["<ENDSONG>"] = ""

for bar in bars:
    bar = bar.replace("\n", "")
    if bar != "" and bar[-1] != "]" and bar[-1] != "}":
        words = bar.split(" ")

    for w in words:
        w = w.upper()
        w = w.replace("?", "<Q_MARK>")
        w = w.replace("!", "<E_MARK>")
        w = w.replace(".", "<DOT>")
        w = w.replace(",", "<COMMA>")
        if (w not in CMUSpelling) and (w.replace("'", "") in CMUSpelling):
            w = w.replace("'", "")
        if w not in CMUSpelling:
            if w[-3:] == "IN'":
                w = w[0:-1]
            if w[-2:] == "IN":
                if w + "G" in CMUSpelling:
                    CMUSpelling[w] = CMUSpelling[w + "G"][0:-1] + ['N']
                elif w[0:-2] in CMUSpelling:
                    CMUSpelling[w] = CMUSpelling[w[0:-2]] + ['IH0', 'N']
                elif w[0:-2] + "E" in CMUSpelling:
                    CMUSpelling[w] = CMUSpelling[w[0:-2] + "E"] + ['IH0', 'N']
            if w[-3:] == "'LL":
                if w[0:-3] in CMUSpelling:
                    CMUSpelling[w] = CMUSpelling[w[0:-3]] + ['IH0', 'L']
            if w[-2:] == "'S":
                if w[0:-2] in CMUSpelling:
                    CMUSpelling[w] = CMUSpelling[w[0:-2]] + ['S']
        if w in CMUSpelling:
            diction[w]=CMUSpelling[w]
vocabulary = sorted(diction.keys())
indexes = dict()
print(len(CMUSpelling.keys()))
f = open("eminem-dictionary.txt", 'w')
index = 0
for i in vocabulary:
    f.write(i)
    for s in diction[i]:
        f.write(" "+s)
    indexes[i] = index
    index = index + 1
    if index!=len(vocabulary):
        f.write('\n')
f.close()
