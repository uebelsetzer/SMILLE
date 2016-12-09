#Recreates a text from dictionary and prints it to an HTML file

import webbrowser
from conll2dic import conll_dic

def rebuild_text(dic, conll_file, output_dir, test_1, test_2=[], test_3=[], test_4=[], test_5=[]):
	
	#POS tag to textual POS conversion
	POStags = {'CC': 'Conjunction', 'CD': 'Cardinal Number', 'DT': 'Determiner', 'EX': 'Existential THERE', 'FW': 'Foreign Word', 'IN': 'Preposition or Subordinate Conjunction', 
				'JJ': 'Adjective', 'JJR': 'Comparative Adjective', 'JJS': 'Superlative Adjective', 'LS': 'List Item', 'MD': 'Modal Verb', 'NN': 'Common Noun Singular', 
				'NNP': 'Proper Noun Singular', 'NNPS': 'Proper Noun Plural', 'NNS': 'Common Noun Plural', 'PDT': 'Pre-determiner', 'POS': 'Genitive Marker',
				'PRP': 'Personal Pronoun', 'PRP$': 'Possessive Pronoun', 'RB': 'Adverb', 'RBR': 'Comparative Adverb', 'RBS': 'Superlative Adverb', 'RP': 'Particle',
				'SYM': 'Symbol', 'TO': 'Infinitive TO', 'UH': 'Interjection', 'VB': 'Base Form of Verb', 'VBD': 'Past Form of Verb', 'VBG': 'Gerund or Present Participle',
				'VBN': 'Past Participle', 'VBP': 'Present Form of Verb, not 3rd Person', 'VBZ': 'Present Form of Verb, 3rd Person', 'WDT': 'WH-determiner', 'WP': 'WH-pronoun',
				'WP$': 'Possessive WH-pronoun', 'WRB': 'WH-adverb'}
	
	#Symbols that should not have a space before them
	punctuation = ['.', '?', '!', ',', ';', ':', '--']
	contractions = ["'s", "'ve", "'d", "n't", "'ll", "'m", "'re"]
	
	#Symbols modified by the parser and that need to be replaced in text
	brackets = ['-LSB-', '-RSB-', '-LRB-', '-RRB-', '``', "''", '`', "'"]
	text_brackets = ['[', ']', '(', ')', '"', '"', "'", "'"]
	
	#Stores information from the dic
	paragraph = []
	
	#Output HTML file
	output = open(output_dir + conll_file + '.html', 'w', encoding='utf-8')
	
	#Writes beginning of the HTML file
	output.write('<!DOCTYPE html>\n<html lang="en">\n\n<head>\n\n<meta charset="utf-8"/>\n\n<link rel="stylesheet" type="text/css" href="css/style.css">\n\n</head>\n\n<body id="main">\n\n<div class="tooltip" style="display:none"></div>\n\n<iframe id="wordnet" style="display:none"></iframe>\n\n')
	
	#Writes the right-hand panel with content info
	output.write('<div id="mySidenav" class="sidenav">\n<a href="javascript:void(0)" class="closebtn" onclick="closeNav()">&times;</a>\n<a href="#">About</a>\n<a href="#">Services</a>\n<a href="#">Clients</a>\n<a href="#">Contact</a>\n</div>\n\n\n<button type="button" id="navButton">Menu</button>\n')
	
	
	for i in dic:

		#IMPORTANT PART = HERE IS THE CODE THAT PRINTS EACH PARAGRAPH TO AN HTML FILE
		#Searches for inserted end of paragraph markers and uses them as mark 
		#for writing each paragraph to an html file
		if int(i) > 1 and dic[i-1][1].startswith('FIM_DE_PARAGRAFO') and paragraph != []:
			output.write('<p>')
			for p in paragraph:
				output.write(p)

			paragraph = []
		
		#Makes sure there is no space after brackets and beginning of quotes
		elif i > 1 and dic[i-1][1] == brackets[0] or i > 1 and dic[i-1][1] == brackets[2] or i > 1 and dic[i-1][1] == brackets[4] or i > 1 and dic[i-1][1] == brackets[6]:
			paragraph.append(dic[i][1])
		
		#Removes end of sentence marker from dic
		elif dic[i][1].startswith('FIM_DE_SENTENCA'):
			pass
		
		#Searches for end of paragraphs
		elif dic[i][1].startswith('FIM_DE_PARAGRAFO'):
			paragraph.append('</p>\n\n')
		
		#Searches for punctuation and contractions that doesn't need space before it
		elif dic[i][1] in punctuation: 
			paragraph.append(dic[i][1])
		
		elif dic[i][1] in contractions:
			try:
				POStag = POStags[dic[i][3]]
			except KeyError:
				print(str(dic[i]))
				
			#Each test corresponds to a different tag, that will later be manipulated
			#by a CSS and a JS file
			tags = []
			endtag = '</tag>'			
			
			if i in test_1:
				tags.append('<tag class="Tag1">')
			if i in test_2:
				tags.append('<tag class="Tag2">')
			if i in test_3:
				tags.append('<tag class="Tag3">')
			if i in test_4:
				tags.append('<tag class="Tag4">')
			if i in test_5:
				tags.append('<tag class="Tag5">')
			if len(tags) > 0:
				
				
				beginningtag = ''.join(tags)
				paragraph.append(beginningtag + '<span  id="' + str(i) + '" pos="' + dic[i][3] + '" lemma="'+ dic[i][2] + '" title="' + POStag + '&#13;Word = ' + dic[i][2] + '">' + dic[i][1]  + '</span>' + len(tags)*endtag)
			else:
				paragraph.append('<span id="' + str(i) + '" pos="' + dic[i][3] + '" lemma="'+ dic[i][2] + '" title="' + POStag + '&#13;Word = ' + dic[i][2] + '">' + dic[i][1] + '</span>')
				
		#Searches for brackets and substitutes them by their correct symbol
		elif dic[i][1] in brackets:
			for n,b in enumerate(brackets):
				if b == dic[i][1] and n % 2 == 0:
					paragraph.append(' ' + text_brackets[n])
				elif b == dic[i][1] and n % 2 == 1:
					paragraph.append(text_brackets[n])
					
		#Any other type of word or symbol that desn't require special treatment (except if being in a test)
		else:
			
			try:
				POStag = POStags[dic[i][3]]
			except KeyError:
				print(str(dic[i]))

			
			#Each test corresponds to a different tag, that will later be manipulated
			#by a CSS and a JS file
			tags = []
			endtag = '</tag>'			
			

			
			if i in test_1:
				tags.append(' <tag class="Tag1">')
			if i in test_2:
				tags.append(' <tag class="Tag2">')
			if i in test_3:
				tags.append(' <tag class="Tag3">')
			if i in test_4:
				tags.append(' <tag class="Tag4">')
			if i in test_5:
				tags.append(' <tag class="Tag5">')
			if len(tags) > 0:
				
				
				beginningtag = ''.join(tags)
				paragraph.append(' ' + beginningtag + '<span id="' + str(i) + '" pos="' + dic[i][3] + '" lemma="'+ dic[i][2] + '" title="' + POStag + '&#13;Word = ' + dic[i][2] + '">' + dic[i][1]  + '</span>' + len(tags)*endtag)
			else:
				paragraph.append(' <span id="' + str(i) + '" pos="' + dic[i][3] + '" lemma="'+ dic[i][2] + '" title="' + POStag + '&#13;Word = ' + dic[i][2] + '">' + dic[i][1] + '</span>')


	
	output.write('<script src="js/jQuery.js"></script>\n\n<script src="js/dic.js"></script>\n\n<script src="js/style.js"></script>\n\n</body>\n</html>')
	output.close()
	
	webbrowser.open(output_dir + conll_file + '.html')

########################Test Area#####################

#conll_file = 'senwikipediaorgwikiBird_of_prey.tmp.conll'

#dic = conll_dic(conll_file, 'output/')

#rebuild_text(dic, conll_file, 'html/')
