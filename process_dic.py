from conll2dic import conll_dic

import webbrowser


#============================= Functions for Detecting Grammar Items =================================

#Level B1
#Function for matching simple adverbs: 
def adverb(dic):
    adverbs = []

    for i in dic:

        #Looks for all instances in the text tagged as RB, RBR or RBS (adverb tags)
        if dic[i][3].startswith('RB'):
            adverbs.append(i)

            #Prints the given word:
            print(dic[i][1] + ' = This adverb is the word number %s in the text.' % i)

    #Informs how many adverbs are comprised in the text
    print('\nThis text has %s adverbs.\n\n\n' % len(adverbs))
    
    return adverbs


#Levels A1, A2, B1
#Function for matching adjectives in their comparative and superlative form:
def adjectives_comp_super(dic):
	adjectives = []
	comparatives = []
	superlatives = []

	for i in dic:

		#Looks for all instances in the text tagged as JJ, JJR or JJS (adverb tags)
		if dic[i][3].startswith('JJ'):
			adjectives.append(i)
        
		if dic[i][3] == 'JJR':
			comparatives.append(i)

		elif dic[i][3] == 'JJS':
			superlatives.append(i)

		

    #Print simple statistics of adjectives:
	print('This text has %s adjectives, from which %s are in the comparative form and %s are in the superlative form.\n\n'
          % (len(adjectives), len(comparatives), len(superlatives)))

	print('These are the adjectives in comparative form:\n')
	for c in comparatives:
		print(dic[c][1] + ' = This adjective is the word number %s in the text.' % c)
    
	print('\n\n\nThese are the adjectives in superlative form:\n')
	for s in superlatives:
		print(dic[s][1] + ' = This adjective is the word number %s in the text.' % s)
        
	return adjectives, comparatives, superlatives



#Levels A2, B1
#Function for matching modal verbs
def modals():
    modal_verbs = []
    
    multiword_modals = ['ought', 'need', 'have']

    for i in dic:

        #Looks for all instances in the text tagged as RB, RBR or RBS (adverb tags)
        if dic[i][3] == 'MD' and dic[i][2] != 'will' and dic[i][2] not in multiword_modals:
            modal_verbs.append(i)
			
			#Prints the given word:
            print(dic[i][1] + ' = This verb is the word number %s in the text.' % i)
            
            
        elif dic[i][2] in multiword_modals and dic[i+1][2] == 'to':
            modal_verbs.append(i)
			  
			#Prints the given word:
            print(dic[i][1] + ' ' + dic[i+1][1] + ' = This verb is the word number %s in the text.' % i)

    #Informs how many adverbs are comprised in the text
    print('\nThis text has %s modal verbs instances.\n\n\n' % len(modal_verbs))


#Levels A2, B1
#Function for matching the use of passive voice
def passive_voice():
    passive = []

    for i in dic:

        #Looks for all instances in the text tagged as auxpass (dependency tag)
        if dic[i][6] == 'auxpass':
            passive.append(i)
			
			#Localizes the id of the participle in regard to the auxiliary verb
            position_participle = int(dic[i][5]) - int(dic[i][0])
			
			#Localizes the past participle
            participle = dic[i+position_participle]
			
			#Prints the given word:
            print(dic[i][1] + ' ' + participle[1] + ' = This auxiliary verb is the word number %s and this past participle is the word number %s in the text.\n' % (i, i+position_participle))
            
    #Informs how many adverbs are comprised in the text
    print('\nThis text has %s instances of passive voice.\n\n\n' % len(passive))


#Levels A2, B1
#Function for matching the use of future continuous
def future_continuous():
    future_continuous_structure = []

    for i in dic:
        be = []
        
        #Looks for all instances of "will" in the text
        if dic[i][2] == 'will':
			
			#Localizes the id of the participle in regard to the auxiliary verb
            position_ing = int(dic[i][5]) - int(dic[i][0])
			
			#Localizes the past participle
            if dic[i+position_ing][3] == 'VBG':
                ing = dic[i+position_ing]
                for numero in range(1, position_ing):
                    if dic[i+numero][2] == 'be':
                        future_continuous_structure.append(i)
                        be = dic[i+numero]
			
        #Prints the given word:
        if be != []:
            print(dic[i][1] + ' ' + be[1] + ' ' + ing[1] + ' = This auxiliary verb is the word number %s and this present participle is the word number %s in the text.\n' % (i, i+position_ing))
            
    #Informs how many adverbs are comprised in the text
    print('\nThis text has %s instances of future continuous.\n\n\n' % len(future_continuous_structure))


