#Compulsory task 1

import spacy
nlp=spacy.load('en_core_web_md')

word1=nlp("cat")
word2=nlp("monkey")
word3=nlp("banana")

print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

'''
# using the loops to find similarity
tokens=nlp('cat apple monkey banana')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text,token1.similarity(token2))



# working with sentences
sentence_to_compare="Why is my cat on the car"

sentences=["Where did my dog do",
"Hello,there is my car",
"I\'ve lost my car in my car",
"I\'d like my boat back",
"I will name my dog Diana"]

model_sentences=nlp(sentence_to_compare)

for sentence in sentences:
    similarity=nlp(sentence).similarity(model_sentences)
    print(sentence+" - ", similarity)
'''

# the semantic similarity referes to the degree to which two pieces of text have a similar meaning
# as cat and moneky are both animals so they have highest similarity
# monkey and banana are somewhat related as monkey eats bananas so they have some similarity but lesser than the first one
# cat and banana are least similar as they are not very linked

# example 
word1=nlp("bus")
word2=nlp("car")
word3=nlp("house")

print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))
# bus and car have hishest similarity as they are means of transport
# car and house have lesser similarity than 1 as they are somewhat linked
# bus and house have least similarity



'''by running example1.py with a simpler model en_core_Web_sm generates a warning that this model does not have
word vectors loaded and the similarity calculation will not be very accurate. It advises to use larger models
'''
