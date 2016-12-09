import os

example = ['if', 'If', 'had']

dir_corpus = 'gutenberg/'

for f in os.listdir(dir_corpus):
	text = open(dir_corpus + f, 'r', encoding='utf8')
	
	frase = []
	
	try:
		for l in text.readlines():
			try:
				if l[-2] != '.':
					frase.append(l)
					
				else:
					frase.append(l)
					line = ' '.join(frase).split(' ')
					frase = []
					for num,w in enumerate(line):
						if example[0] == w or example[1] == w:
							for i in range(-2, 2):
								try:
									if example[2] in line[num+i]:
										print(' '.join(line) + '\n\n\n\n')
								except: 
									pass
			except IndexError:
				pass
		
	except 	UnicodeDecodeError:
		pass			
	
	text.close()
