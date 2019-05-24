import numpy as np
import string
import operator
import matplotlib.pyplot as plt


def get_text(filename):
    f = open(filename)
    text = f.read()
    f.close()
    return text

def clean_text(text):
    text = text.translate(str.maketrans('', '', string.punctuation))
    words = text.split()
    word_freq_map = {}
    for word in words:
        word = word.lower()
        word_freq_map[word] = word_freq_map.get(word, 0) + 1
    word_freq_map = sorted(word_freq_map.items(), key = operator.itemgetter(1), reverse = True)
    return word_freq_map

def plot_freq(freq_map1, freq_map2, freq_map3, freq_map4, freq_map5):
    freq1 = [f for w, f in freq_map1]
    rank1 = [i + 1 for i, f in enumerate(freq1)]
    freq2 = [f for w, f in freq_map2]
    rank2 = [i + 1 for i, f in enumerate(freq2)]
    freq3 = [f for w, f in freq_map3]
    rank3 = [i + 1 for i, f in enumerate(freq3)]
    freq4 = [f for w, f in freq_map4]
    rank4 = [i + 1 for i, f in enumerate(freq4)]
    freq5 = [f for w, f in freq_map5]
    rank5 = [i + 1 for i, f in enumerate(freq5)]
    
    plt.figure(figsize = (6, 8))
    
    plt.subplot(5, 2, 1)
    plt.plot(freq1)
    plt.xlabel('Rank')
    plt.ylabel('Frequency')
    plt.title("Rahul's story")
    plt.subplot(5, 2, 2)
    plt.scatter(np.log(rank1), np.log(freq1))
    plt.ylabel('Log frequency')
    plt.xlabel('Log Rank')
  
    plt.subplot(5, 2, 3)
    plt.plot(freq2)
    plt.xlabel('Rank')
    plt.ylabel('Frequency')
    plt.title("Nayonika's story")
    plt.subplot(5, 2, 4)
    plt.scatter(np.log(rank2), np.log(freq2))
    plt.ylabel('Log frequency')
    plt.xlabel('Log Rank')

    plt.subplot(5, 2, 5)
    plt.plot(freq3)
    plt.xlabel('Rank')
    plt.ylabel('Frequency')
    plt.title("Amisha's story")
    plt.subplot(5, 2, 6)
    plt.scatter(np.log(rank3), np.log(freq3))
    plt.ylabel('Log frequency')
    plt.xlabel('Log Rank')
    
    plt.subplot(5, 2, 7)
    plt.plot(freq4)
    plt.xlabel('Rank')
    plt.ylabel('Frequency')
    plt.title("Chinmay's story")
    plt.subplot(5, 2, 8)
    plt.scatter(np.log(rank4), np.log(freq4))
    plt.ylabel('Log frequency')
    plt.xlabel('Log Rank')
    
    plt.subplot(5, 2, 9)
    plt.plot(freq5)
    plt.xlabel('Rank')
    plt.ylabel('Frequency')
    plt.title("Atharva's story")
    plt.subplot(5, 2, 10)
    plt.scatter(np.log(rank5), np.log(freq5))
    plt.ylabel('Log frequency')
    plt.xlabel('Log Rank')

    
    plt.tight_layout()
    plt.show()

def char_analysis(freq_map, character_set):
    char_map = {}
    for w, f in freq_map:
        if w in character_set:
            char_map[w] = f
    return char_map

def get_freq_list(char_freq_map):
    freq_list = [f for w, f in char_freq_map.items()]
    return freq_list
    
    
