def process_info(text_string):

    key_words = ['Project:', 'Hole:', 'Depth:', 'Description:', 'Samples:',\
                 'Groundwater:']
    proj = ''
    hole = ''
    depth = []
    descr = []
    samples = {}
    gw = []

    #this splits the string into words, it splits wherever there is a space
    text = text_string.split()

    for i in range(len(text)-1):
        #create a temporary list containing the remainder of the text
        #this allows you to find the next key word without finding the current
        #word (if it is a key word)
        temp_list = []
        temp_list.extend(text[i+1:len(text)])
        
        if text[i] == 'Depth:':
            #this is in case the remaining text doesn't contain a key word i.e.
            #the last piece of information in the text. without this the last
            #bit of info wouldn't be saved to a list
            if any(x in key_words for x in temp_list) == False:
                depth.extend(temp_list[0:len(temp_list)])
            #this tells it to add the following words in the test to a list,
            #until it comes to a keyword at which point it stops (not including
            #the key word)   
            else:    
                depth.extend(temp_list[0:temp_list.index(next(x for x in \
                                                              temp_list if x \
                                                              in key_words))])

        elif text[i] == 'Description:':
            descr_list = []
            if any(x in key_words for x in temp_list) == False:
                descr_list = temp_list[0:len(temp_list)]
                descr.append(' '.join(descr_list))
            else:
                descr_list = temp_list[0:temp_list.index(next(x for x in \
                                                              temp_list if x \
                                                              in key_words))]
                descr.append(' '.join(descr_list))

        elif text[i] == 'Project:':
            if any(x in key_words for x in temp_list) == False:
                proj = ''.join(temp_list[0:len(temp_list)])
            else:    
                proj = ''.join(temp_list[0:temp_list.index(next(x for x in \
                                                              temp_list if x \
                                                              in key_words))])

        elif text[i] == 'Hole:':
            if any(x in key_words for x in temp_list) == False:
                hole = ''.join(temp_list[0:len(temp_list)])
            else:    
                hole = ''.join(temp_list[0:temp_list.index(next(x for x in \
                                                              temp_list if x \
                                                              in key_words))])

        elif text[i] == 'Samples:':
            #makes a list of samples which will then be split into depths and
            #sample types and input into the samples dictionary
            samples_list = []
            if any(x in key_words for x in temp_list) == False:
                samples_list.extend(temp_list[0:len(temp_list)]) 
            else:    
                samples_list.extend(temp_list[0:temp_list.index(next(x for x in \
                                                              temp_list if x \
                                                              in key_words))])
            #iterates through the samples in samples_list
            for j in range(len(samples_list)):
                #samples that start with E will have two letters for the sample
                #type - ES or EW
                if samples_list[j][0] == 'E':
                    sample_type = samples_list[j][0] + samples_list[j][1]
                    sample_depth = ''
                    #samples in sample list will be separated by commas, if the
                    #sample is the last one in the sample list then the whole
                    #of the remainder of the string is  the depth. otherwise
                    #we need to subtract the comma
                    if j == len(samples_list)-1:
                        for y in range(2, len(samples_list[j])):
                            sample_depth += samples_list[j][y]
                    else:
                        for y in range(2, len(samples_list[j])-1):
                            sample_depth += samples_list[j][y]
                            
                    samples[sample_depth] = sample_type
                #same but for samples with only one letter in the sample type
                #i.e. B, D, U
                else:
                    sample_type = samples_list[j][0]
                    sample_depth = ''
                    
                    if j == len(samples_list)-1:
                        for y in range(1, len(samples_list[j])):
                            sample_depth += samples_list[j][y]
                    else:
                        for y in range(1, len(samples_list[j])-1):
                            sample_depth += samples_list[j][y]
                   
                    samples[sample_depth] = sample_type

        elif text[i] == 'Groundwater:':
            if any(x in key_words for x in temp_list) == False:
                gw.extend(temp_list[0:len(temp_list)])  
            else:    
                gw.extend(temp_list[0:temp_list.index(next(x for x in \
                                                              temp_list if x \
                                                              in key_words))])
             
    return proj, hole, depth, descr, samples, gw

