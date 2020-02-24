#Decryption
from termcolor import colored,cprint

cprint('Welcome to the Decrypter, Developed By Siddhant Khare','yellow',attrs=['blink'])


decrypter = {
'N' : '0' ,'H' : '9' ,'X' : '8' ,'G' : '7' ,'P' : '6' ,'T' : '5' ,'A' : '4' ,'U' : '3' ,'Y' : '2','V' : '1'  
  
  
,'g' : 'Z' , 'l' : 'Y' ,'i' : 'X' ,'h' : 'W' ,'|' : 'V' ,'t' : 'U' ,'u' : 'T' , 'j' : 'S' ,'k' : 'R' ,'n' : 'Q' ,'m': 'P' ,'y' : 'O' ,'r' : 'N' , 'f' : 'M' ,'e' : 'L' ,'d' :'K' , 'c' : 'J' , 'b' : 'I' , 'v' : 'H', 'x' : 'G' , 'a' : 'F' , 'z' : 'E' , 's' : 'D' ,'q' :'C' , '<' : 'B' , '>' : 'A'  
 
 
,'.' : ' ' , '[' : 'z', ']' : 'y' , '(' : 'x' , ')' : 'w' , '=' : 'v' , '`' : 'u' , '~' : 't' , '!' : 's' , '#' : 'r' , '-' : 'q' , '+' : 'p' , '?' : 'o' , '/' : 'n' , '*' : 'm' , '$' : 'l' , '%' : 'k' , '5' : 'j' , '8' : 'i' , '2' : 'h' , '6' : 'g' , '3' : 'f' , '9' : 'e' , '1' : 'd'  , '7' : 'c'  , '4' : 'b' ,'0' : 'a' 

}


message = str(input('\nEnter Encrypted Message : '))

print('\nInput : ' + '\n' + message + '\n')
print('Output : ' )

length = len(message)
for i in range(0,length):
  print(decrypter[message[i]],end='')
  
print('\n\nHope you like this code, Please give it a Thumbs up i.e (+1)')


