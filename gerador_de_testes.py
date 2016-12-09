#import sys
#sys.path.append('/usr/local/lib/python3.5/site-packages')

import requests
import justext
import subprocess
import time
import re
from conll2dic import conll_dic

gutenberg = ['austen-persuasion.txt', 'bryant-stories.txt', 'carroll-alice.txt', 'shakespeare-hamlet.txt']

#Absolute path to CoreNLP
core_nlp_dir = '/home/zilio/Downloads/Stanford_NLP_Core/'

input_dir = 'data/'
output_dir = 'output/'


for f in gutenberg:
	tmp_file = f

#with open(input_dir + 'gutenberg_complete', 'w', encoding='utf8') as outfile:
	
	#for text in gutenberg:
		#print(text)
		#outfile.write('\n')
		#f = open(text, 'r', encoding='utf8')
		#try:	
			#for line in f:
				#outfile.write(line)
		#except UnicodeDecodeError:
			#pass
				
				
	#Uses Stanford Core NLP to parse the stored file
	
	#Runs CoreNLP
	print('Parsing ' + tmp_file)
	time_now = time.time()
	subprocess.run([core_nlp_dir + './corenlp.sh', '-annotators tokenize,ssplit,pos,lemma,ner,parse',
	                '-file ' + input_dir + tmp_file, '-outputFormat conll', '-outputDirectory ' + output_dir])
	print('Done! The parsing file %s process took %.2f seconds.' % (f, float(time.time() - time_now)))


#dic = conll_dic(tmp_file + '.conll')

#Counts number of sentences in the CONLL file, if needed
#sentences = 0
#for entry in dic:
    #try: 
        #if int(dic[entry][0]) >= int(dic[entry+1][0]):
            #sentences += 1
    #except KeyError:
        #sentences += 1
        #print('Number of sentences = %s.' % sentences)
