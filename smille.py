from import_parse import import_webpage, coreNLP
from conll2dic import conll_dic
from wordnet_sense import wordnet_sense
from process_dic import adverb, adjectives_comp_super
from text_rebuilder import rebuild_text
import time


print('Processing.../n/n')
time_now = time.time()


data_dir = 'data/'
output_dir = 'output/'
core_output = 'conll/'
html_output = 'html/'
web_page = "http://www.nytimes.com/2016/12/08/opinion/the-ghosts-spain-tries-to-ignore.html?_r=0"

tmp_file = import_webpage(web_page, data_dir)

coreNLP(tmp_file, data_dir, output_dir)

dic = conll_dic(tmp_file + '.conll', output_dir)

#Counts number of sentences in the CONLL file, if needed
#This option is off by default, to activate it, remove the
#comment on the line 'dic_counter(dic)'
#def dic_counter(dic):
#	sentences = 0
#	for entry in dic:
#		if dic[entry][1].startswith('FIM_DE_SENTENCA'):
#			sentences += 1
#	
#	print('Number of sentences = %s.' % sentences)

#dic_counter(dic)

test_1 = adverb(dic)
test_2, test_3, test_4 = adjectives_comp_super(dic)
test_2 = []

rebuild_text(dic, tmp_file + '.conll', html_output, test_1, test_2, test_3, test_4)

print('/n/n/n/nDone! The whole process took %.2f seconds.' % (float(time.time() - time_now)))
