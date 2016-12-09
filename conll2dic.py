def conll_dic(conll_file, input_dir):

    #Creates an iterating key for inserting localized info from the
    #CONLL file to a dictionary 'info_conll'
    itr = 1
    sent = 1
    info_conll = {}


    #Opens the CONLL file
    f = open(input_dir + conll_file, 'r')
    for line in f:

        #Divides each line in the CONLL file and assigns a numbered key
        #to each entry in the dictionary
        if line != '\n':
            info_conll[itr] = line.strip('\n').split('\t')
            itr += 1
            
        #Marks in the dictionary the point where a sentence ends, and enumerate it
        else:
            info_conll[itr] = [sent, 'FIM_DE_SENTENCA_' + str(sent), '', '', '', '', '']
            itr += 1
            sent += 1
		
    return info_conll
        
