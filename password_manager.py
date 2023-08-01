import string
import pandas as pd
df = pd.read_csv(r'D:\python\Projects\Encrypted_password_database .csv')
# def Unique_Element_Finder(colomn_name:str,colomn_index:int)->list:
'''Returns the list of unique elemets in a colomn(identified by its {colomn_name} and {colomn_index}) of a pandas datafram '''
Unique_Website_list=[]
for i in [df.iloc[i,0] for i in range(len(df['Facebook.com']))]:
    if i in Unique_Website_list:
        pass
    else:
        Unique_Website_list.append(i)
            
    # return Unique_Website_list
print(Unique_Website_list)

# def Unique_Element_Finder(df: pd.DataFrame, column_name: str) -> list:
#     '''Returns the list of unique elements in a column (identified by its {column_name}) of a pandas DataFrame.'''
#     unique_elements_list = [df[column_name].unique().tolist()]
#     return unique_elements_list

# def Unique_Element_Finder(df: pd.DataFrame, column_index: int) -> list:
#     '''Returns the list of unique elements in a column (identified by its {column_index}) of a pandas DataFrame.'''
#     unique_elements_list = df.iloc[:, column_index].unique().tolist()
#     return unique_elements_list




Website_name='Facebook.com'
filtered_df = df[df['Website'] == Website_name]

def Encrypter(initial_string:str,cypher:int=3)-> str:
    '''
    shift the postion of the element in the string base {cypher} No. of times
    '''
    encrypt=''    
    string_base=[i for i in (string.ascii_letters+string.digits+' ')]
    #'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 '          
    for letter in initial_string:        
        if letter in string_base:
            new_letter_index=string_base.index(letter)+cypher
            if new_letter_index>=len(string_base)-1:
                new_letter_index-=len(string_base)
                encrypt+=string_base[new_letter_index]
            else:
                encrypt+=string_base[new_letter_index]
        else:
            encrypt+=letter    

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
        if letter in string_base:     
            new_letter_index=string_base.index(letter)-cypher
            decrypt+=string_base[new_letter_index]
        else:
            decrypt+=letter
    return decrypt


lst1=[filtered_df.iloc[i,1] for i in range(len(filtered_df['Username']))]
lst2=[Decrypter(filtered_df.iloc[i,2]) for i in range(len(filtered_df['Password']))]


# encrypted=list(map(Encrypter,lst1))
# decrypted=list(map(Decrypter,encrypted))

# print(encrypted)
# print(decrypted)
# print(lst2)

paired_list=list(zip(lst1,lst2))
for i in paired_list:
    print('Facebook.com','->',i[0],'->',i[1])
