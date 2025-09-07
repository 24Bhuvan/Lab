import nltk 
import matplotlib.pyplot as plt
nltk.download('punkt_tab')
text = """Welcome you to programming knowledge, let's start with our first tutorial on NLTK. We shall learn the basics of NLTK here."""
from nltk.tokenize import word_tokenize
word_tokenized=word_tokenize(text)
# from nltk.tokenize import sent_tokenize
# print(sent_tokenize(text))
from nltk.probability import FreqDist
fd=FreqDist(word_tokenized)
print(fd.most_common(5))
fd.plot(30,cumulative=False)
plt.show()