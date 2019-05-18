# Why Languages Evolve, Mathematically

It isn't uncommon to hear elders bemoan the younger generations about the language that the latter use, while glorifying the language of the past. However, they don’t speak the Shakespearean language either. An evolution in language is inevitable and there are many theories about it. But can we explain this phenomenon mathematically?
#### "The knights still slay as they slew; then do we play as we plew?"
Structurally, the cause of changing language can be attributed to the irregular verbs. All the confusion regarding tenses and grammar arise due to these. In case of regular verbs, we can easily decipher different forms of the verb by adding some letters at the end (work, works, worked, working etc). This isn’t the case with irregular verbs (be, is, was, being etc). Why do we adhere to these norms of irregular verbs? From a pedagogical standpoint one would argue that it is because of some already estalished grammar rules, but from a mathematical standpoint, one can counter as to why these rules were formulated in the first place. We can answer these questions if we look at the origins of the English language.

Earlier linguists used to write books called concordances, which essentially contained the number of times a word appeared in a particular book. This involved a careful counting of each and every word and indexing it. These days, thanks to advanced language processing techniques, we can do that in seconds. Once we have these concordances, we can further study the language behaviour. In order to do it myself, I asked a bunch of my friends to write short paragraphs and send them to me. In all those paragraphs, the most frequently used words were "the", "and", and "of".
Since the paragraphs were only about 100 words worth of text, they weren't big enough to find any definite conclusions. So I combined all the paragraphs into one single corpus and made another concordance out of it. This time, "the" was the most commonly used word, followed by "of", followed by "and" and so on. However, another interesting observation: "the" appeared almost twice as often as "of", and almost thrice as often as "and" etc. It seemed as if the most frequent word appeared n times as often as the nth frequent word.

So, if words are ranked according to their frequency (i.e. the most frequent word has the rank 1) then it is safe to say that, for the combined corpus, frequency of a word is equivalent to the reciprocal of the rank of the word. Hence, we can also derive that if we take the logarithm of both word frequency and word rank, then the relation should be linear with a negative slope. My corpus seems to adhere to this rule.

Not only that, the individual paragraphs also show similar patterns, albeit the short length of the text prevents the results from being quite conclusive.

While writing their little paragraphs, I asked my friends to develop a story based on 6 characters. In order to remove any kind of bias, the character names were to be complete gibberish. Again, in an average story, the most frequent character appeared almost twice as many times as the second most frequent character, almost thrice as many times as the third most frequent character, and so on. So the occurence of character names seemed to follow the same pattern.

The corpus of the Modern American English by Brown University also follows the same pattern,

<img width="600" height="400" src="https://github.com/itsmepiyush2/Zipf-Law/blob/master/results/brown_corpus.jpg">

as does the text from Wikipedia,

<img width="600" height="400" src="https://github.com/itsmepiyush2/Zipf-Law/blob/master/results/wiki_corpus.jpg">


From all these plots, it is clear that the frequency of a word is inversely proportional to the rank of the word and on plotting the log-log graph, we get almost a straight line with a negative slope.
This is an empirical law widely known as the Zipf's law. It explains why common words are very common, and uncommon words are very uncommon. Every language that has ever existed shows this property; even the ones we haven't been able to decode yet.

The reasons as to why all languages show this property are still under research but there are some theories. Zipf's law becomes very apparent when there are many unobserved, underlying variables. There are many natural as well as artificial systems that show a varying degree, and often, a surprising amount of statistical regularity. Zipf's law happens to be one of those regularities. One explanation is that it seeks to impose a balance between the listener and the speaker. Another argument could be that it is to minimise the number of phonemes to carry out communication. All these explanations are quite domain specific and don't necessarily prove anything really. So Zipf's law remains a mystery in the field of computational linguistics.

The fascinating truth is that the distribution of frequencies in randomly generated text also abides by the Zipf's law.

<img width="600" height="400" src="https://github.com/itsmepiyush2/Zipf-Law/blob/master/results/random_text.png">

The explanation for the distribution of random words is much easier. Consider a monkey intelligent enough to be able to press the alphaets on a keyboard. Each alphabet cluster (not separated by a space) is considered to be a word. To press a key each time, the monkey has 27 chances: all the 26 letters and the spacebar. So the probability to generate a single letter word is 1/27 since after a letter has been pressed, there is only one out of 27 ways to press the spacebar. Similarly the probability of getting a two letter word is 26/27 x 1/27 since after a letter is pressed there are 26 ways to not press the spacebar and then only one way to do so after the second letter. So as a word becomes longer (the spacebar is not pressed), its probability to exist decreases. This leads to a power law that is similar to Zipf's. However, this still does not explain why natural language behaves similarly. That's because, unlike random sequencing, where a word can be followed by any other word, in natural language, the probability of a word occurance largely depends on the previous word, or a sequence of previous words.

Whatever be the reasoning, this law helps us in identifying the driving factors of language evolution. It becomes evident because of this law that the most common verbs in the English language are all irregular (be, have, do, say, get, make, go, know, take, see, come, think) verbs. Instead of having only a few very commonly used irregular verbs and many more uncommon irregular verbs, almost all irregular verbs are quite commonly used. These verbs are an exception to the Zipf's law. This can be explained since irregular verbs are some of the oldest existing verbs.


English comes from the Proto Indo-European language family which followed the "ablaut" sytem; switching the vowel to convey tense (e.g. dig and dug, or sing and sang). The Proto Germanic language family, which descended from the Proto Indo-European family brought in some new rules by adding certain letters at the end of the word to convey tenses (e.g. work and worked). Today these "newer" additions are known as the regular rules but back then, these were the exceptions because there were so few of them. So as new words were being added to the vocabulary, they started adhering to the new rules, thereby increasing the proportion of the new words which followed the new rules. At the same time, more infrequently used irregular verbs switched to regular verbs (like the traditional past tense of "slay" is "slew" but in social media slang it is "slayed"). Infrequently used irregular verbs are regularised to do away with memorising the exceptions. That is the reason why most of the irregular verbs today are the ones that are very commonly used. It is as logical as us forgetting rules if we don't keep in touch with them as often.

Some researchers argue that language evolution has an analogy with principles of evolutionary biology. Languages transform as they are passed down from one generation to another or from one geographical location to another. This is termed as linguistic drift. Inclusion of the word "do" as an auxiliary verb ("you know not" to "you do not know") and other such changes were the result of random mutations in the language as usage evolved.

Combining the three properties: the Zipf's law, verb regularisation and the randomness factor, one can predict how fast a word will be regularised or changed completely in a language, i.e. how much time it will take for, say, the word "dug" to become "digged". If a word is highly common, it will take longer to regularise. If a verb is used a 100 times less frequently, it will reguralise 10 times as fast; whereas if a verb is used 10,000 times less frequently, it will regularise 100 times as fast. There is a hidden Zipfian pattern here as well. Let's consider an irregular verb "stink" which is used roughly once every 10,000 times: it will take around 700 years to regularise. On the other hand, "wed" has already started reguralising to "wedded". Thus, an increasing amount of language behaviour and evolution, despite its inherent randomnness, has its systematic and mathematical aspects.
