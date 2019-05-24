# Why Languages Evolve, Mathematically

It isn't uncommon to hear elders lament the death of "their language" and bemoan the younger generations about the language that the latter use. However, they don’t speak the Shakespearean tongue either. An evolution in language is inevitable and there are many theories about it. But can we explain this phenomenon mathematically?
#### "The knights still slay as they slew; then do we play as we plew?"
Structurally, the cause of changing language can be attributed to the irregular verbs. All the confusion regarding tenses and grammar arise due to these. In case of regular verbs, we can easily decipher different forms of the verb by adding some letters at the end (e.g. work, works, worked, working etc). This isn’t the case with irregular verbs (e.g. be, is, was, being etc). Why do we adhere to these norms of irregular verbs? From a pedagogical standpoint one would argue that it is because of some already estalished grammar rules, but from a mathematical standpoint, one can counter as to why these rules have been formulated in the first place. We can answer these questions if we look at the origins of the English language.

Earlier linguists used to write books called concordances, which essentially contained the number of times a word appeared in a particular book. This involved a careful counting of each and every word and indexing it. These days, thanks to advanced language processing techniques, we can do that in seconds. Once we have these concordances, we can further study the language behaviour. In order to do it myself, I asked a bunch of my friends to write short paragraphs and I made little concordances out of those. In all the paragraphs, the most frequently used words were "the", "and", and "of".
Since the paragraphs were only about 100 words worth of text, they weren't big enough to find any definite conclusions. So I combined all the paragraphs into one single corpus and made another concordance out of it. This time, "the" was the most commonly used word, followed by "of", followed by "and" and so on. However, another interesting observation: "the" appeared almost twice as often as "of", and almost thrice as often as "and". It seemed as if the most frequent word appeared n times as often as the nth frequent word.

So, if words are ranked according to their frequency (i.e. the most frequent word has the rank 1) then it is safe to say that, for the combined corpus, frequency of a word is proportional to the reciprocal of the rank of the word. Hence, we can also derive a logarithmic relationship between the two. If we take the logarithm of both word frequency and word rank, then the relation should be linear with a negative slope. My corpus seems to adhere to this rule.

<img width="600" height="400" src="results/combined_corpus.png" class="img-responsive" alt="">

That is astounding. Even more astounding is the fact that the individual paragraphs also show similar patterns, albeit the short length of the text prevents the results from being quite conclusive.

<img width="600" height="800" src="results/individual.png" class="img-responsive" alt="">

While writing their little paragraphs, I asked my friends to develop a story based on 6 characters. In order to remove any kind of bias, the character names were to be complete gibberish. Again, in a mean story, one character was always the most preferred, followed by the second most preferred character, followed by the third most preferred character, and so on. Moreover, the number of times a character occured in a story also followed a similar pattern. The pattern is not quite pronounced because there are only six characters as opposed to millions of words in the vocabulary. However, despite the small number of characters, the text shows this behaviour pretty well.
<img width="600" height="400" src="results/char.png" class="img-responsive" alt="">

The corpus of the Modern American English by Brown University also follows the same pattern,

<img width="600" height="400" src="results/brown_corpus.png" class="img-responsive" alt="">

as does the text from Wikipedia,

<img width="600" height="400" src="results/wiki_corpus.png" class="img-responsive" alt="">


From all these plots, it is clear that the frequency of a word is inversely proportional to the rank of the word and on plotting the log-log graph, we get almost a straight line with a negative slope.
This is an empirical law widely known as the Zipf's law. It explains why common words are very common, and uncommon words are very uncommon. Every language that has ever existed shows this property; even the ones we haven't been able to decode yet.

The reasons as to why all languages show this property are still under research but there are some theories. Zipf's law becomes very apparent when there are many unobserved, underlying variables. There are many natural as well as artificial systems that show a varying degree, and often, a surprising amount of statistical regularity. Zipf's law happens to be one of those regularities. One explanation is that it seeks to impose a balance between the listener and the speaker. Another argument could be that it is to minimise the number of phonemes to carry out communication. All these explanations are quite domain-specific and don't necessarily prove anything really. So Zipf's law remains a mystery in the field of computational linguistics.