if __name__ == "__main__":    
    rahul = get_text('Stories/rahul.txt')
    freq_map_rahul = clean_text(rahul)
    nayo = get_text('Stories/nayonika.txt')
    freq_map_nayo = clean_text(nayo)
    amisha = get_text('Stories/amisha.txt')
    freq_map_amisha = clean_text(amisha)
    chinmay = get_text('Stories/chinmay.txt')
    freq_map_chinmay = clean_text(chinmay)
    atharva = get_text('Stories/atharva.txt')
    freq_map_atharva = clean_text(atharva)
    
    plot_freq(freq_map_rahul, freq_map_nayo, freq_map_amisha, freq_map_chinmay, freq_map_atharva)
    
    combined = get_text('Stories/combined.txt')
    freq_map_comb = clean_text(combined)
    comb_freq = [f for w, f in freq_map_comb]
    comb_rank = [i+1 for i, f in enumerate(comb_freq)]
    plt.subplot(1, 2, 1)
    plt.plot(comb_freq)
    plt.ylabel('Frequency')
    plt.xlabel('Rank')
    plt.subplot(1, 2, 2)
    plt.scatter(np.log(comb_rank), np.log(comb_freq))
    plt.ylabel('Log Frequency')
    plt.xlabel('Log Rank')
    plt.suptitle('Combined Corpus')
    plt.tight_layout()
    plt.show()



    rahul_character_set = ('fnehn', 'oecvyz', 'plcswea', 'eyrde', 'zxdgf', 'pefsha')
    rahul_char_freq_map = char_analysis(freq_map_rahul, rahul_character_set)
    nayo_character_set = ('dgyee', 'gysw', 'jigqa', 'loffo', 'tudr', 'reew')
    nayo_char_freq_map = char_analysis(freq_map_nayo, nayo_character_set)
    amisha_character_set = ('mehitamo', 'rakuse', 'poeintsa', 'ouytre', 'davaidle', 'loiwe')
    amisha_char_freq_map = char_analysis(freq_map_amisha, amisha_character_set)
    chinmay_character_set = ('ketri', 'yandex', 'ussopin', 'detiria', 'tordeb', 'gashni')
    chinmay_char_freq_map = char_analysis(freq_map_chinmay, chinmay_character_set)
    atharva_character_set = ('ffuso', 'rpflaj', 'kgodla', 'dlalaf', 'kaapc', 'Taoalc')
    atharva_char_freq_map = char_analysis(freq_map_atharva, atharva_character_set)
    
    
    rahul_char_freq = get_freq_list(rahul_char_freq_map)
    nayo_char_freq = get_freq_list(nayo_char_freq_map)
    amisha_char_freq = get_freq_list(amisha_char_freq_map)
    chinmay_char_freq = get_freq_list(chinmay_char_freq_map)
    atharva_char_freq = get_freq_list(atharva_char_freq_map)
    
    
    char_freq = []
    for i in range(6):
        freq = rahul_char_freq[i] + nayo_char_freq[i] + amisha_char_freq[i] + chinmay_char_freq[i] + atharva_char_freq[i]
        freq = freq / 5
        char_freq.append(freq)
    
    char_rank = [(i + 1) for i, f in enumerate(char_freq)]
    
    plt.subplot(1, 2, 1)
    plt.bar(char_rank, char_freq)
    plt.ylabel('Frequency')
    plt.xlabel('Rank')
    plt.subplot(1, 2, 2)
    plt.scatter(np.log(char_rank), np.log(char_freq))
    plt.ylabel('Log frequency')
    plt.xlabel('Log rank')
    plt.tight_layout()
    
    
    # random = get_text('Stories/random.txt')
    # random_freq_map = clean_text(random)
    # rand_freq = [f for w, f in random_freq_map]
    # rand_rank = [i + 1 for i, f in enumerate(rand_freq)]

    # plt.subplot(1, 2, 1)
    # plt.plot(rand_freq)
    # plt.xlabel('Rank')
    # plt.ylabel('Frequency')
    # plt.subplot(1, 2, 2)
    # plt.scatter(np.log(rand_rank), np.log(rand_freq))
    # plt.ylabel('Log frequency')
    # plt.xlabel('Log Rank')
    # plt.tight_layout()
    # plt.suptitle("Random Text")
    # plt.show()