import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
import warnings
import gensim
from gensim.models import Word2Vec

#bot = Scraper()
#bot.get_songs()

sample = open("/Users/macbook/Desktop/eminem-lyrics.txt.txt", "r")
s = sample.read()

# Replaces escape character with space
f = s.replace("\n", " ")
print(f)

data = []

# iterate through each sentence in the file
for i in sent_tokenize(f):
    temp = []

    # tokenize the sentence into words
    for j in word_tokenize(i):
        temp.append(j.lower())

    data.append(temp)


# Create CBOW model
model1 = gensim.models.Word2Vec(data, min_count = 1, size = 80, window = 10)

# Print results
word1="sock"
word2="hair"

print("Cosine similarity between '"+word1+"' " + "and '"+word2+"' - CBOW : ", model1.similarity(word1, word2))