import operator
from nltk.corpus import brown
import matplotlib.pyplot as plt
import numpy as np
import string
from glob import glob

def get_brown_freq():
    sentences = brown.sents()
    
    word_idx_count = {}
    
    for sentence in sentences:
        for token in sentence:
            token = token.lower()
            word_idx_count[token] = word_idx_count.get(token, 0) + 1

    
    sorted_word_idx_map = sorted(word_idx_count.items(), key = operator.itemgetter(1), reverse = True)
    freq = [f for w, f in sorted_word_idx_map]
    rank = [i + 1 for i, f in enumerate(freq)]
    return freq, rank

def get_wiki_freq():
    files = glob('../Wiki/enwiki*.txt')
    all_word_counts = {}
    for f in files:
        for line in open(f):
            if line and line[0] not in '[*-|=\{\}':
                s = line.translate(str.maketrans('', '', string.punctuation)).lower().split()
                for word in s:
                    if word not in all_word_counts:
                        all_word_counts[word] = 0
                    all_word_counts[word] += 1
    all_word_counts = sorted(all_word_counts.items(), key = lambda x: x[1], reverse = True)
    freq = [f for w, f in all_word_counts]
    rank = [i + 1 for i, f in enumerate(freq)]
    return freq, rank
        

def plot_freq(freq, rank):
    plt.subplot(1, 2, 1)
    plt.scatter(rank, freq)
    plt.xlabel('Rank')
    plt.ylabel('Frequency')
    plt.subplot(1, 2, 2)
    plt.scatter(np.log(rank), np.log(freq))
    plt.ylabel('Log frequency')
    plt.xlabel('Log Rank')
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    print("Brown Corpus Data")
    brown_freq, brown_rank = get_brown_freq()
    plot_freq(brown_freq, brown_rank)
    
    print("Wikipedia Data")
    wiki_freq, wiki_rank = get_wiki_freq()
    plot_freq(wiki_freq, wiki_rank)