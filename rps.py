import random
import sys
import pyttsx3

engine = pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def exit_game():
	sys.exit()


engine = pyttsx3.init()

speak('Hello user I am Jack, Jeevan\'s personal assistant')


speak('What is your name')
name = input('What is your name ? -->')
if name == 'Jeevan':
    speak('oh sir, you are playing this game, I am excited to see you here')
    print('oh sir, you are playing this game, I am excited to see you here')
print('Hello '+ name + ' , nice to meet you' )
speak('Hello '+ name + ' , nice to meet you')

speak('Are you sure you are going to play the rock paper scissors game ?')
confirm = input('Are you sure you are going to play the rock paper scissors game ? -->')
confirm.lower()

if 'yes' in confirm:
	speak('you can proceed !')
	print(speak)
else:
	print('okay no problem')
	speak('okay no exceptions !')
	exit_game()

print('These are the set of rules to play the game :-')
print('! - The player will be plaing with the computer')
print('! - The player or the computer wins if they defeat each other')
print('! - The player does not need to write all the letters in lower case letters')
print('! - The computer also has a life')
speak('These are the set of rules to play the game :-')
speak('! - The player will be plaing with the computer')
speak('! - The player does not need to write all the letters in lower case letters if they wish to')
speak('! - The computer also has a life')
speak('! - The player or the computer wins if they defeat each other')
speak('please enter yes or no to begin the game')
game_enter = input('please enter yes / No to begin -->')
game_enter.lower()

if 'yes' in game_enter:
	speak('have fun playing')
	print('Have fun playing')
else:
	speak('why are you leaving the game ?')
	print('why are you leaving the game ?')
	reason = input()
	speak('ohh okay I understand, see you later')
	print('oh okay I understand, see you later')
	exit_game()



Honesty = True

while Honesty:
    
    speak('Choose your decision, rock, paper, scissors')
    desicion = input('Rock, Paper, Scissors --> ')
    desicion.lower()

    computer = random.choice(['rock', 'paper', 'scissors'])
   
    speak(computer)
    print(computer)
            

    if desicion == computer:
        speak('it is a draw')
        print('it is a draw')
        ask_draw = input('Do you want to retry say y / n -->')
        ask_draw.lower()

        if ask_draw == 'y':
        	continue
        else:
        	break
    
    if desicion == 'rock' and computer == 'paper' or desicion == 'paper' and computer == 'scissors' or desicion == 'scissors' and computer == 'rock':
        speak('yeah ! I win')
        print('yeah ! I win')  
    
    if computer == 'rock' and desicion == 'paper' or computer == 'paper' and desicion == 'scissors' or computer == 'scissors' and desicion == 'rock':
        speak(name + ' ,you defeated the computer')
        print(name + ' ,you defeated the computer')

        speak('do you want to retry ?')
        ask_user = input('Do you want to retry say y / n -->') 
        ask_user.lower()
        
        if ask_user == 'y':
        	continue
        else:
        	break



            


    





