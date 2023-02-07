# === Your task ==============================================================
# Let's have some 'fun'.
# Go to http://en.wikipedia.org/wiki/Garden_path_sentence and have a brief read 
# at what a 'Garden Path sentence' is (at the top) and look at the 'Examples'

# Create the file garden.py for this task.
# 1. Use some Garden Path sentences or think up your own (at least 5).
# 2. Tokenise and perform Entity recognition for each of the sentences 
#    after you have stored them in a list called gardenpathSentences.
# 3. See how spaCy has categorised these sentences and look up the entities you
#    don't understand
# 4. At the bottom of your file, write a comment about two unusual entities 
# you found that spaCy gave one of the words of your sentences - did you expect this?


import spacy

nlp = spacy.load('en_core_web_md')


gardenpathsentences = ['The complex in New York houses married and single soldiers and their families',
                       'Fat people eat accumulates.',
                       'The black horse raced past the red barn that fell down',
                       'The sun rises in the east and sets in the west.',
                       'The man who hunts ducks out on weekends']

#tokenise the input sample in loop
for sentence in gardenpathsentences:
    sentence = nlp(sentence)
    print ([token.orth_ for token in sentence])


#loop for entity recognition for each of the sentences
#tokenise and entity recognition on list
for sentence in gardenpathsentences:
    sentence = nlp(sentence)
    entities = ([(ent.text, ent.label_, ent.label) for ent in sentence.ents])
    print(entities)

# output is below
'''
[('New York', 'GPE', 384)]
[]
[]
[]
[('weekends', 'DATE', 391)]
'''
# shows that only 2 tokens were entity recognised in the sentence 
#GPE = Geo-Political Entity
#DATE = date