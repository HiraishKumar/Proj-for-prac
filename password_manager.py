import string
def Encrypter(initial_string:str,cypher:int=3)-> str:
    '''
    shift the postion of the element in the string base {cypher} No. of times
    '''
    encrypt=''    
    string_base=[i for i in (string.ascii_letters+string.digits+' ')]
    #'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 '
    for letter in initial_string:
        new_letter_index=string_base.index(letter)+cypher
        if new_letter_index>=len(string_base)-1:
            if letter in string_base:
                new_letter_index-=len(string_base)
                encrypt+=string_base[new_letter_index]
            else:
                pass
        else:
            encrypt+=string_base[new_letter_index]

    return encrypt   
 
def Decrypter(initial_string:str,cypher:int=3)-> str:
    '''
    shift the postion of the element in the string base BACK {cypher} No. of times
    (to mentain integrity decrypt with the same cypher as encryption)
    '''   
    decrypt=''
    string_base=[i for i in (string.ascii_letters+string.digits+' ')]
    #'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 '
    for letter in initial_string:        
        new_letter_index=string_base.index(letter)-cypher
        decrypt+=string_base[new_letter_index]
            
    return decrypt

import pandas as pd
df = pd.read_csv('password_database.csv')

df.loc[:, 'Password'] = Encrypter(df.loc[:, 'Password'])
df.head(10)