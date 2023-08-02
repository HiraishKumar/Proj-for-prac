import string
import pandas as pd
df = pd.read_csv(r'D:\python\Projects\Encrypted_password_database .csv')

def Unique_element(colomn_name:str,Enumer:int=None)->list:
    '''returns list of unique elements in a colomn {colomn_name} 
    of pd.DataFrame which are enumerated if a starting enumer is specified'''
    if Enumer != None:
        Unique_element_list=[(j,i) for j, i in enumerate(df[colomn_name].unique(),start=Enumer)]
    else:
        Unique_element_list=[i for i in df[colomn_name].unique()]                
    return Unique_element_list
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
def Filter(_colomn_name_:str,_Entry_name:str)->list:
    '''returns a filtered Pd.DataFrame based with the Name of entries in the website colomn'''
    return df[df[_colomn_name_] == _Entry_name]
def Zipper(colomn_1:str,Colomn_2:str,_Site_Name)->list:  
    '''filtering(on the basis of site name) and zipping(of specified 
    {colomn_1 and colomn_2}) into a paired list)'''
    filtered_df=Filter('Website',_Site_Name)  
    lst1=[filtered_df.iloc[i,1] for i in range(len(filtered_df[colomn_1]))]
    lst2=[filtered_df.iloc[i,2] for i in range(len(filtered_df[Colomn_2]))]
    return list(zip(lst1,lst2))


Enumer_site=Unique_element('Website',1)
#make the initaial display of websites in stre
for i in Enumer_site:
    print(*i)

#user input of which website data to access
while True:
    Site_index=input('specify the index of the website to be acessed: ')
    try:
        Site_index=int(Site_index)
        if 1<= Site_index<= len(Enumer_site):
            Site_index-=1
            break
        else:
            print('Invalid Index. Try Again')
    except ValueError:
        print('Invalid Index Type. Try Again')
        
Site_name=Enumer_site[Site_index][1]

# filtering(on the basis of site name from user inputed index) 
# and zipping(of specified {colomn_1 and colomn_2}) into a paired list)    

paired_list=Zipper('Username','Password',Site_name)
for j,i in enumerate(paired_list,start=1):
    print(j,f'{Site_name}','->',i[0])
        
#user input of which username data to access    
while True:
    Name_index = input('Specify the index of the username to be accessed: ')
    try:
        Name_index = int(Name_index)  # Convert user input to an integer
        if 1 <= Name_index <= len(paired_list):
            Name_index -= 1
            # print(Name_index)
            break
        else:
            print('Invalid Index. Try Again')
    except ValueError:
        print('Invalid Index Type. Try Again.')
        
#master Key to access data        
while True:
    user_input = input('Input Master Key: ')
    if user_input == 'Life After Death':
        print(paired_list[Name_index][0], '->', Decrypter(paired_list[Name_index][1]))
        break
    else:
        print("Invalid Key. Try Again.")        