#Levels A1, A2, B1
#Function for matching the use of future tense
def future():
    future_structure = []
    
    for i in dic:

        #Looks for all instances of "will" in the text
        if dic[i][2] == 'will' and dic[i][6] == 'aux':
			
			#Localizes the id of the infinitive in regard to the auxiliary verb
            position_inf = int(dic[i][5]) - int(dic[i][0])
			
			#Localizes the past participle
            if dic[i+position_inf][3] == 'VB':
                inf = dic[i+position_inf]
                future_structure.append(i)
			
                #Prints the given word:
                print(dic[i][1] + ' ' + inf[1] + ' = This auxiliary verb is the word number %s and this infinitive is the word number %s in the text.\n' % (i, i+position_inf))
            
    #Informs how many adverbs are comprised in the text
    print('\nThis text has %s instances of future.\n\n\n' % len(future_structure))


#Levels A1, A2, B1
#Function for matching the use of future with 'going to'
def future_going_to():
    future_going_to_structure = []
    
    verb_present_tense = ['VBP', 'VBZ']
    
    for i in dic:

        #Looks for all instances of "will" in the text
        if dic[i][2] == 'be' and dic[i][3] in verb_present_tense and dic[i][6] == 'aux':
			
			#Localizes the id of the infinitive in regard to the auxiliary verb
            position_going = int(dic[i][5]) - int(dic[i][0])
			
			#Localizes the past participle
            if dic[i+position_going][1] == 'going' and dic[i+position_going+1][1] == 'to' and dic[i+position_going+2][3] == 'VB':
                going = dic[i+position_going]
                to = dic[i+position_going+1]
                inf = dic[i+position_going+2]
                future_going_to_structure.append(i)
			
                #Prints the given word:
                print(dic[i][1] + ' ' + going[1] + ' ' + to[1] + ' ' + inf[1] + ' = This auxiliary verb is the word number %s and this going is the word number %s in the text.\n' % (i, i+position_going))
            
    #Informs how many adverbs are comprised in the text
    print('\nThis text has %s instances of future with "going to".\n\n\n' % len(future_going_to_structure))


#Level A1, A2, B1
#Differences between future simple and future with 'going to'
#This is simply the union of two other functions
def fsVSfgt():
    future()
    future_going_to()



#Level B1
#Function for matching (non-auxiliary) past simple verbs
def past_tense_simple():
    past_tense_verbs = []

    for i in dic:

        #Looks for all instances in the text tagged as VBD (but not as auxiliar verb)
        if dic[i][3] == 'VBD' and dic[i][6].startswith('aux') == False:
            past_tense_verbs.append(i)

            #Prints the given word:
            print(dic[i][1] + ' = This verb is the word number %s in the text.' % i)

    #Informs how many verbs are comprised in the text
    print('\nThis text has %s verbs instances in the past form.\n\n\n' % len(past_tense_verbs))


#Level B1, B2
#Function for matching past continuous constructions
def past_continuous():
    past_continuous_structure = []

    for i in dic:

        #Looks for all instances of "had" in the text tagged as aux (dependency tag)
        if dic[i][2] == 'be' and dic[i][3] == 'VBD' and dic[i][6] == 'aux':
			
			#Localizes the id of the participle in regard to the auxiliary verb
            position_ing = int(dic[i][5]) - int(dic[i][0])
			
			#Localizes the present participle
            if dic[i+position_ing][3] == 'VBG':
                ing = dic[i+position_ing]
                past_continuous_structure.append(i)
			
                #Prints the given word:
                print(dic[i][1] + ' ' + ing[1] + ' = This auxiliary verb is the word number %s and this present participle is the word number %s in the text.\n' % (i, i+position_ing))
            
    #Informs how many adverbs are comprised in the text
    print('\nThis text has %s instances of past continuous.\n\n\n' % len(past_continuous_structure))



#Level A1, A2, B1
#Function for matching past perfect constructions
def past_perfect():
    past_perfect_construction = []
    
    for i in dic:

        #Looks for all instances of "had" in the text tagged as aux (dependency tag)
        if dic[i][2] == 'have' and dic[i][3] == 'VBD' and dic[i][6] == 'aux':
			
			#Localizes the id of the participle in regard to the auxiliary verb
            position_participle = int(dic[i][5]) - int(dic[i][0])
			
			#Localizes the past participle (and tries to match also regular participles, in case the verb is wrongly annotated as past tense)
            if dic[i+position_participle][3] == 'VBN' or dic[i+position_participle][1].endswith('ed'):
                participle = dic[i+position_participle]
                past_perfect_construction.append(i)
			
                #Prints the given word:
                print(dic[i][1] + ' ' + participle[1] + ' = This auxiliary verb is the word number %s and this past participle is the word number %s in the text.\n' % (i, i+position_participle))
            
    #Informs how many adverbs are comprised in the text
    print('\nThis text has %s instances of past perfect.\n\n\n' % len(past_perfect_construction))