The fascinating truth is that the distribution of frequencies in randomly generated text also abides by the Zipf's law. I generated random gibberish using an online gibberish generator and plotted it's distribution and log-log plots as shown below.

<img width="600" height="400" src="results/random_text.png" class="img-responsive">

The explanation for the distribution of random words is much easier. Consider a monkey intelligent enough to be able to press the alphabets on a keyboard. Each alphabet cluster (not separated by a space) is considered to be a word. To press a key each time, the monkey has 27 choices: all the 26 letters and the spacebar. So the probability to generate a single letter word is 1/27, since after a letter has been pressed, there is only one out of 27 ways to press the spacebar. Similarly, the probability of getting a two letter word is 26/27 x 1/27, since after a letter is pressed there are 26 ways to not press the spacebar and then only one way to do so after the second letter. Similarly, the probability of getting a three letter word is 26/27 x 26/27 x 1/27. So, as a word becomes longer (the spacebar is not pressed), its probability to exist decreases exponentially. This leads to a power law that is similar to Zipf's. However, this still does not explain why natural language behaves similarly. That's because, unlike random sequencing, where a word can be followed by any other word, in natural language, the probability of a word occurence largely depends on the previous word, or a sequence of previous words.

Whatever be the reasoning, this law helps us in identifying the driving factors of language evolution. It becomes evident because of this law that the most common verbs in the English language are all irregular (be, have, do, say, get, make, go, know, take, see, come, think) verbs. Instead of having only a few very commonly used irregular verbs and many more uncommon irregular verbs, almost all irregular verbs are quite commonly used. These verbs are an exception to the Zipf's law. This can be explained since irregular verbs are some of the oldest existing verbs.


English comes from the Proto Indo-European language family which followed the "ablaut" sytem; switching the vowel to convey tense (e.g. dig and dug, or sing and sang). The Proto Germanic language family, which descended from the Proto Indo-European family brought in some new rules by adding certain letters at the end of the word to convey tenses (e.g. work and worked). Today these "newer" additions are known as the regular rules but back then, these were the exceptions because there were so few of them. So as new words were being added to the vocabulary, they started adhering to the new rules, thereby increasing the proportion of the new words which followed the new rules. At the same time, more infrequently used irregular verbs switched to regular verbs (like the traditional past tense of "slay" is "slew" but in social media slang it is "slayed"). Infrequently used irregular verbs are regularised to do away with memorising the exceptions. That is the reason why most of the irregular verbs today are the ones that are very commonly used. It is as logical as us forgetting rules if we don't keep in touch with them as often. This is perhaps why the word "smelt" which has enjoyed its popularity for a long time has been overthrown by its regularised counterpart "smelled" since the 1900s.

<img width="900" height="400" src="results/ngram_viewer.png" class="img-responsive">

Some researchers argue that language evolution has an analogy with principles of evolutionary biology. Languages transform as they are passed down from one generation to another or from one geographical location to another. This is termed as linguistic drift. Inclusion of the word "do" as an auxiliary verb ("you know not" to "you do not know") and other such changes were the result of random mutations in the language as usage evolved.

Combining the three properties: the Zipf's law, verb regularisation and the randomness factor, one can predict how fast a word will be regularised or changed completely in a language, i.e. how much time it will take for, say, the word "dug" to become "digged". If a word is highly common, it will take longer to regularise. If a verb is used a 100 times less frequently, it will reguralise 10 times as fast; whereas if a verb is used 10,000 times less frequently, it will regularise 100 times as fast. There is a hidden Zipfian pattern here as well. Let's consider an irregular verb "stink", the past tense of which is "stank". It is used roughly once every 10,000 times: it will take around 700 years to regularise, i.e. become "stinked". On the other hand, "wed" has already started reguralising to "wedded", whereas "drank" will take a much longer time to become "drinked" because it is comparatively more frequently used. Thus, an increasing amount of language behaviour and evolution, despite its inherent randomnness, has its systematic predictability and mathematical aspects.
