'''
Created on Jan 12, 2022

@author: ohbster
'''

class EntityBase(object):
    def sanitize(self, input_string):
        #test if the input is a type string before attempting to scrub
        if isinstance(input_string, str):
            print("Yay, string!")
            return ''.join(k for k in input_string if k.isalnum() or k == ' ' or k == '.')
            
        else:
            print("Scrub: None string input detected!")
            return input_string
        