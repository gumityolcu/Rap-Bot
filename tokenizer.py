f = open("eminem-lyrics-raw.txt", "r")
bars = f.readlines()
f.close()

spelling = dict()
f = open("CMU/cmudict-0.7b.txt", "r")
dictLines = f.readlines()
vocabulary = list()
f.close()
for l in range(0, len(dictLines)):
    dictLines[l] = dictLines[l].replace("\n", "")
    if dictLines[l][0:3] != ";;;":
        spl = dictLines[l].split(" ")
        if spl[0][-1] != ')':
            spelling[spl[0]] = spl[2:]

spelling["<Q_MARK>"] = ""
spelling["<E_MARK>"] = ""
spelling["<DOT>"] = ""
spelling["<COMMA>"] = ""
spelling["<BEGINSONG>"] = ""
spelling["<ENDSONG>"] = ""

misses = dict()
for bar in bars:
    bar = bar.replace("\n", "")
    if bar != "" and bar[-1] != "]" and bar[-1] != "}" and bar[-1] != ">":
        words = bar.split(" ")
    else:
        words = [bar]

    for w in words:
        w = w.upper()
        w = w.replace("?", "<Q_MARK>")
        w = w.replace("!", "<E_MARK>")
        w = w.replace(".", "<DOT>")
        w = w.replace(",", "<COMMA>")
        if w not in spelling:
            if w[-3:] == "IN'":
                w = w[0:-1]
            if w[-2:] == "IN":
                w_t = w + "G"
                if w + "G" in spelling:
                    spelling[w] = spelling[w + "G"][0:-1] + ['N']
                elif w[0:-2] in spelling:
                    spelling[w] = spelling[w[0:-2]] + ['IH0', 'N']
                elif w[0:-2] + "E" in spelling:
                    spelling[w] = spelling[w[0:-2] + "E"] + ['IH0', 'N']

        if not w in spelling:
            if w in misses:
                misses[w] += 1
            else:
                misses[w] = 1
running = 0
for w in misses:
    running += misses[w]
    if len(w) > 5:
        print(w + "  " + str(misses[w]))

print("Total distinct : " + str(len(misses.keys())))
print("Total : " + str(running))
