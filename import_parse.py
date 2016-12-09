#import sys
#sys.path.append('/usr/local/lib/python3.5/site-packages')

import requests
import justext
import subprocess
import time
import re


def import_webpage(web_page, input_dir):

	#Retrieves the desired web page text contents:
	response = requests.get(web_page)
	paragraphs = justext.justext(response.content, justext.get_stoplist("English"))


	#Creates a temporary file (strips some symbols from the web page name and shortens name)
	#in the input_dir folder for storing the text contents of a web page:
	if len(web_page) >= 50:
	  tmp_file = re.sub('http|:|\/|\%|\.|\=|\&|\?|\!|\~', '', web_page)[:50] + '.tmp'
	else:
	  tmp_file = re.sub('http|:|\/|\%|\.|\=|\&|\?|\!|\~', '', web_page) + '.tmp'

	text_tmp = open(input_dir + tmp_file, 'w', encoding='utf-8')
	
	#Print the text contents of the web page to the temporary file
	for paragraph in paragraphs:
	  if not paragraph.is_boilerplate:
	    text_tmp.write(paragraph.text + '\nFIM_DE_PARAGRAFO.\n')
	
	text_tmp.close()
	return tmp_file
	

#Uses Stanford Core NLP to parse a stored file
def coreNLP(tmp_file, input_dir, output_dir):
	
	#Absolute path to CoreNLP
	core_nlp_dir = '/home/zilio/Downloads/Stanford_NLP_Core/'
	
	#Runs CoreNLP
	print('Parsing...')
	time_now = time.time()
	subprocess.run([core_nlp_dir + './corenlp.sh', '-annotators tokenize,ssplit,pos,lemma,ner,parse',
	                '-nthreads 4', '-file ' + input_dir + tmp_file, '-outputFormat conll', '-outputDirectory ' + output_dir])
	print('Done! The parsing process took %.2f seconds.' % (float(time.time() - time_now)))
