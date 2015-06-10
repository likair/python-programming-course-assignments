'''
Created on 20.5.2015

    A program which finds and displays all words, whcih end with 'y' in the following text: "The sky may be sunny 
    or cloudy, but still you should try to do your best to achieve your tiny joy.".

@author: e1201757
'''
import re
    
text = 'The sky may be sunny or cloudy, but still you should try to do your best to achieve your tiny joy.'

print([word for word in re.split('\W+', text) if re.match('.*y$', word)])
    