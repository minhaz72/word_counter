#hi , there let's build a word counting app : 
def character_couting(word) : 
    print(f' you have write{len(word)} number of charcter :  ')
def word_couting(word) : 
    coun=  word.split()
    print(f'you have write {len(coun)} number of word : ')
word= str(input('what is on your mind :  '))
a= str(input('to count word press a or count character press b :  '))
if a == 'a ' :
    word_couting(word)
elif a ==  'b'  :
    character_couting(word )
else : 
    print('invalid inpit : ')
    
    