#Levels B1
#Function for matching the use of present perfect continuous
def present_perfect_continuous():
    present_perfect_continuous_structure = []

    for i in dic:
        
        #Looks for all instances of "had" in the text tagged as aux (dependency tag)
        if dic[i][2] == 'have' and dic[i][3] == 'VBD' and dic[i][6] == 'aux':
			
			#Localizes the id of the -ing participle in regard to the auxiliary verb
            position_ing = int(dic[i][5]) - int(dic[i][0])
			
			#Localizes the past participle
            if dic[i+position_ing][3] == 'VBG':
                ing = dic[i+position_ing]
                for numero in range(1, position_ing):
                    if dic[i+numero][1] == 'been':
                        present_perfect_continuous_structure.append(i)
                        been = dic[i+numero]
			
                        print(dic[i][1] + ' ' + been[1] + ' ' + ing[1] + ' = This auxiliary verb is the word number %s and this present participle is the word number %s in the text.\n' % (i, i+position_ing))
            
    #Informs how many present perfect continuous are comprised in the text
    print('\nThis text has %s instances of present perfect continuous.\n\n\n' % len(present_perfect_continuous_structure))



#Levels A1, A2, B1
#Function for matching the use of present perfect
def present_perfect():
    present_perfect_structure = []

    for i in dic:
        
        verb_form_tags = ['VBZ', 'VBP']
        participle = []
        
        #Looks for all instances of "had" in the text tagged as aux (dependency tag)
        if dic[i][2] == 'have' and dic[i][3] in verb_form_tags and dic[i][6] == 'aux':
			
			#Localizes the id of the -ing participle in regard to the auxiliary verb
            position_participle = int(dic[i][5]) - int(dic[i][0])
			
			#Localizes the past participle (and tries to match also regular participles, in case the verb is wrongly annotated as past tense)
            if dic[i+position_participle][3] == 'VBN' or dic[i+position_participle][1].endswith('ed'):
                participle = dic[i+position_participle]
                present_perfect_structure.append(i)

                #Prints the given word:
                print(dic[i][1] + ' ' + participle[1] + ' = This auxiliary verb is the word number %s and this past participle is the word number %s in the text.\n' % (i, i+position_participle))
            
    #Informs how many present perfects are comprised in the text
    print('\nThis text has %s instances of present perfect.\n\n\n' % len(present_perfect_structure))



#Level B1, B2
#Differences between present perfect and past simple
#This is simply the union of two other functions
def ppVSps():
    present_perfect()
    past_tense_simple()




#Levels A2, B1, B2
#Function for matching phrasal verbs
def phrasal_verbs():
    phrasal_verb_structure = []
    
    for i in dic:
        
        #Detects verb particles
        if dic[i][6] == 'compound:prt':
            
            #Localizes the id of the verb in regard to the verb particle
            position_verb = int(dic[i][5]) - int(dic[i][0])

            #Assures that the target is actually a verb
            if dic[i+position_verb][3].startswith('VB'):
                verb = dic[i+position_verb]
                phrasal_verb_structure.append(i)
                
                
                #Prints the given phrasal verb:
                print(verb[1] + ' ' + dic[i][1] + ' = This verb is the word number %s and this particle is the word number %s in the text.\n' % (i+position_verb, i))
            
    #Informs how many present perfects are comprised in the text
    print('\nThis text has %s instances of phrasal verbs.\n\n\n' % len(phrasal_verb_structure))
    
    
    
