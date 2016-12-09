#import sys
#sys.path.append('/usr/local/lib/python3.5/site-packages')

from nltk.corpus import wordnet as wn


def wordnet_sense(word=None, tag=None):
    if word == None:
        word = input('What word do you want to look up?  ')
    if tag == None:
        tag = input('What type of word do you want to look up?\nFor nouns, enter "n"\nFor verbs, enter "v"\nFor adjectives, enter "a"\nOr simply press Enter for all possible meanings.\n')

    possible_tags = ['a', 'n', 'v']

    if tag == '':
        syn = wn.synsets(word)
    else:
        syn = wn.synsets(word, pos=tag)

    if syn == []:
        print('No known definitions on the dictionary for this word and/or word type.')
    else:
        for s in syn:
            if tag in possible_tags: 
                print(word + ' == ' + s.definition())
            else:
                new_s = str(s).split('.')
                print(word + ', ' + new_s[1] + ' == ' + s.definition())


#####################Test Area#####################

#wordnet_sense('car', 'n')
