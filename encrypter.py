# Project name  : Encrypter
# Please give it a (+1) If you like it..
# Author :- Siddhant Khare


# Input :
# 'alphabets' - Allowed
# 'ALPHABETS' - Allowed
# '1234567890' - Allowed
# '^&*(#+/*-' - Not Allowed !

# Hope you like it !


from termcolor import colored,cprint
import replit
import time

replit.clear()

cprint('Hello, This Encrypter is developed by Siddhant Khare! ','cyan',attrs=['blink'])


cprint(' \n\nSuccesfully running ......\n','yellow')

time.sleep(3)


dictionary = {
  
  'a' : '0', 'b' : '4' ,  'c' : '7' ,  'd' : '1' , 'e' : '9' , 'f' : '3' , 'g' : '6' , 'h' : '2' , 'i' : '8' , 'j' : '5' , 'k' : '%' , 'l' : '$' , 'm' : '*' , 'n' : '/' , 'o' : '?' , 'p' : '+' , 'q' : '-' , 'r' : '#' , 's' : '!' , 't' : '~' , 'u' : '`' , 'v' : '=' , 'w' : ')' , 'x' : '(' , 'y' : ']' ,'z' : '[' , ' ' : '.',
 
 
  'A' : '>' , 'B' : '<' , 'C': 'q', 'D' : 's' , 'E' : 'z' , 'F' : 'a' , 'G' : 'x' ,'H' : 'v' , 'I' : 'b' , 'J' : 'c' , 'K': 'd', 'L' : 'e', 'M' : 'f' , 'N' : 'r', 'O' : 'y', 'P' :'m', 'Q' : 'n', 'R' : 'k', 'S' : 'j' , 'T' : 'u', 'U' : 't', 'V' : '|', 'W' : 'h', 'X' : 'i', 'Y' : 'l' , 'Z' : 'g',
  
  
  '1' : 'V','2' : 'Y', '3' : 'U', '4' : 'A', '5' : 'T', '6' : 'P', '7' : 'G', '8' : 'X', '9' : 'H', '0' : 'N',

}



message = str(input('Enter any message without using any Symbols : '))

print('\nInput : ' + '\n'+ message +'\n')

print('Output : ' )

length = len(message)

for i in range(0,length):
  print(dictionary[message[i]], end ='')
  
print('\n\n\n↑ Above, is your encrypted message... ')  
print('Copy and paste it in the decrypter to get the decrypted message of encryption !..')
cprint('\nMade by John_123','cyan',attrs=['bold'])

