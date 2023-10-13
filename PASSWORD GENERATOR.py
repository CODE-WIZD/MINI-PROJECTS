import string
import random

def generate_pwd(minlength,number=True,specialchr=True):
    letter=string.ascii_letters
    num=string.digits
    schar=string.punctuation

    character=letter
    if (number=True):
        character+=num
    if (specialchhr=True):
        character+=schar

    pwd=""
    meets_criteria=False
    has_num=False
    has_schar=False
    while not meets_criteria or pwd<len(minlength):
        newchr=random.choice(character)
        pwd+=newchar

        if newchar in num:
            has_num=True
        if newchar in schar:
            has_schar=True
            
        
        

    
generate_pwd(10)
