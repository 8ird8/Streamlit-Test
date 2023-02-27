# def greet(name):
#     return ('hello '+ name )
# name = input('enter ur name :')
# print(greet(name))
# #default parameters 
# def greet2(name='',status=''):
#     print('hello ' + name +' you are '+ status)

# greet2('achraf' )    
#Ex 1 
# find out if the word dog is in string 
def strr(string):
    if 'dog' in string :
        return True 
    else: 
        return False
print(strr('my name is achraf'))

def dog_check(string):
    return 'dog' in string 
print(dog_check('dog dof'))
 
 #Ex2 
 # if the word starts with a vowels, add 'ay' to the end 
 # if the word does not start with a vowel, put first letter at the end,  then add ay 

def Pig_latin(word):
   vowels=["a","e","i","o","u"]
   if word[0].lower() in vowels :
       return word + 'ay '
   else:
       return word[1:] + word[0] +'ay'
print(Pig_latin('same'))
   