#Level B1
#Function for matching assurance questions (complex question tags)
#Complex questions = You're crazy, AREN'T YOU?, You did this, DIDN'T YOU?, I didn't tell you that, DID I?
def complex_question():
    complex_question_structure = []
    
    verb_forms = ['can', 'may', 'do', 'be', 'must', 'shall', 'should', 'will', 'have']
    
    for i in dic:
        
        #Detects verb particles
        if dic[i][2] == '?':
            
            #Assures that the target is actually a verb
            if dic[i-1][2] == 'not' and dic[i-3][3].startswith('VB'):
                neg = dic[i-1]
                pronoun = dic[i-2]
                verb = dic[i-3]
                complex_question_structure.append(i)

                #Prints the given phrasal verb:
                print(verb[1] + ' ' + pronoun[1] + ' ' + neg[1] + dic[i][1] + ' = This verb is the word number %s and this negative particle is the word number %s in the text.\n' % (i-3, i-1))

            
            elif dic[i-1][3].startswith('PRP') and dic[i-3][3].startswith('VB') and dic[i-2][2] == 'not':
                neg = dic[i-2]
                pronoun = dic[i-1]
                verb = dic[i-3]
                complex_question_structure.append(i)
                
                
                #Prints the given phrasal verb:
                print(verb[1] + ' ' + neg[1] + ' ' + pronoun[1] + dic[i][1] + ' = This verb is the word number %s and this negative particle is the word number %s in the text.\n' % (i-3, i-2))
                
                
            elif dic[i-1][3].startswith('PRP') and dic[i-2][3].startswith('VB') and dic[i-2][2] in verb_forms:
                pronoun = dic[i-1]
                verb = dic[i-2]
                complex_question_structure.append(i)
                
                
                #Prints the given phrasal verb:
                print(verb[1] + ' ' + pronoun[1] + dic[i][1] + ' = This verb is the word number %s and this negative particle is the word number %s in the text.\n' % (i-2, i-1))
            
            
    #Informs how many present perfects are comprised in the text
    print('\nThis text has %s instances of complex questions.\n\n\n' % len(complex_question_structure))



#Level A2, B1, B2
#Function for detecting questions that begin with a WH-pronoun
def wh_question():
    wh = ['what', 'who', 'whose', 'whom', 'where', 'when', 'how', 'which', 'why']
    
    #Dic of wh and infos
    wh_dic = {}
    
    for i in dic:
        if dic[i][1] == '?':
            
            verb_pos = dic[i][5]
            
            #Searches for a wh-pronoun in the sentence
            for n in range(-1, -100, -1):
                if dic[i+n][2] in wh and dic[i+n][5] == verb_pos:
                    wh_dic[i+n] = dic[i+n]
                    print(wh_dic[i+n][1] + ' = This wh-pronoun is the word number %s in the text.\n' % str(i+n))
                    break


#============================= NAMED ENTITIES RECOGNITION =================================

#This function retrieves named entities from the annotated dictionary (using dependency and named entities tags)
def ner():
    
    named_entities = {}
    
    #Named entities that are of interest for us
    white_list = ['LOCATION', 'PERSON', 'ORGANIZATION']
    
    for i in dic:
        
        named_entity = []
        
        ner = ''
        
        #Searches only for new named entities of the types described on the white list
        if dic[i][4] in white_list and dic[i][1] not in named_entities:
            named_entity.append(dic[i][1])
            
            #Crawls the next four words to see if they are part of the named entity
            #The try-except is there to ensure it won't rise a problem at the end of a file
            try:
                if dic[i+1][4] == dic[i][4]:
                    named_entity.append(dic[i+1][1])
                    if dic[i+2][4] == dic[i][4]:
                        named_entity.append(dic[i+2][1])
                        if dic[i+3][4] == dic[i][4]:
                            named_entity.append(dic[i+3][1])
                            if dic[i+4][4] == dic[i][4]:
                                named_entity.append(dic[i+4][1])
            except KeyError:
                pass
            
            #Condenses multiword NEs into one and stores it in the named_entities list 
            for n in named_entity:
                if n == named_entity[0]:
                    ner = n
                else:
                    ner = ner + ' ' + n
            
            named_entities[dic[i][4] + '_' + dic[i][0]] = ner
            
    #Prints a list of named_entities        
    print(named_entities)


#============================= Wikipedia Search of Named Entities ============================

#Very simple function to open an wikipedia page by giving it the desired subject
def wikipedia(ner):
    webbrowser.open('https://en.wikipedia.org/wiki/' + ner)



######################################### TEST AREA ##########################################

#dic = conll_dic('gutenberg_conll/edgeworth-parents.txt.conll')

#adverb()
#adjectives_comp_super()
#past_tense_simple()
#modals()
#passive_voice()
#future_continuous()
#past_perfect()
#present_perfect_continuous()
#present_perfect()
#ppVSps()
#future()
#future_going_to()
#fsVSfgt()
#phrasal_verbs()
#past_continuous()
#complex_question()
#wh_question()
#ner()
#wikipedia('porto alegre')
